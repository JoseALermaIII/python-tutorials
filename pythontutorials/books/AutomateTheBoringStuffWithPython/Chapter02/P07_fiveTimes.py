"""Five times

This program runs five times.

"""


def main():
    print('My name is')
    for i in range(5):
        print('Jimmy Five Times(' + str(i) + ')')


# If P07_fiveTimes.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
