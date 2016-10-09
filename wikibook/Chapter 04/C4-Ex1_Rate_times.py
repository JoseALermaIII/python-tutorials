#!/usr/bin/env python3
# This program calculates rate and distance problems
embedded = 1

print("Input a rate and a distance")

if embedded == 1:
    rate = 2.0
    distance = 5.0
    print("Rate = ", rate)
    print("Distance = ", distance)
else:
    rate = float(input("Rate: "))
    distance = float(input("Distance: "))

print("Time:", (distance / rate))
