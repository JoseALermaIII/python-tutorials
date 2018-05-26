# Define a faster fibonacci procedure that will enable us to compute
# fibonacci(36).


def fibonacci(n):
    i, j = 0, 1
    n -= 1
    while n >= 0:
        i, j = j, j + i
        n -= 1
    return i

print(fibonacci(0))
# >>> 0
print(fibonacci(1))
# >>> 1
print(fibonacci(2))
# >>> 1
print(fibonacci(3))
# >>> 2
print(fibonacci(36))
# >>> 14930352
