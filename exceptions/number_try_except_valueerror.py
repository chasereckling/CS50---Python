try:
    # passing the return value of input as the argument to int function and x will store the value
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
    # use f 'format string' to interpolate the value of the x variable. otherwise python will just print {x} literally
    print(f"x is {x}")
