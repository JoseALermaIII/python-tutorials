# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(n1, n2):
    if n1 == n2:
        return n1
    if n1 > n2:
        return n1
    return n2


print bigger(2, 7)
# >>> 7

print bigger(3, 2)
# >>> 3

print bigger(3, 3)
# >>> 3
