class Restaurant:
    """An attempt to make a restaurant's cuisine."""
    def __init__(self, restaurant_name, cisine_type):
        """Initiating the attributes"""
        self.name = restaurant_name
        self.type = cisine_type

    def describe_restaurant(self):
        """A method to describe the restaurant."""
        print(f"This restaurant have red paint on walls.")
        print(f"This restaurant have 10 seats")

    def open_restaurant(self):
        """A method to tell if restaurant."""
        print("This reataurant is open.")

resta_info = Restaurant('coco cafe pink', 'pure veg')

print(f"i went to a restaurant name {resta_info.name.title()} yesturday.")
print(f"it's cuisine's were {resta_info.type.title()}")
resta_info.describe_restaurant()
resta_info.open_restaurant()