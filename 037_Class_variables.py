# class variables = shared among all instance of a class
#                   defined outside the constructor
#                   allows you to share data among all objects created from that class

class student:

    class_year = 2025
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Adi", 18)
student2 = student("Patrick", 35)
student3 = student("Squid", 55)
student4 = student("Sandy", 24)

print(f"My graduating class of {student.class_year} has {student.num_students} students")