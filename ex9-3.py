class User:
    """A attempt to make a profile of user."""
    def __init__(self, first_name, last_name, users_age, users_location):
        """Initiating attributes for the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.users_age = users_age
        self.users_location = users_location

    def describe_user(self):
        """A method to describe user's info."""
        print(f"\nUser's name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"{self.first_name.title()}'s age is {self.users_age}.")
        print(f"{self.first_name.title()} live in {self.users_location.title()}.")


    def greet_user(self):
        """A method to greet user."""
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}.")


user_profile = User('priyanshu', 'yadav', 20, 'behror')
user2_profile = User('dedha', 'yadav', 20, 'jaipur')

print("\nHere are the details of first user:")
print(f"\tName: {user_profile.first_name.title()} {user_profile.last_name.title()}")
print(f"\tAge: {user_profile.users_age}")
print(f"\tLocation: {user_profile.users_location.title()}")

user_profile.describe_user()
user_profile.greet_user()

print("\nHere are the details of second user:")
print(f"\tName: {user2_profile.first_name.title()} {user2_profile.last_name.title()}")
print(f"\tAge: {user2_profile.users_age}")
print(f"\tLocation: {user2_profile.users_location.title()}")

user2_profile.describe_user()
user2_profile.greet_user()