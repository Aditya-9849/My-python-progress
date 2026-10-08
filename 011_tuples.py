'''tuples are ordered and unchangeable and faster, duplicates are OK'''

fruits = ("apple","coconut","coconut","banana","orange","pineapple")

# "pineapple" in fruits
# print(len(fruits))

'''in tuples, we have only 2 main functions'''
# print(fruits.index("apple"))
# fruits.count("coconut")

'''they are iterable, by for loops'''
for fruit in fruits:
    print(fruit)