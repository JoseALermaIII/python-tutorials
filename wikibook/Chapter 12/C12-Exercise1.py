#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Write a program that has a user guess your name, but they only get 3
# chances to do so until the program quits.
print("Try to guess my name!")
count = 1
name = "guileherme"
guess = input("What is my name? ")
while count < 3 and guess.lower() != name: # . lower allows things like Guileherme to still match.
    print("You are wrong!")
    guess = input("What is my name? ")
    count = count + 1

if guess.lower() != name:
    print("You are wrong!") # this message isn't printed in the third chance, so we print it now
    print("You ran out of chances.")
else:
    print("Yes! My name is", name + "!")
