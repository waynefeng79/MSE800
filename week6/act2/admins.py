from decorators import admin_check

@admin_check
def admin_login(username):
    print(f"admin {username} logged into the system.")

@admin_check
def admin_logout(username):
    print(f"admin {username} logged out.")
