"""Hello function 2.0

This program uses a function with an input argument to say hello to Alice and Bob.

"""


def hello(name: str) -> None:
    """Hello

    Says hello to a given name.

    Args:
        name: String containing name of person to say hello to.

    Returns:
        None. Prints out a statement.
    """
    print('Hello ' + name)


def main():
    hello('Alice')
    hello('Bob')


if __name__ == '__main__':
    main()
