import random
attempts = 0
lower = 1
upper = 50
number = random.randint(lower, upper)

print("Welcome to number guessing game")
print(f"Enter a number between {lower} and {upper}")
while True:
    user_ans = input("Enter your guess: ")
    if user_ans.isdigit():
        user_ans = int(user_ans)
        if user_ans > number:
            print("Try a lower number")
            print()
            attempts += 1
        if user_ans < number:
            print("Try a higher number")
            print()
            attempts += 1
        if user_ans == number:
            print("Correct guess!")
            print()
            attempts += 1
            print(f"Number was {number}, guessed at {attempts}th attempt !")
            break
    else:
        print("Please enter a valid type of guess")