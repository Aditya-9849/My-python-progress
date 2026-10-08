# this is a simple slot machine game
import random
balance:float = 1000
symbols = ['🍒','🍋','🍉','🔔','⭐']

def spin_row():
    global symbols
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(*row, sep="   ")
    print()

def pay_out(row, bets):
    global balance
    if row[0] == row[1] == row[2]:
        print("JACKPOT   JACKPOT    JACKPOT")
        bets *= 50
        print(f"You won ${bets:.2f}")
        balance += bets
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("You won $5.00")
        balance += 5
    else:
        print("You lost !")

def main():
    global balance
    global symbols
    print()
    print("Welcome to the Juaa machine ")
    print("Juaa khelna galat baat, fir bhi khel lo thoda sa...")
    print("Symbols are:-",*symbols)

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")
        print()
        bet = input("Enter your bet amount: $")
  
        if not bet.isdigit():
            print("Please enter a digit as bet")
            continue
        bets = float(bet)
        if bets <= 0:
            print("Bet must be more than $1")
            continue
        balance -= bets
        row = spin_row()
        print("Spinning....")
        print_row(row)
        payout = pay_out(row, bets)

if __name__ == "__main__":
    main()