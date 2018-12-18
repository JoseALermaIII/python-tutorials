"""Hello function

This program uses a function to say hello.

"""


def hello() -> None:
    """Hello

    Prints hello three different ways.

    Returns:
        None. Only prints three statements.

    """
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


def main():
    hello()
    hello()
    hello()


if __name__ == '__main__':
    main()
