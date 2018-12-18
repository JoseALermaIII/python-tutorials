"""Your name 2.0

This program also forces you to type your name, but using a different way to exit the loop.

"""


def main():
    while True:
        print('Please type your name.')
        name = input()
        if name == 'your name':
            break
    print('Thank you!')


# If P12_yourName2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
