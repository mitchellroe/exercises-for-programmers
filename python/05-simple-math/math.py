#!/usr/bin/env python3
"""
Do some simple math.
"""

def main():
    """
    Do some simple math.
    """
    first = input("What is the first number? ")
    second = input("What is the second number? ")
    print(first + " + " + second + " = " + str(int(first) + int(second)) + "\n" +
          first + " - " + second + " = " + str(int(first) - int(second)) + "\n" +
          first + " * " + second + " = " + str(int(first) * int(second)) + "\n" +
          first + " / " + second + " = " + str(int(first) / int(second)))

if __name__ == '__main__':
    main()
