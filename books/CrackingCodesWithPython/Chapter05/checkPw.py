"""Password checker.

Checks given input to saved password.
"""


def main():
    # Password checker
    typedPassword = input("Enter your password.\n")
    if typedPassword == "hunter2":
        print("You entered: *******")
    elif typedPassword == "jose":
        print("Hint: the password is a meme.")
    elif typedPassword == "12345":
        print("That is a really obvious password.")
    else:
        print("You entered: " + typedPassword)
    print("Done")


if __name__ == '__main__':
    main()
