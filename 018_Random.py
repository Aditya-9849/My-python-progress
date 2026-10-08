import random

# print(help(random))
'''if i want to roll a dice of 6-sides then i will do this:'''
number = random.randint(1,6)
# print(number)

# we can also put variables as long as they contain numbers, like this:
lower_range = 1
upper_range = 100
number2 = random.randint(lower_range, upper_range)
# print(number2)

'''printing random.random() will give random number between 0-1'''
'''we can also play rock paper scissors'''
options = ("Rock", "Paper", "Scissors")
# print(random.choice(options))

'''we can also shuffle a deck of cards'''
cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards) 
'''remember, the shuffle method returns none'''
print(cards)