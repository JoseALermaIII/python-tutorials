"""Five times 2.0

This program also runs five times, but using a while loop.

"""


def main():
    print('My name is')
    i = 0
    while i < 5:
        print('Jimmy Five Times (' + str(i) + ')')
        i = i + 1


# If P09_fiveTimes2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
