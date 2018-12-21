"""Great

This program asks how you're doing and responds by filtering input
through an if-else statement.

"""


def main():
    print('How are you?')
    feeling = input()
    if feeling.lower() == 'great':
        print('I feel great too.')
    else:
        print('I hope the rest of your day is good.')


if __name__ == '__main__':
    main()
