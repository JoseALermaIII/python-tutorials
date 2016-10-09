#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Rewrite the high_low.py program from section Decisions to use an random
# integer between 0 and 99 instead of the hard-coded 78. Use the Python
# documentation to find an appropriate module and function to do this.

from random import randint
number = randint(0, 99)
guess = -1
while guess != number:
    guess = int(input("Guess a number: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
print("Just right")
