# list comprehension = A concise way to create lists in python
#                       compact and easier to read than traditional loops
#                       formula - [expression for value in iterable if condition]

#           -----------------------TRICKY THINGS AHEAD------------------------

douubles = []
for y in range(1,11):
    douubles.append(y*2)
print(douubles)

# now using list comprehension formula

'''doubles = [expression for value in iterable if condition]'''
''' we have skippped condition for now'''
doubles = [x * 2 for x in range(1,11)]
print(doubles)

triples = [z*3 for z in range(1,6)]
print(triples)

squares = [a ** 2 for a in range(1,11)]
print(squares)

# with srings
fruits= ["apple","orange","banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# ##########  conditions    #####
numbers = [1,-2,3,-4,5]
positive_nums = [num for num in numbers if num>=0] # expression is required otherwise, error
print(positive_nums)

negative_nums = [num for num in numbers if num<=0]
print(negative_nums)