'''default arguments = a default value for certain parameters
                        Default is used when that argument is ommitted
                        make your functions more flexible and reduce the no of arguments passed in
                        1- positional argument(project 021)
                        2- default arguments
                        3- keyword
                        4- arbitrary'''

# create a function to calculate net price
def net_price(list_price, discount=0, tax=0.18):
    # the =0 means we set default discount to 0,
    # if anyone doesnt enters discount it will not show error
    # same thing with tax, but if someone enters it, it will forget default value
    return list_price * (1-discount) * (1+tax)

print(net_price(16000))