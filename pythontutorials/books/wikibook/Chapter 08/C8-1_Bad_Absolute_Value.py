#!/usr/bin/env python3
# Example of repetitive programming. Do not type it out.
# NOTE Finding the absolute value changes the value of the variable.
a = 23
b = -23

if a < 0:
    a = -a
if b < 0:
    b = -b
if a == b:
    print("The absolute values of", a, "and", b, "are equal.")
else:
    print("The absolute values of", a, "and", b, "are different.")
