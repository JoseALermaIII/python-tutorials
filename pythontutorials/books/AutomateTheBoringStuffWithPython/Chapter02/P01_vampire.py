"""Vampire

This program checks name and age.

"""


def main():
    name = input("What's your name?")
    age = int(input("How old are you?"))
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are not Alice, grannie.')


# If P01_vampire.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
