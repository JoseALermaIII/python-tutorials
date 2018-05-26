# Define a faster fibonacci procedure that will enable us to compute
# fibonacci(36).


def fibonacci(n):
    current, after = 0, 1
    n -= 1
    while n >= 0:
        current, after = after, after + current
        n -= 1
    return current


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
