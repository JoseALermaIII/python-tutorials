#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

def shout(string):
    for character in string:
        print("Gimme a " + character)
        print("'" + character + "'")

shout("Lose")

def middle(string):
    print("The middle character is:", string[len(string) // 2])

middle("abcdefg")
middle("The Python Programming Language")
middle("Atlanta")
