#!/usr/bin/env python3
embedded = 1 # using embedded python libraries

if embedded == 1:
    number = 3.0
    integer = 3
    text = "3"
else:
    number = float(input("Type in a number: "))
    integer = int(input("Type in an integer: "))
    text = input("Type in a string: ")

print("number =", number)
print("number is a", type(number))
print("number * 2 =", number * 2)
print("integer =", integer)
print("integer is a", type(integer))
print("integer * 2 =", integer * 2)
print("text =", text)
print("text is a", type(text))
print("text * 2 =", text * 2)
