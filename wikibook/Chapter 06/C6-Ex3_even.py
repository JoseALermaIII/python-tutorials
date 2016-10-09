#!/usr/bin/env python3
# Asks for a number.
# Prints if it is even or odd

number = float(input("Tell me a number: "))
if number % 2 == 0:
    print(int(number), "is even")
elif number % 2 == 1:
    print(int(number), "is odd.")
else:
    print(number, "is very strange.")
