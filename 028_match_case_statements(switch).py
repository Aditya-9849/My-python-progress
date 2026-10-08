''' match case statement (switch) = an alternative to using 'elif' statements
                                    execute some code if a value matches a 'case'
                                    benefits:- cleaner and syntax in more readable'''

def which_day(din):
    if din == 1:
        return "Monday"
    elif din == 2: 
        return "Tuesday"
    elif din == 3:
        return "Wednesday"
    elif din == 4:
        return "Thursday"
    elif din == 5:
        return "Friday"
    elif din == 6:
        return "Saturday" 
    elif din == 7:
        return "Sunday"
    elif din > 7:
        return "Invalid day"

# this same can be done using match case statements
# take all if statements and enclose them into match case block, 
# where the case is going to be value we are checking for,
# and the code block is going to be the code that we want to execute if the value matches the case
def day_of_week(day):
    match day:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case 7:
            return "It is Sunday"
        case _:
            return "Invalid day"
        # we will perform case_ when there are no matching cases

print(which_day(3))
print(day_of_week(3))

# see how cool this feature is, we can also use match case statements to check for strings
def is_weekend(diwas):
    match diwas:
        case "Sunday" | "Saturday":
            return "Yes, it is a weekend"
        case _:
            return "No, it is not a weekend"
print(is_weekend("Monday"))