# @property = decorator used to define a method as a property(can be accessed like an attribute)
#              Benefit: add additional logic when reading, writing, or deleting an attribute
#              gives you getter(to read), setter(to write) and deleter(to delete) methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

# line 11 to line 17 - getter method
    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

# line 20 to line 32 - setter method
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

# line 35 to 43 - deleter method
    @height.deleter
    def height(self):
        del self._height
        print("Height is deleted")

    @width.deleter
    def width(self):
        del self._width
        print("width is deleted")

rectangle1 = Rectangle(5,7)
rectangle1.width = 4 
del rectangle1.height
del rectangle1.width
# print(rectangle1.width)
# print(rectangle1.height)