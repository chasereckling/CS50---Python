# Input
# age = int(input("How old are you? "))

# Operations
# birth_year = 2023 - age

# Output
# print("Your birth year is", birth_year)


def main():
    age = int(input("How old are you? "))
    birth_year_function(age)


def birth_year_function(number):
    birth_year = 2023 - number
    print("Your birth year is", birth_year)


# This way...
# birth_year_function(int(input("How old are you? ")))
# ... is the same as this way
main()
