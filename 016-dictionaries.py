#  collection of {key:value} pairs. ordered and changeable. no duplicates

capitals = {"India":"New delhi",
"USA":"Washington DC",
"China":"Beijing",
"Russia":"Moscow"}

print(capitals.get("India"))

capitals.update({"Germany":"Berlin"}) 
''' capitals.update() will add a new key and value if it is not in the dictionary
and it will update that if it already exists'''

# capitals.pop("India")
# this above line will eliminate india and its value from the dictionary
'''if i want to pop the last added key and its value, i will use the code, capitals.popitem()  '''

# capitals.clear()   this will clear the whole dictionary

# if i want to get all the keys from a dictionary i will use:
keys = capitals.keys()
# we can use for loop here
for key in keys:
    print(key)

# # there is this method for values also
# values = capitals.values()
# # using for loop here too:
# for value in values:
#     print(value)

print()

# here is the most complicated one
items = capitals.items()
# print(items)
'''this above returns the dictionary in the format of 2-D list, like:- [(),(),()]
we can use this to many things'''
for key, value in items:
    print(f"{key} : {value}")