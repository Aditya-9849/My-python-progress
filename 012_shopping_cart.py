# this program takes names and prices of items user wants to buy and display the total

food_items = []
food_prices = []
total = 0

while True:
    food = input("Enter the food you want(q to quit): ")
    if food.lower() == "q":
        break
    else:
        prices = float(input(f"Enter the price of {food} :$ "))
        food_prices.append(prices)
        food_items.append(food)

print("----YOUR SHOPPING CART----")
for x in food_items:
    print(x, end=", ")

for y in food_prices:
    total += y
print()
print(f" Yout total price is ${total}")