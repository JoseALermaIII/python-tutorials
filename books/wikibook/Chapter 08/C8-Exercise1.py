#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Rewrite the area2.py program to have a separate function for the area of
# a square, rhe area of a rectangle, and the area of a circle
# (3.14 * radius **2). This program should include a menu interface.

def square(L):
    return L* L

def rectangle(width , height):
    return width * height

def circle(redius):
    return 3.14159 * radius ** 2

def options():
    print()
    print("Options:")
    print("s = calculate the area of a square.")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("q = quit")
    print()

print("This program will calculate the area of a square, circle or rectangle.")
choice = "x"
options()
while choice != "q":
    choice = input("Please enter your choice:")
    if choice == "s":
        L = float(input("Length of square side: "))
        print("The area of this square is", square(L))
        options()
    elif choice == "c":
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))
        options()
    elif choice = "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))
        options()
    elif choice == "q":
        print(" ", end="")
    else:
        print("Unrecognized option.")
        options()
