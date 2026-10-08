import time

# many times we have 0 as default to start
# but its a rule to have default value after a not default value so, 

def count(end, start=0):
    for number in range(start, end+1):
        print(number)
        time.sleep(1)
    print("DONE...")

# start = int(input("Enter your highest number to count: "))
count(30,25)