# inheritance = allow a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class child(parent)

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(animal):
    def speak(self):
        print("WOOF")

class cat(animal):
    pass

class mouse(animal):
    pass

Dog = dog("Scooby")
Cat = cat("Garfield")
Mouse = mouse("Mickey")

Dog.eat()
Dog.speak()