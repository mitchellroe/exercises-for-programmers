#!/usr/bin/env python3
"""
Ask the user for their name and print a greeting.
"""


def main():
    """
    Ask the user for their name and print a greeting.
    """
    name = input("What is your name? ")
    output = "Hello, " + name + ", nice to meet you."
    print(output)


if __name__ == '__main__':
    main()
