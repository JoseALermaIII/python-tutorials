#!/usr/bin/env python3
# Write a program that gets 2 string variables and 2 number variables from the
# user, concatenates (joins them together with no spaces) and displays  the
# strings, then multiplies the two numbers on a new line.
embedded = 1 # using embedded python libraries

if embedded == 1:
    string1 = "Hello "
    string2 = "World"
    print("String1 = ",string1)
    print("String2 = ", string2)
    float1 = 3.0
    float2 = 5.0
    print("Float1 = ", float1)
    print("Float2 = ", float2)
else:
    string1 = input('String 1: ')
    string2 = input('String 2: ')
    float1 = float(input('Number 1: '))
    float2 = float(input('Number 2: '))

print(string1 + string2)
print(float1 + float2)
