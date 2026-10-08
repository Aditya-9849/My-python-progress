# --------------------- 2. DUCK TYPING ---------------------

# "IF IT LOOKS AND QUACKS LIKE A DUCK, IT MUST BE A DUCK" [WTF]
'''as long as an object resembles another, it could also be treated of that type'''

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Bhau Bhau")

class Cat(Animal):
    def speak(self):
        print("Meow")

# lets add a completely different class
class car:
    alive = False
    def speak(self): #if there is honk at the place of speak, it will not work but honk, speak same thing
        print("Beep Beep")

animals = [Dog(),Cat(),car()]
for animal in animals:
    animal.speak()
    print(f"Is it alive? {animal.alive}")