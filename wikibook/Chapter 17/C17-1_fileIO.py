#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

# Write a file
with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")

# Read a file
with open("test.txt", "rt") as in_file:
        text = in_file.read()

print(text)
