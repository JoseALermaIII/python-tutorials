# Define a faster fibonacci procedure that will enable us to compute
# fibonacci(36).


def fibonacci(n):
    i, j = 0, 1
    n -= 2
    while n >= 0:
        i, j = j, j + i
        n -= 1
    return j


print(fibonacci(36))
# >>> 14930352
