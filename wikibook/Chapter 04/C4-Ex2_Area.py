#!/usr/bin/env python3
# This program calculats the perimeter and area of a rectangle
embedded = 1 # using embedded python libraries

print("Calculate information about a rectangle")

if embedded == 1:
    length = 3.0
    width = 5.0
    print("length = ", length)
    print("width = ", width)
else:
    length = float(input("Length: "))
    width = float(input("Width: "))

print("Area:", length * width)
print("Perimeter:", 2 * length + 2 * width)
