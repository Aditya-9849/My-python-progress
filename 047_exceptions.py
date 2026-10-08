# exceptions = an event that interrupts the flow of a program, like:-
#               ZeroDivisionError, TypeError, ValueError
#               1. Try - any code that can cause error
#               2. Except "error" - if this "error" is found, run some code 
#               3. Finally - it always executes

try:
    division = int(input("Enter a number here: "))
    num = 1/division
    print(num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Only numbers !")
except Exception:
    print("Something went wrong")
finally:
    print("Okay bye")