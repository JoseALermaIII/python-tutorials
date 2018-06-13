# This program also handles an error
def spam(divideBy):
    return 42 / divideBy


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))  # skipped due to error
except ZeroDivisionError:
    print('Error: Invalid argument.')
