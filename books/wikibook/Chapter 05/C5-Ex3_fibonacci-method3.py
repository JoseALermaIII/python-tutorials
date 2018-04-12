#!/usr/bin/env python3
a = 0
b = 1
count = 0
maxcount = 20

# Once loop is started we stay in it
while count < maxcount:
    count += 1
    olda = a
    a = a + b
    b = olda
    print(olda, end = ' ')
print()
