# columns code
# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")


# def main():
#     print_column(3)


# function option 1 using for
# def print_column(height):
#     for _ in range(height):
#         print("#")


# function option 2 using inline
# def print_column(height):
#     print("#\n" * height, end="")


# main()


# row code
# def main():
#     print_row(4)


# def print_row(width):
#     print("?" * width)


# main()


# square code
def main():
    print_square(3)


def print_row(width):
    print("[]" * width)


def print_square(size):
    # option 1
    # for each row in square
    # for i in range(size):
    #     # for each brick in row
    #     for j in range(size):
    #         # print brick
    #         print("[]", end="")
    #     # creates new row
    #     print()

    # option 2
    # for _ in range(size):
    #     print("[]" * size)

    # option 3
    for i in range(size):
        print_row(size)


main()
