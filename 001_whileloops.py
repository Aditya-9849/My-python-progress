# '''while loop = excetutes some code WHILE some condition remains true  '''
name = input("Please enter your name: ")
while name == "":
    print("You did not enter your name !")
    name = input("Please enter your name: ")

print(f"Hello {name}!")

# another example of while loops
num = int(input("Choose a num btw 1-10: "))

while 0 > num or num> 10:
    print("Number is not btw given range")
    num = int(input("Choose a num btw 1-10: "))
print(f"You choose {num}")