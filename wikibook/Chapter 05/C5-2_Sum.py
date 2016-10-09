#!/usr/bin/env python3
embedded = 1 # Using embedded python libraries
s = 0

if embedded == 1:
    a = [0, 1, 2, 3]
    for i in a:
        s = s + i
else:
    a = 1
    print('Enter Numbers to add to the sum.')
    print('Enter 0 to quit.')
    while a != 0:
        print('Current Sum: ', a)
        a = float(input('Number? '))
        s = s + a
print('Total Sum =', s)
