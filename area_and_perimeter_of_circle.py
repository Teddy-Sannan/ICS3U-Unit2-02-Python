#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: September 16
# This program calculates the area and perimeter of a rectangle


def main():
    # main function
    print("We will be calculating the area and perimeter of a rectangle")
    print("")
    # input
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))
    # process
    perimeter = 2 * (length + width)
    area = length * width
    print("")
    # output
    print("Perimeter is {} mm".format(perimeter))
    print("Area is {} mm^2".format(area))


if __name__ == "__main__":
    main()
