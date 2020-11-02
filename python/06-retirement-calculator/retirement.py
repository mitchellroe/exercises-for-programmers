#!/usr/bin/env python3
"""
Foo
"""

from datetime import datetime


def get_int(prompt="Please enter an integer.", error_prompt="Please provide a valid integer."):
    """Prompt the user and return the value when they provide an integer."""
    retval = None
    while not isinstance(retval, int):
        try:
            retval = int(input(prompt))
        except ValueError:
            print(error_prompt)
    return retval


def get_years_to_retirement():
    """Return a positive integer"""
    error_prompt = "Please provide a valid age."
    current_age = get_int("What is your current age? ", error_prompt)
    retirement_age = get_int("At what age would you like to retire? ", error_prompt)
    years_to_retirement = retirement_age - current_age
    if years_to_retirement <= 0:
        print("You're too late! You should have already retired!")
    return years_to_retirement


def main():
    """bar"""
    years_to_retirement = -1
    while years_to_retirement <= 0:
        years_to_retirement = get_years_to_retirement()

    print("You have " + str(years_to_retirement) +
          " years left until you can retire.")

    current_year = datetime.today().year
    retirement_year = current_year + years_to_retirement
    print("It's " + str(current_year) + ", so you can retire in " + str(retirement_year))


if __name__ == '__main__':
    main()
