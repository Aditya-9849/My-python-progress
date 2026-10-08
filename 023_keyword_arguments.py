'''keyword arguments = a way to pass arguments to a function by 
                     explicitly stating which parameter the value is for'''

#                           OR

# an argument preceded by an identifier, helps in readability of the code,
#and allows us to skip arguments or place them out of order

def hello(greeting, title, firstname, lastname):
    print(f"{greeting} {title} {firstname} {lastname}")

hello("Hello", "Mr", "Aditya", "Kumar")
'''this can give wrong results when not placed in order, so:'''
hello("Hii",title="Mrs", lastname="WTF", firstname="Kyaa")
'''this above line is called keyword argument'''

# REMEMBER :- positional argument pehle hoga keyword argument ke

for x in range(1,11):
    print(x, end=" ")
    '''here, end=" " is also a keyword argument in print statement'''
    
# there is also a keyword argument called separate(sep="")
print("1","2","3","4","5","6","7", sep="-")