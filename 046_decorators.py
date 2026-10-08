# decorator = a function that extends the behaviour of another function without
#               modifying the base function
#               pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("Adding sprinkles 🍬")
        func(*args,**kwargs)
    return wrapper   #ye return function "add_sprinkles" ka hai

# add_sprinkles run karega wrapper ko jo print statement + function ko call karega 
# and the return kr diya jayega by "add_sprinkles" function

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("Adding fudge 🍫")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge  # we can apply more than one decorators in a function
def get_icecream(flavor):
    print(f"Here is your {flavor} ice-cream 🍧")
get_icecream(flavor = "vanilla")