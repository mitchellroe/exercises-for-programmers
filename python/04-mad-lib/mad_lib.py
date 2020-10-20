#!/usr/bin/env python3
"""
Play a Mad Lib
"""

def main():
    """
    Play a Mad Lib
    """
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj  = input("Enter an adjective: ")
    adv  = input("Enter an adverb: ")
    print("Do you " + verb + " your " + adj + " " + noun + " " + adv + "? That's hilarious!")

if __name__ == '__main__':
    main()
