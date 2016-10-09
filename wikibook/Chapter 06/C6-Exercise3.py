#!/usr/bin/env python3
# Write a pgoram that asks for two numbers. If the sum of the numbers is
# greater than 100, print "That is a big number."

number1 = float(input('1st number: '))
number2 = float(input('2nd number: '))
if number1 + number2 > 100:
    print('That is a big number.')
