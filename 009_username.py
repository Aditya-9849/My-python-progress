'''validate user input exercise 
rule 1 - not more than 12 characters
rule 2 - must not contain spaces
rule 3 - must not contain digits'''

username = input("Please enter your desired username:")

user_length = len(username)
space_search = username.find(" ")
digits_check = username.isalpha()

if space_search > 0:
    print("Username can't contain spaces")
if user_length > 12:
    print("Your username exceeds word limit !")
if digits_check == False:
    print("Username cannot contain digits !")

if space_search == -1 and user_length <= 12 and digits_check == True:
    print(f"Welcome {username} !!")