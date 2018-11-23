""" Chapter 5 Practice Question 4

What do the following pieces of code display on the screen?

Note:
    Contains spoilers for Chapter 7 (functions)
"""


def main():
    # a
    spam = "foo"
    for i in spam:
        spam = spam + i
    print(spam)

    # b
    if 10 < 5:
        print("Hello")
    elif False:
        print("Alice")
    elif 5 != 5:
        print("Bob")
    else:
        print("Goodbye")

    # c
    print("f" not in "foo")

    # d
    print("foo" in "f")

    # e
    print("hello".find("oo"))


# If Question4.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
