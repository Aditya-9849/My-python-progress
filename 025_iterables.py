'''iterables = An object/collection that can return its element one at a time,
                allowing it to be iterated over in a loop'''

numbers = [1,2,3,4,5]

for num in reversed(numbers):
    print(num, end=" ")
print()
# iteration can also be done in tuples

fruits = {"apple","banana","orange"}
for fruit in fruits:
    print(fruit)
'''reversing is not done in sets'''

# strings
name = "Aditya sharma"
for ch in name:
    print(ch, end=" ")
print()
 
# dictionary
my_dictionary = {"A":1,
                 "B":2,
                 "C":3}
for value in my_dictionary.values():
    print(value)
''' .values() - for values
    .keys()    - for keys
    .items()    - for keys and values'''