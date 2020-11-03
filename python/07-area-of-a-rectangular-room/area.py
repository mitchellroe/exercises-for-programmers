#!/usr/bin/env python
"""foo"""

import math

CONVERSION_FACTOR = 0.09290304


class Room():
    """Get a room"""
    def __init__(self, length=0, width=0, units="imperial"):
        self.length = length
        self.width = width
        self.units = units

    def convert_units(self):
        """Convert the measurements from whatever they are to the other."""

    def get_area(self):
        """Get the square feet / square meters"""
        return self.length * self.width

def main():
    """Prompt for dimensions and convert them."""
    length = get_number("What is the length of the room in feet? ")
    width = get_number("What is the width of the room in feet? ")
    print("You entered dimensions of " + str(length) + " feet by " + str(width) + " feet.")

    area_in_feet = length * width
    print("The area is")
    print(str(area_in_feet) + " square feet")
    area_in_meters = get_square_meters(area_in_feet)
    print(str(area_in_meters) + " square meters")


def get_number(prompt="Please enter a number: ", error_message="Invalid number, please try again."):
    """Prompt for a number"""
    my_number = input(prompt)
    while not my_number.isnumeric():
        print(error_message)
        my_number = input(prompt)
    return my_number


def get_square_meters(square_feet):
    """Converts square feet into square meters"""
    square_meters = (square_feet * square_feet) * CONVERSION_FACTOR
    square_meters = math.sqrt(square_meters)
    return square_meters


def get_square_feet(square_meters):
    """Converts square meters into square feet"""
    square_meters = (square_feet * square_feet) * CONVERSION_FACTOR
    square_meters = math.sqrt(square_meters)
    return square_meters


if __name__ == '__main__':
    main()
