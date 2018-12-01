#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Integer multiplication using recursion

def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b - 1)
    value = a + rest
    return value
result = mult(3, 2)
print(" 3 * 2 = ", result)
