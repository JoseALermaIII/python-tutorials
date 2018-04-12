#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# defines a function that counts down from a given  integer

def count_down(n):
    print(n)
    if n > 0:
        return count_down(n-1)

count_down(5)
