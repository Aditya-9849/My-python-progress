# this is program made by using dictionaries

menu = {"samosa":10,
        "golgappa":2,
        "chat":20,
        "gulabjamun":20,
        "sonpapdi":70}

total = 0
cart = []
check = menu.keys()
print(check)

print("-------MENU-----------")
for key, value in menu.items():
    print(f"{key:13} $ {value:.2f}")
print("-----------------------")

while True:
    food = input("Enter the item you want(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
         cart.append(food)   

for food in cart:
    total += menu.get(food)
    # this line uses get function to get the value of keys from food and adds to total            

print("----------Your order--------")
for saman in cart:
    print(saman)
print("----------Your total---------")
print(f"$ {total:.2f}")