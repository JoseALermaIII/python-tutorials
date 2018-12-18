"""Swordfish

This program asks for a name and password.

"""


def main():
    while True:
        print('Who are you?')
        name = input()
        if name != 'Joe':
            continue
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()
        if password == 'swordfish':
            break
    print('Access granted.')


# If P06_swordfish.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
