class User:
    """Models typical user information."""

    def __init__(self, username, email):
        """Initialize attributes to describe a user."""
        self.username = username
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        """Greet the user in the console."""
        return f"\nHello, {self.username}!"

    def describe_user(self):
        """Summarize user information."""
        return(f"""
        Username: {self.username}
        Email: {self.email}
        Login Attempts: {self.login_attempts}
        """)

    def increment_logins(self):
        self.login_attempts += 1
        return f"{self.username} Attempted {self.login_attempts} Logins"

    def reset_logins(self):
        self.login_attempts = 0
        return self.login_attempts


# Admin Class
class Admin(User):
    def __init__(self, username, email):
        """
        Initialize attributes from parent class.
        Initialize Admin specific attributes.
        """
        super().__init__(username, email)
    #    self.privileges = ['can delete post', 'can ban user', 'can edit']

   # def show_privileges(self):
    #    print(self.privileges)


admin027 = Admin('admin027', 'admin027@gmail.com')

print(admin027.describe_user())

