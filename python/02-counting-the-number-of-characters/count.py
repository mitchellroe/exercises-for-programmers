#!/usr/bin/env python3
"""
Prompt for an input string and print the number of characters
"""


def main():
    """
    Prompt for an input string and print the number of characters
    """
    my_string = input("What is the input string? ")
    num_of_chars = len(my_string)
    print(my_string + " has " + str(num_of_chars) + " characters.")


if __name__ == '__main__':
    main()
