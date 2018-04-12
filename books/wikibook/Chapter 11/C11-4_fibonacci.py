#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

a = 1
b = 1
for c in range(1, 10):
    print(a, end=" ")
    n = a + b
    a = b
    b = n 
