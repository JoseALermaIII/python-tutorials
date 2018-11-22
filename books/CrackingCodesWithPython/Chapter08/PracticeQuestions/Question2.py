# When you enter the following code into the interactive shell (*cough*), what does
# each line print?

import math


def main():
    print(math.ceil(3.0))
    print(math.floor(3.1))
    print(round(3.1))
    print(round(3.5))
    print(False and False)
    print(False or False)
    print(not not True)


# If Question2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
