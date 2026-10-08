'''4 types of functions:1- positional argument(project 021)
                        2- default arguments(project 022)
                        3- keyword(project 023)
                        4- arbitrary(project 024)'''

# positional arguments 

# functions are a block of reusabe code
# adding a set of () calls the function

'''lets sing happy bday 3 times'''
'''position of the parameters matters, naam ke jagah age nhi kr skte and vice versa'''
def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")
    print("Happy birthday to you")
    print()

happy_birthday("aditya", 20)
happy_birthday("jerry", 30)
happy_birthday("Tony", 40)

# creating an invoice
def invoice(username,amount,duedate):
    print(f"Hello {username}!")
    print(f"Your bill of amount ${amount} is due {duedate}")

invoice("Aditya", 100, "06/05")

# ----------return function----------
# return = statement used to end a function and send result back to the caller

def add(x ,y):
    z = x + y
    return z

def subtract(x ,y):
    z = x - y
    return z

def multiply(x ,y):
    z = x * y
    return z

def divide(x ,y):
    z = x / y
    return z

print(add(5, 8))
print(subtract(8,5))
print(multiply(8,5))
print(divide(20,4))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("aditya","kumar")
print(full_name)