from admins import admin_login, admin_logout

def main():
    admin_login("Mohammad")
    admin_logout("Mohammad")
    admin_login("Alice")
    admin_logout("Alice")

if __name__ == "__main__":
    main()
