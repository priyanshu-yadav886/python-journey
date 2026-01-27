class Restaurant:
    """An attempt to make a restaurant's cuisine."""
    def __init__(self, restaurant_name, cisine_type):
        """Initiating the attributes"""
        self.name = restaurant_name
        self.type = cisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method to describe the restaurant."""
        print(f"This restaurant have red paint on walls.")
        print(f"This restaurant have 10 seats")

    def open_restaurant(self):
        """A method to tell if restaurant."""
        print("This reataurant is open.")


    def served_people(self):
        """TA method to tell the number of people served."""
        print(f"{self.number_served} people have served.")

    def set_number_served(self, peoples):
        """Set the number served to the given value."""
        self.number_served = peoples


    def increment_number_served(self, persons):
        """Increasing the value of served numbers."""
        self.number_served += persons


resta_info = Restaurant('coco cafe pink', 'pure veg')

print(f"i went to a restaurant name {resta_info.name.title()} yesturday.")
print(f"it's cuisine's were {resta_info.type.title()}")
resta_info.describe_restaurant()
resta_info.open_restaurant()
resta_info.served_people()
resta_info.number_served = 23
resta_info.served_people()
resta_info.set_number_served(18)
resta_info.served_people()
resta_info.increment_number_served(180)
resta_info.served_people()