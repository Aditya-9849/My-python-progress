#      Membership operators = used to test whether a value or variable is found in a sequence
#                            i.e. list, string, tuple, set or dictionary
#                            1. in
#                            2. not in

word = "apple"

letter = input("Guess a letter in the secret word: ")
if letter not in word:
    print(f"'{letter}' was not in the secret word !")
else:
    print(f"True, '{letter}' is in the secret word !!")


# lets say we have to check if an e-mail is valid

email = input("Please enter your e-mail: ")
if "@" and ".com" in email:
    print(f"Your e-mail - {email}, is valid")
else:
    print("This is not a valid email !")