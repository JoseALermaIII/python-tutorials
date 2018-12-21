"""Validate input

This program asks for numerical age and alphanumeric password
until they are valid inputs.

"""


def main():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')

    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')


if __name__ == '__main__':
    main()
