from Hello import User

class Privileges:
    """A simple attempt to madel the privileges of admin"""

    def __init__(self):
        """initializing the privileges."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify settings"
        ]

    def show_privilegs(self):
        """A method to print the admin's privilegs."""
        print("\nAdmin's privilegs:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

class Admin(User):
    """A class for admin."""
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilegs = Privileges()