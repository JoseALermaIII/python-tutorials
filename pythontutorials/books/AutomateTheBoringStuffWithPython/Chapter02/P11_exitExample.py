"""Exit example

This program terminates itself when told to using the :py:mod:`sys` module.

"""


def main():
    import sys

    while True:
        print('Type exit to exit.')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')


# If P11_exitExample.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
