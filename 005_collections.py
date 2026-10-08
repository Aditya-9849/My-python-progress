# '''there are 4 general collections'''
# collection = single variable to store multiple values
'''list = [] ordered and changeable, duplicates-OK
set = {} unordered and immutable, add-remove-OK, no duplicates
tuple = () ordered and unchangeable, duplicates-OK, FAST
dictionary '''

fruits = ["apple", "banana", "anar", "guava"]
# print(fruits[::-1])
'''lists can be iterated by for loops'''
# print(help(fruits))
for x in fruits:
     print(f"Your fruits are {x},")

print("apple" in fruits)
fruits.append("orange")
print(fruits)

# to insert any item at specific location, use fruits.insert(0, "mango")

''' fruits.append
.reverse
.remove
.insert
.sort
.clear
.count
.index'''

# other collections on number 10 and ahead