#!/usr/bin/env python3

embedded = 1 # using embedded python libraries. No user inputs.
print("Halt!")

if embedded == 1:
    user_input = "Joe"
else:
    user_input = input("Who goes there? ")

print("You may pass, ", user_input)
