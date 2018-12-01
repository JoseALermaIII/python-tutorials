"""Hello function.

Contains function that prints hello to given name.
"""


def hello(name: str) -> None:
    """Prints hello.

    Prints hello to given name.

    Args:
        name: Name to say hello to.

    Returns:
        Prints hello to given name.
    """
    print('Hello, ' + name)


def main():
    print('Start.')
    hello('Clarice')
    print('Call the function again:')
    hello('Dr. Lecter')
    print('Done.')


if __name__ == '__main__':
    main()
