# stone paper scissors game
import random

options = ("stone", "paper", "scissors")

print("Welcome to 'stone', 'paper', 'scissors' game ")

while True:
    computer = random.choice(options)
    answer = input("Enter your choice: ").lower()
    if answer not in options:
        print("Please type a valid option ")
        answer = input("Enter your choice: ").lower()
    if answer in options:
        print(f"Your choice: {answer}")
        print(f"Computer's choice: {computer}")
        if computer == answer:
            print("Its a tie...")
        elif computer == "stone" and answer == "paper":
            print("You won this round...")
        elif computer == "paper" and answer == "scissors":
            print("You won this round...")
        elif computer == "scissors" and answer == "stone":
            print("You won this round...")
        elif computer == "scissors" and answer == "paper":
            print("You lose this round...")
        elif computer == "stone" and answer == "scissors":
            print("You lose this round...")
        elif computer == "paper" and answer == "stone":
            print("You lose this round...")
    print()