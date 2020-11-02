#!/usr/bin/env python
"""foo"""

import math

CONVERSION_FACTOR = 0.09290304

def get_square_meters(square_feet):
    """foo"""
    square_meters = (square_feet * square_feet) * CONVERSION_FACTOR
    square_meters = math.sqrt(square_meters)
    return square_meters



def main():
    """Prompt for dimensions and convert them."""
    length = float(input("What is the length of the room in feet? "))
    width = float(input("What is the width of the room in feet? "))
    print("You entered dimensions of " + str(length) + " feet by " + str(width) + " feet.")
    area_in_feet = length * width
    print("The area is")
    print(str(area_in_feet) + " square feet")
    area_in_meters = get_square_meters(area_in_feet)
    print(str(area_in_meters) + " square meters")

if __name__ == '__main__':
    main()
