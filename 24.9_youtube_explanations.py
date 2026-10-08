'''to understand better the concept of *args and **kwargs, lets order a pizza'''

def order_pizza(size, *toppings, **details):
    print(f"User ordered a pizza of {size} size")
    for topping in toppings:
        print(f"-- {topping}")
    for key, value in details.items():
        print(f"{key} - {value}")
    
order_pizza("large", "papporoni","cheese","olives", state="Bihar", city="Bettiah", pincode="845438")

'''so, here first argument, large, is used by size
   * the arg uses all the positional arguments to convert to a tuple, except for 
    the keyword arguments which are used by **kwargs to convert them to dictionary'''