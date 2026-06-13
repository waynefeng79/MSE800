class User:
    """User object with role Admin or Customer.

    Provides a simple profile representation with support for mutable profile
    fields, active status, and admin role assignment.
    """

    def __init__(self, user_id, user_name, full_name, email, is_admin, active = True):
        """Initialize a User with identity, profile details, role, and status.

        Args:
            user_id: Unique identifier for the user.
            user_name: Immutable login or account name.
            full_name: Display name for the user.
            email: Contact email address.
            is_admin: Whether the user has administrative privileges.
            active: Whether the account is currently active.
        """
        # User names are immutable after creation; profile details can be updated later.
        self._user_id = user_id
        self._user_name = user_name
        self._full_name = full_name
        self._email = email
        self._is_admin = bool(is_admin)
        self._active = bool(active)

    def __str__(self):
        """Return a readable string representation of the user."""
        role = "Admin" if self.admin else "Customer"
        return f"[{role}] {self.full_name} (user_name: {self.user_name})"

    @property
    def id(self):
        """Get the user's unique identifier."""
        return self._user_id

    @property
    def user_name(self):
        """Get the immutable username."""
        return self._user_name

    @property
    def full_name(self):
        """Get the user's display name."""
        return self._full_name

    @property
    def email(self):
        """Get the user's email address."""
        return self._email

    @property
    def active(self):
        """Return whether the user account is active."""
        return self._active

    @property
    def admin(self):
        """Return whether the user has administrative privileges."""
        return self._is_admin

    @full_name.setter
    def full_name(self, full_name):
        """Update the user's display name."""
        self._full_name = full_name

    @email.setter
    def email(self, email):
        """Update the user's email address."""
        self._email = email

    @active.setter
    def active(self, active):
        """Set the account's active status."""
        self._active = bool(active)

    @admin.setter
    def admin(self, is_admin):
        """Grant or revoke administrative privileges."""
        self._is_admin = is_admin
