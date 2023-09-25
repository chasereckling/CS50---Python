def main():
    question_response = input(str("Do you want to know your age or your birth year? "))

    if question_response == "age":
        year_response = int(input("What is your birth year? "))
        find_age(year_response)
    elif question_response == "birth year":
        age_response = int(input("How old are you? "))
        find_birthYear(age_response)
    else:
        print("Invalid response.")


# Find birth year
def find_birthYear(age):
    birth_year = 2023 - age
    print("Your birth year is", birth_year)


# Find age based on birth year
def find_age(year):
    age = 2023 - year
    print("Your age is", age)


main()
