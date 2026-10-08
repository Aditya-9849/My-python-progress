# let's create a compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than equal to zero")

while rate <= 0:
    rate = float(input("Enter your interest rate: "))
    if rate <= 0:
        print("Rate cannot be less than equal to zero")

while time <= 0:
    time = int(input("Enter your time: "))
    if time <= 0:
        print("Time cannot be less than equal to zero")

total = principle * pow((1 + rate/100), time)

print(f"Your total amount in {time} years at rate {rate}% will be: {total:.2f}")