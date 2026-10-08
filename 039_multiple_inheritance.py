# multiple inheritance = inherit from more than one parent class
#                       C(A,B)

# multi-level inheritance = inherit from a parent class, 
#                           which itself inherits from another parent class
#                           C(B) <- B(A) <- A
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

Hawk = hawk("Baldy")
Fish = fish("Nemo")
Rabbit = rabbit("Thumper")

Hawk.hunt()
Hawk.eat()
Fish.hunt()
Rabbit.flee()
Rabbit.sleep()