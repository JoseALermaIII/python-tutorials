"""Busy work

This program adds numbers 0 to 100.

"""


def main():
    total = 0
    for num in range(101):
        total = total + num
    print(total)


# If P08_busywork.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
