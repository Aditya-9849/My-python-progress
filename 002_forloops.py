# for loops = execute a block of code a fixed number of times.
'''you can iterate over a range, string, sqeuence, etc'''

'''over a range'''
for x in range(1, 11, 2):
    print(x)

'''over a string'''
credit_card = "1234-2345-3456-4567"
for y in credit_card:
    print(y)

'''skipping a number'''
for a in range(1,21):
    if a == 3:
        continue
    else:
        print(a)