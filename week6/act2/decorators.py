
def is_admin(user):
    return True if user == "Mohammad" else False

def admin_check(func):
    # A decorator to check admin role.
    def wrapper(*args, **kwargs):
        result = None

        print("===================================")
        print(f"Function: {func.__name__}")
        print("Admin check started...")
        user = args[0] if len(args) > 0 else None
        if is_admin(user):
            result = func(*args, **kwargs)
            print("Activity completed.")
        else:
            print("Activity restricted by admin, function not called!")
        print("===================================\n")

        return result

    return wrapper
