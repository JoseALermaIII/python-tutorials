#!/usr/bin/env python3
def hello():
    print("Hello")

def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

hello()
hello()

print_welcome("Fred")

w = 4
h = 5
print("width =", w, " height =", h, " area=", area(w, h))
