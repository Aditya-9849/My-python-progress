# Class methods = allow operation related to the class itself
#                  Take (cls) as the first parameter, which represents the class itself

# Instance methods = best for operations on objects of the class
# Static methods = best for utility functions that do not need access to class data (file no-043)
# Class methods = best for class-level data or require access to the class itself

class Student:
    count = 0
    gpa = 0
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
        Student.count += 1
        Student.gpa += GPA

    # INSTANCE METHOD   
    def get_info(self):
        return f"{self.name} - {self.GPA}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA : {cls.gpa}"
    
    @classmethod
    def avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA : {cls.gpa/cls.count:.2f}"

student1 = Student("Spongebob", 7.6)
student2 = Student("Patrick", 8.0)
student3 = Student("Sandy", 9.0)

print(Student.avg_gpa())

'''Instance method — takes self (the specific object). Works with instance data like self.name
    Class method — takes cls (the class itself), not any particular object. 
                    Works with class-level data like count.
    Static method — takes neither. Just a regular function that happens to live inside the class,
                    for organizational purposes.'''