# What value does each of the following expressions evaluate to?
# aka "Lists are OP"


def main():
    print(len([2, 4]))
    print(len([]))
    print(len(['', '', '']))
    print([4, 5, 6] + [1, 2, 3])
    print(3 * [1, 2, 3] + [0])  # I hate you
    print(42 in [41, 42, 42, 42])


# If Question4.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
