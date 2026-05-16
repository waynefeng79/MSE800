# decorateor usage in the project
This project shows a simple decorator example which includes a wrapper for admin check.

## structure
The application includes three parts:
- main: application entry
- admins: functions only allowed by admin role, decorated by decorator admin_check
- decorator: wrapper function admin_check to check admin role before calling the decorated function

## decorator
The decorator admin_check checks the first parameter of the decorated function, which must be a user name. Only when the user name is with admin role, the decorated function will be called.
