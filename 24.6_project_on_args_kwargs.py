'''this project, we will print a shipping label'''

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=", ")

shipping_label("Dr","Jhatka",
               street="Dholakpur",
               state="Bhotakpur",
               Pin="00123")