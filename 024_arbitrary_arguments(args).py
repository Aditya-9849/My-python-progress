#   *args     = allow you to pass multiple non-key arguments
#   **kwargs  = allow you to pass multiple keyword arguments
#       *  is unpacking operator

'''remember - TUPLE IF ARGS, DICTIONARY IF KWARGS'''

def subtract(num1,num2):
    return num1+num2

subtract(5,2)
# if we pass in 3 arguments, this will give error
# so we modify it with args

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(5,6))
# its not necessary to name it args
# we can also name it what we want, sign matters
def multiply(*digit):
    tootal = 0
    for deegit in digit:
        tootal += deegit
    return tootal

print(multiply(1,2,3))

def name(*args):
    for arg in args:
        print(arg, end=" ")

name("Aditya", "Bin", "Ladin")