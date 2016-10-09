#!/usr/bin/env python3
# This program converts Fahrenheit to Celsius
embedded = 1 # using embedded python libraries

if embedded == 1:
    fahr_temp = 33
    print("Fahrenheit Temperature = ", fahr_temp)
else:
    fahr_temp = float(input("Fahrenheit temperature: "))

print("Celsius temperature:", (fahr_temp - 32.0) * 5.0 / 9.0)
