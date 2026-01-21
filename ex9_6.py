class Restaurant:
    """An attempt to make a restaurant's cuisine."""
    def __init__(self, restaurant_name, cisine_type):
        """Initiating the attributes"""
        self.name = restaurant_name
        self.type = cisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method to describe the restaurant."""
        print(f"This {self.name} have red paint on walls.")
        print(f"This {self.name} have 10 seats")

    def open_restaurant(self):
        """A method to tell if restaurant."""
        print(f"{self.name} is open.")

class IceCreamStand(Restaurant):
    """Writing a child class"""

    def __init__(self, restaurant_name, cisine_type):
        super().__init__(restaurant_name, cisine_type)
        self.flavors = []

    def show_flavors(self):
        """printing flavor's name"""
        print("\n Available ice cream name")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Cool Scoops", "Ice Cream")

ice_cream.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango"]

ice_cream.describe_restaurant()
ice_cream.show_flavors()