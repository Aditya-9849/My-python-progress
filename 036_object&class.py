# object = A "bundle" of related attributes (variables) and methods (functions) 
#        Ex. phone,cup,book,computer,car
#        You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stopped the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car_1 = Car("BMW", 2025, "Black", True)
car_2 = Car("Corvette",2024,"Yellow",True)
car_3 = Car("Dodge", 2026, "Black", False)

car_1.drive()
car_1.stop()
car_1.describe()
car_2.drive()
car_2.stop()
car_2.describe()
car_3.drive()
car_3.stop()
car_3.describe()