"""Your name

This program forces you to type your name

"""


def main():
    name = ''
    while name != 'your name':
        print('Please type your name.')
        name = input()
    print('Thank you!')


# If P04_yourName.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
