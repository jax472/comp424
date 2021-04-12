"""
Module Docstring - For oop_example.py
Author: Jon
Date: 12 Apr 21

Week 11 example to help clarify objective oriented programming (OOP)
using Blender Bottle
"""

class Blender:
    """
    Class representing a blender bottle for liquids

    Properties:
    - bottle_text
    - cap_color
    - size
    - liquid_contents (liquid contents in ounces)

    Methods:
    - fill
    - pour
    """

    def __init__(self, bottle_text, cap_color, size=20):
        """
        Blender constructor, executes every time a new Blender object is
        created

        @param self - points to the created object - YOU DO NOT PASS THIS IN
        @param bottle_text - string - the text printed on the side of the
                                    bottle
        @param cap_color - string - the color of the cap
        """
        self.bottle_text = bottle_text
        self.cap_color = cap_color
        self.size = size
        self.liquid_contents = 0

    def fill(self):
        """
        Fills the blender bottle, setting the liquid_contents to equal
        the size
        """
        self.liquid_contents = self.size

    def pour(self, amount):
        """
        Pours the given amount from the bottle
        @param amount - int - decrement self.liquid_contents by amount
        """
        if amount <= self.liquid_contents:
            self.liquid_contents = self.liquid_contents - amount
        else:
            self.liquid_contents = 0


bottle_one = Blender("Reg Blender Bottle (TM) - Version 1", "Blue")
super_bottle = Blender("Super Blender Bottle (TM) - Version 2", "Green")
mini_bottle = Blender("Mini Blender Bottle (TM) - Version 3", "Red", 14)

# print(super_bottle.liquid_contents)
# print(mini_bottle.liquid_contents)

super_bottle.fill()
print(super_bottle.liquid_contents)
# mini_bottle.fill()

# print(bottle_one.liquid_contents)
# print(super_bottle.liquid_contents)
# print(mini_bottle.liquid_contents)

super_bottle.pour(25)
print(super_bottle.liquid_contents)
