"""Vampire 2.0

This program checks name and age, but won't work as planned.

"""


def main():
    name = input("What's your name?")
    age = int(input("How old are you?"))
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    elif age > 100:
        print('You are not Alice, grannie.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')


# If P02_vampire2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
