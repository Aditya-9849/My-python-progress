# user data
users = {"Name":"Aditya",
         "Balance":90990.14,
         "Pin":9065}

balance = users["Balance"]
password = int(input("Please enter your PIN: "))
print()
check = users["Pin"]
program_running = True

# functions
def show_balance():
    print(f"Your Balance is ${balance:.2f}")
def deposit():
    global balance # this is important, if forgot, go search
    amount = float(input("Enter the amount you want to deposit: $ "))
    if amount >= 1:
        balance += amount
        print(f"Current balance -> ${balance:.2f}")
    else:
        print("Amount must be a positive number !")
        
def withdraw():
    global balance
    amount2 = float(input("Enter the amount you want to withdraw: $ "))
    if amount2 < 0:
        print("Amount must be positive")
    elif amount2 <= balance:
        balance -= amount2
        print(f"Successfully withdrawn ${amount2:.2f}")
    elif amount2 > balance:
        print("Insufficient funds !")
    print(f"Current balance -> ${balance:.2f}")

# pin system
if password != check:
    print("Enter a correct PIN")
if password == check:
    print(f"Welcome {users['Name']}!")
    while program_running:
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print('4. Exit')

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                show_balance()
            case 2:
                deposit()
            case 3:
                withdraw()
            case _:
                program_running = False
                print("Thank you for using banking program !")
        print()