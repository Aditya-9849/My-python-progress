# super() = function used in a child class to call methods from a parent class (superclass)
#  allows you to extend the functionality of the inherited method
#  allows you to avoid using the base class name explicitly

# AGAR MULTIPLE ARRIBUTES SAME SAME HAI TO USKO EK ALAG FUNCTION KAR DO
# TAAKI BAAR BAAR CHANGE NA KARNA PADEGA HAR JAGAH, ONLY ONCE
# AND USE SUPER TO CALL THE FUNCTION

'''Why you need it-
When a class inherits from another class, it doesn't automatically run the parent's __init__. 
If you define your own __init__ in the child class, it overrides the parent's entirely, 
unless you explicitly call the parent's version using super().'''

class Shapes:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shapes):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)  # aise call krte h super ko
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"Area of the Circle is {3.14 * self.radius * self.radius:.2f} cm^2")
# agar same methods hoga parent aur child me to child ko preferance milega
# agar parent ka print krna hai to use super
class Square(Shapes):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"Area of the Square is {self.side * self.side} cm^2")

class Triangle(Shapes):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.base = base
        self.height = height

    def describe(self):
        super().describe()
        print(f"Area of the Triangle is {1/2 * self.base * self.height} cm^2")

circle = Circle(color="Red",filled=False,radius=6)
square = Square(color="Orange",filled=False,side=3)
triangle = Triangle(color="Cyan",filled=True,base=4, height=5)
# print(circle.color)
# print(circle.filled)
# print(circle.radius)
# print(square.side)
circle.describe()
print()
square.describe()
print()
triangle.describe()