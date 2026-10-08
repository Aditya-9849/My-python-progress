# if __name__ == __main__:  (this script can be imported or run as a standalone script)
#                           functions and classes in this script can be reused
#                           without the main block being executed

''' good practice as :- code is modular,
                        helps readability,
                        leaves no global variables,
                        avoid intented execution of code'''
def main():
    print("This is the main function.")

if __name__ == "__main__":
    main()