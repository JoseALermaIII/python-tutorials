"""Little kid

This program checks name and age, but not as many ages.

"""


def main():
    name = input("What's your name?")
    age = int(input("How old are you?"))
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    else:
        print('You are neither Alice nor a little kid.')


# If P03_littleKid.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
