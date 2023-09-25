# while loop
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# for loop
# for _ in range(3):
#     print("meow")

# inline
# print("meow\n" * 3, end="")

# while True:
#     n = int(input("what's n? "))
#     if n < 0:
#         continue
#     else:
#         break

# while True:
#     n = int(input("what's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    # need to use return to hand back a value from the function
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
