# this program will encrypt a message and also decrypt it using a simple substitution cipher
import random
import string

chars = string.punctuation+ " " + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

plain = input("Enter the secret message:")
encrypted = ""

# encryption

for text in plain:
    index = chars.index(text)
    encrypted += key[index]
print(f'Encrypted message:{encrypted}')
print()

#decryption

original = ""
yes_no = input("Do you want to decrypt the message (Y/N)? :").lower()
if not yes_no == "y":
    exit
else:
    decrypt = input("Please enter the encrypted message:")
    for txt in decrypt:
        indx = key.index(txt)
        original += chars[indx]
    print(f'Decrypted message:{original}')
print()
print("Thanks for using the program, have a nice day!")