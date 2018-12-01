#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found.")
    prev = item
