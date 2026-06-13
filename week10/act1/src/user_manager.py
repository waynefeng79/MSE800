import sqlite3
import hashlib
import os
from user import User
from base_manager import BaseManager

class UserManager(BaseManager):
    """Handles database interactions and User object creation."""

    def __init__(self, db):
        self.db = db
        # Create table if necessary
        self._create_table()
        # Register a default admin if not existing
        self.signup("admin", "Admin", "admin@carrental.com", "admin", is_admin=True)

    def _create_table(self):
        conn = self.db.get_connection()
        try:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT UNIQUE NOT NULL,
                        full_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password_hash BLOB NOT NULL,
                        salt BLOB NOT NULL,
                        is_admin INTEGER DEFAULT 0,
                        inactive INTEGER DEFAULT 0
                    )
                """)
        except sqlite3.Error as e:
            print(f"Database create tables exception: {e}")
        finally:
            conn.close()

    def _hash_password(self, password, salt=None):
        # Reuse the stored salt on login; generate a new salt when saving a password.
        if salt is None:
            salt = os.urandom(32)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return pwd_hash, salt

    def signup(self, user_name, full_name, email, password, is_admin=False):
        print(f"UserManager register (user_name: {user_name})")
        retval = False
        pwd_hash, salt = self._hash_password(password)
        conn = self.db.get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (user_name, full_name, email, password_hash, salt, is_admin)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (user_name, full_name, email, pwd_hash, salt, 1 if is_admin else 0)
                )
                user_id = cursor.lastrowid
                print(f"""UserManager register succeeded (user_id: {user_id}, user_name:
                       {user_name})""")
                retval = True
        except sqlite3.IntegrityError as e:
            # user_name is unique, so duplicate registration lands here.
            print(f"UserManager register failed, user name {user_name} already exists. {e}")
        except sqlite3.Error as e:
            print(f"UserManager register exception: {e}")
        finally:
            conn.close()
        return retval

    def update(self, user, full_name, email, password, is_admin):
        print(f"UserManager update_user (user_name: {user.user_name if user else None})")
        retval = False
        conn = self.db.get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                if password is None:
                    # Keep the existing password hash when the user leaves password blank.
                    cursor.execute("""UPDATE users SET full_name = ?, email = ?, is_admin = ?
                                    WHERE id = ?""", (full_name, email, 1 if is_admin else 0,
                                                       user.id))
                else:
                    pwd_hash, salt = self._hash_password(password)
                    cursor.execute("""UPDATE users SET full_name = ?, email = ?, password_hash = ?,
                                salt = ?, is_admin = ? WHERE id = ?""",
                                (full_name, email, pwd_hash, salt, 1 if is_admin else 0, user.id))
                if cursor.rowcount == 0:
                    print(f"UserManager update_user failed: User ID {user.id} not found.")
                else:
                    print(f"""UserManager update_user succeeded: (user_id: {user.id},
                           user_name: {user.user_name})""")
                    retval = True
        except sqlite3.Error as e:
            print(f"UserManager update_user exception: {e}")
        finally:
            conn.close()
        return retval

    def _build_user(self, row):
        uid, uname, full_name, email, is_admin, inactive = row
        return User(uid, uname, full_name, email, is_admin, not bool(inactive))

    def login(self, user_name, password):
        print(f"UserManager login (user_name: {user_name})")
        user = None
        conn = self.db.get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT id, user_name, full_name, email, password_hash, salt,
                                is_admin FROM users WHERE user_name = ? AND inactive = 0""",
                               (user_name,))
                row = cursor.fetchone()
                if row:
                    uid, uname, full_name, email, stored_hash, salt, is_admin = row
                    # Hash the supplied password with the stored salt and compare bytes.
                    check_hash, _ = self._hash_password(password, salt)
                    if check_hash == stored_hash:
                        # Return an instance of the User class
                        user = User(uid, uname, full_name, email, is_admin)
                        print(f"UserManager login succeeded (user_name: {user_name})")
                    else:
                        print(f"UserManager login password error (user_name: {user_name})")
                else:
                    print(f"UserManager login user_name error (user_name: {user_name})")
        except sqlite3.Error as e:
            print(f"UserManager login exception: {e}")
        finally:
            conn.close()
        return user

    def filter(self, **filters):
        print("UserManager filter")
        users = []
        if not filters:
            # Get all users
            where_clause = ""
            values = []
        else:
            numeric_columns = {"id", "is_admin", "inactive"}
            where_clause, values = self._generate_where_clause(filters, numeric_columns)
        sql = f"""SELECT id, user_name, full_name, email, is_admin, inactive FROM users
          {where_clause}"""
        conn = self.db.get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                rows = cursor.execute(sql, values).fetchall()
                if len(rows) > 0:
                    print("UserManager filter_users succeeded")
                else:
                    print("UserManager filter_users get no users")
                for row in rows:
                    users.append(self._build_user(row))
        except sqlite3.Error as e:
            print(f"UserManager filter_users exception: {e}")
        finally:
            conn.close()
        return users

    def activate(self, user, enable):
        print(f"""UserManager activate (user_name: {user.user_name if user else None},
               enable: {enable})""")
        retval = False
        conn = self.db.get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                # Users are soft-deleted by flipping inactive instead of removing rows.
                cursor.execute("UPDATE users SET inactive = ? WHERE id = ?",
                                (0 if enable else 1, user.id,))
                if cursor.rowcount == 0:
                    print(f"UserManager activate failed: User ID {user.id} not found.")
                else:
                    print(f"""UserManager activate succeeded: (user_id: {user.id}, user_name:
                           {user.user_name})""")
                    retval = True
        except sqlite3.Error as e:
            print(f"UserManager activate exception: {e}")
        finally:
            conn.close()
        return retval
