class Die:
    """A class representing a Die"""
    def __init__(self):
        """Initializing the attributes of die class."""
        self.sides = 6


    def roll_die(self):
        """A method to print numbers on die"""
        from random import randint
        return randint(1, self.sides)
        


    def change_sides(self, new_die):
        """A method to change the sides of the die."""
        self.sides = new_die



die = Die()

print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())

die.change_sides(10)

print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
