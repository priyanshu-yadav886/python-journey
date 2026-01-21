class User:
    """Class for representing details of a user."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        """A method to describe information about user."""
        print(f"User's full name is {self.first_name.title()} {self.last_name.title()}")
        print(f"{self.first_name.title()} is {self.age} years old.")

    def greet_user(self):
        """A method to greet user."""
        print(f"Hello {self.first_name.title()}!")



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


admin = Admin("prince", "yadav", 20)

admin.describe_user()
admin.privilegs.show_privilegs()