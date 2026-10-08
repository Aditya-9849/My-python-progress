# here are some 1-D lists
veggies = ["brinjal","potato","cauliflower","bottlegourd"]
meats =   ["mutton","fish","chicken","turkey"]
others =  ["maize","bajra","jwar","arhar"]

# converting them to 2-D

eatables = [veggies,meats,others]

# now printing anything by imagining this 2-D list as a excel spreadsheet 

# print(eatables[1][0])

'''this thing works with tuples, lists, sets'''

for items in eatables:
    for collections in items:
        print(collections, end=" ")
    print()