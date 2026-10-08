'''nested loops = looops within loops'''
for x in range(3):
    for y in range(1, 11):
        print(y, end="")
    print("")


'''creating a rectangle with this concept'''

# the, end="" makes the print(something) to continue in the same line
# the print() makes it to change the line by printing empty string

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter the symbol you want to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()