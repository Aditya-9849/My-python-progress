# polymorphism = having different 'faces' or 'forms'
#               TWO WAYS TO ACHIEVE POLYMORPHISM:
#                1.INHERITANCE = An object could be treated of the same type as parent class
#                2."DUCK TYPING" = Object must have necessary attributes/methods

# ------------------------1.  INHERITANCE   ---------------------------------

# from abc import ABC,abstractmethod

class Shape:
    # @abstractmethod  
    # i have not read decorators yet
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius**2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base*self.height)/2

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

# here pizza is considered a pizza, a circle, and a shape, 3 forms of pizza 

shapes = [Circle(4),Square(3),Triangle(6,7), Pizza("cheeze",7)]

for shape in shapes:
    print(f"Area is {shape.area()} cm^2")