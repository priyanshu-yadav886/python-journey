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