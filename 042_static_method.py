# static method = A method that belongs to a class rather than any object(instance) from that class.
#                   Usually used for general utility functions.

# Instance method = Best for operations on instances of the class(objects)
# Static method = Best for utility functions that don't require access to the class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):      #self is the instance of the class
        return f"{self.name} = {self.position}"
    
    # now we create a static method
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions  #Returns True or False

employee1 = Employee("Eugene","Manager")
employee2 = Employee("Spongebob","Cook")

print(employee1.get_info())
print(Employee.is_valid_position("Manager")) #True
print(Employee.is_valid_position("CEO")) #False