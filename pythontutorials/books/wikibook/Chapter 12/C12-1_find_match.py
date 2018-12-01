#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

list = ["Life", "The Universe", "Everything", "Jack", "Jill", "Life", "Jill"]

# make a copy of the list. See the More on Lists chapter to explain what [:]
# means.
copy = list[:]
# sort the copy
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# go through the list searching for a match
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# If a match was not found then count can't be < len
# since the while loop continues while count is < len
# and no match is found

if count < len(copy):
    print("First Match:", prev)
