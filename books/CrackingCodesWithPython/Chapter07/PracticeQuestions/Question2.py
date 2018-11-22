# Is each spam a global or local variable?

spam = 42  # global/local


def foo():
    global spam
    spam = 99  # global/local
    print(spam)


def main():
    foo()  # mind == blown


# If Question2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
