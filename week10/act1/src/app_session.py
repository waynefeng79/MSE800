from user_manager import UserManager
from enum import IntEnum
from database import Database

class StateMachine(IntEnum):
    """Menu states used by the command-line session loop."""

    MAIN          = 0
    QUIT          = 1
    LOGIN         = 2
    LOGOUT        = 3
    REGISTER      = 4
    UPDATE_USER   = 5
    MANAGE_USERS  = 6

class AppSession:
    """Application session."""

    def __init__(self, db: Database):
        self.user = None
        self.state = StateMachine.MAIN
        self.db = db
        self.user_manager = UserManager(db)

    def _session_user_info(self):
        if self.user:
            return f"user_id={self.user.id}, user_name={self.user.user_name}"
        return "user_id=None, user_name=None"

    def _confirm(self, prompt: str) -> bool:
        return input(prompt).strip().lower() == "y"

    def run(self):
        # Dispatch to one handler per state until a handler sets QUIT.
        while True:
            if self.state == StateMachine.MAIN:
                self.main()
            if self.state == StateMachine.QUIT:
                break
            elif self.state == StateMachine.LOGIN:
                self.login()
            elif self.state == StateMachine.LOGOUT:
                self.logout()
            elif self.state == StateMachine.REGISTER:
                self.register()
            elif self.state == StateMachine.UPDATE_USER:
                self.update_user(self.user)
            elif self.state == StateMachine.MANAGE_USERS:
                self.manage_users()
            else:
                print("Invalid state!!!")

    def _show_main_states(self):
        states = []
        # Keep menu numbers aligned with the state list returned to main().
        print("0. Quit")
        states.append(StateMachine.QUIT)
        print("1. Register")
        states.append(StateMachine.REGISTER)
        if not self.user:
            print("2. Login")
            states.append(StateMachine.LOGIN)
        else:
            print(f"2. Logout {self.user.user_name}")
            states.append(StateMachine.LOGOUT)
            if self.user.admin:
                print("3. Manage Users")
                states.append(StateMachine.MANAGE_USERS)
            else:
                print("3. Update User Profile")
                states.append(StateMachine.UPDATE_USER)

        return states

    def main(self):
        states = []
        while True:
            uname = self.user.user_name if self.user else ""
            print(f"\n== Main page ({uname}) ==")
            states = self._show_main_states()
            try:
                choice = int(input(f"select command (0-{len(states) - 1}): "))
                if choice < 0 or choice >= len(states):
                    print("Command out of range! Try again.")
                    continue
            except(ValueError):
                print("Command must be a number! Try again.")
                continue
            self.state = states[choice]
            break

    def login(self):
        print("\n== Login ==")
        self.user = self.user_manager.login(input("username: "), input("password: "))
        if not self.user:
            print("Login failed")
        self.state = StateMachine.MAIN

    def logout(self):
        print("\n== Logout ==")
        self.user = None
        self.car = None
        self.start_date = None
        self.end_date = None
        self.state = StateMachine.MAIN

    def register(self):
        print("\n== Register ==")
        uname = input("Username: ")
        pwd = input("Password: ")
        full_name = input("Full Name: ")
        email = input("Email: ")
        if self.user_manager.signup(uname, full_name, email, pwd):
            print("Registration successful! You can now log in.")
        else:
            print("Registration failed. Username might be taken.")
        self.state = StateMachine.MAIN

    def _show_user(self, user, show_header, show_foot):
        header = f"{'id':<4} | {'user_name':<15} | {'full_name':<20} | {'email':<25} | {'role':<8} | {'active':<5}"
        separator = "-" * len(header)

        if show_header:
            print("\n" + header)
            print(separator)

        role = "Admin" if user.admin else "Customer"
        active_text = "True" if user.active else "False"
        print(f"{user.id:<4} | {user.user_name:<15} | {user.full_name:<20} | {user.email:<25} | {role:<8} | {active_text:<5}")
    
        if show_foot:
            print(separator + "\n")

    def _get_user(self, users, id):
        user = None
        try:
            user_id = int(id)
            for u in users:
                if u.id == user_id:
                    user = u
                    break
        except Exception:
            pass
        return user

    def _update_user(self, user):
        # Blank profile fields keep their current values.
        full_name = input(f"Full Name ({user.full_name}): ") or user.full_name
        email = input(f"Email ({user.email}): ") or user.email
        pwd = input("Password (blank for unchanged): ")
        if user.admin:
            admin_input = input(f"Admin ({'y' if user.admin else 'n'}) (y/n): ").strip().lower()
            if admin_input == "":
                is_admin = user.admin
            else:
                is_admin = admin_input == "y"
        else:
            is_admin = False
        if self.user_manager.update(user, full_name, email, pwd if pwd != "" else None, is_admin):
            user.full_name = full_name
            user.email = email
            user.admin = is_admin

    def update_user(self, user):
        print("\n== Update User Profile ==")

        if not user:
            print("Invalid user in session.")
        else:
            self._show_user(user, True, True)
            self._update_user(user)
        self.state = StateMachine.MAIN

    def _filter_users(self):
        users = []
        while True:
            print("\nFilter by: 0. user_name, 1. full_name, 2. email, 3. is_admin 4. show all")
            choice = input("Select an option (0-4): ")
            # Map the menu choices to your database column names
            column_map = {
                "0": "user_name",
                "1": "full_name",
                "2": "email",
                "3": "is_admin"
            }
            if choice == "4" or choice == "":
                users = self.user_manager.filter()
            elif choice in column_map:
                column_name = column_map[choice]
                search_term = input(f"Enter search term for {column_name}: ")
                # We pass the column name as a key in a dictionary using ** unpacking
                filters = {column_name: search_term}
                users = self.user_manager.filter(**filters)
            else:
                print("Invalid selection. Try again.")
                continue
            break
        return users
    
    def _select_user(self, users):
        user = None
        while True:
            id = input("Enter user ID to update (blank for quit): ")
            if id == "":
                break
            user = self._get_user(users, id)
            if not user:
                print("Wrong ID. Try again.")
            else:
                break
        return user
    
    def _operate_users(self, users):
        while(True):
            choice = input("Operation (0. quit, 1. update, 2. activate 3. deactivate): ")
            if choice == "0" or choice == "":
                self.state = StateMachine.MAIN
                break
            user = self._select_user(users)
            if user:
                if choice == "1":
                    self._update_user(user)
                    break
                elif choice == "2":
                    if self.user_manager.activate(user, True):
                        user.active = True
                    break
                elif choice == "3":
                    if self.user_manager.activate(user, False):
                        user.active = False
                    break
                else:
                    print("Wrong operation. Try again.")
            else:
                print("No user selected. Operation cancelled.")
    
    def manage_users(self):
        print("\n== Manage Users ==")

        if not self.user or not self.user.admin:
            print("Invalid user in session.")
            self.state = StateMachine.MAIN
        else:
            users = self._filter_users()
            for i in range(len(users)):
                self._show_user(users[i], i == 0, i == len(users) - 1)
            if len(users) > 0:
                self._operate_users(users)
            else:
                print("Found no users.")
                self.state = StateMachine.MAIN
