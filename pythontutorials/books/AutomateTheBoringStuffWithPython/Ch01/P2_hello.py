"""Hello

This program says hello and asks for my name.

"""


def main():
    print('Hello world!')
    print('What is your name?')  # ask for their name
    myName = input()
    print('It is good to meet you, ' + myName)
    print('The length of your name is:')
    print(len(myName))
    print('What is your age?')  # ask for their age
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# If P2_hello.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
