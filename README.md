### Class Blender

####  __init__
```
def __init__(self, bottle_text, cap_color, size=20):
        """
        Blender constructor, executes every time a new Blender object is
        created

        @param self - points to the created object - YOU DO NOT PASS THIS IN
        @param bottle_text - string - the text printed on the side of the
                                    bottle
        @param cap_color - string - the color of the cap
        """
```

#### fill
```
def fill(self):
        """
        Fills the blender bottle, setting the liquid_contents to equal
        the size
        """
```

#### pour
```
def pour(self, amount):
        """
        Pours the given amount from the bottle
        @param amount - int - decrement self.liquid_contents by amount
        """
```

* Create bottles using syntax variable_name = Blender(bottle_text, cap_color)
    * Example: bottle_one = Blender("Reg Blender Bottle (TM) - Version 1", "Blue")

* Fill the bottles with water using the fill method
    * Example: bottle_one.fill()

* Pour the water out of the bottles using the pour metho
    * Example: bottle_one.pour()
