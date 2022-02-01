#!/usr/bin/env python3
"""
Print out a quote and an author, with quotation marks around the quote.
"""


def main():
    """
    Print out a quote and an author, with quotation marks around the quote.
    """
    quote = input("What is the quote? ")
    author = input("Who said it? ")
    print(author + " says, \"" + quote + "\"")


if __name__ == '__main__':
    main()
