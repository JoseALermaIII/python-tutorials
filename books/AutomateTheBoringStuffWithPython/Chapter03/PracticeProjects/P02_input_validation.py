# This program adds input validation to make_collatz_seq.py

# Add try and except statements to the previous project to detect whether
# the user types in a noninteger string. Normally, the int() function will
# raise a ValueError error if it is passed a noninteger string, as in int('puppy').
# In the except clause, print a message to the user saying they must enter an integer.

from P01_make_collatz_seq import collatz

try:
    n = int(input("Input a number: "))
    while n != 1:
        print(n)
        n = collatz(n)
    print(n)  # When n == 1
except ValueError:
    print("Error: Input must be an integer.")
