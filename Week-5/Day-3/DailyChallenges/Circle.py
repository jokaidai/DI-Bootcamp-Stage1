import turtle
import math
# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# - Compute the circle’s area
# - Print the circle and get something nice
# - Be able to add two circles together
# - Be able to compare two circles to see which is bigger
# - Be able to compare two circles and see if there are equal
# - Be able to put them in a list and sort them

class Circle:
    """
    a class that emulate a circle an allow some basic actions on it
    """

    circles = []

    def __init__(self:object, radius:int, name:str) -> None:

        self.radius = int(radius)
        self.diameter = 2 * radius
        self.name = name
        Circle.circles.append(self)

    def __add__(self:object, other:object) -> None:

            self.radius += other.radius
            self.diameter = self.radius * 2
            
    
    def get_area(self:object) -> None:
        """
        compute the circle's area
        """

        pow = math.pow(self.radius, 2)

        return math.pi * pow


    def draw(self:object) -> None:
        """
        get a nice thing ;)
        """
        
        turtle.circle(self.get_area())

    def compare(self:object, other:object) -> None:
        """
        compare the 2 circles and see if its equal or bigger and print a message accordingly
        """

        if self.radius == other.radius:
            print("The 2 circles are equals .")
        elif self.radius > other.radius:
            print(f"{self.name} is biger.")
        else:
            print(f"{other.name} is biger")
    

c1 = Circle(7, "c1")
c1.draw()
print(c1.get_area())
print(c1.radius, c1.diameter)

c2 = Circle(5, "c2")
print(c2.radius, c2.diameter)

c1 + c2
print(c1.radius, c1.diameter)

c1.compare(c2)

