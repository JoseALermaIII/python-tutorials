"""Print random

This program prints five random numbers using the :py:mod:`random` module.

"""


def main():
    import random
    for i in range(5):
        print(random.randint(1, 10))


# If P10_printRandom.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
