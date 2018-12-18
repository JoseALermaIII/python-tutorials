"""Zero Divide 2.0

This program handles a :class:`ZeroDivisionError`.

"""


def spam(divideBy: int) -> float:
    """Spam

    Divides integer 42 by given integer, but also handles a :class:`ZeroDivisionError`.

    Args:
        divideBy: Integer to divide 42 by.

    Returns:
        Float result of 42 divided by given integer.
    """
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


def main():
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


if __name__ == '__main__':
    main()
