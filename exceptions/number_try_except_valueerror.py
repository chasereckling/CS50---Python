# w/o function
# try:
#     # passing the return value of input as the argument to int function and x will store the value
#     x = int(input("what's x? "))
#     # use f 'format string' to interpolate the value of the x variable. otherwise python will just print {x} literally
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# w/ function
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
