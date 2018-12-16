"""Zero divide 3.0

This program also handles a :class:`ZeroDivisionError`, but in the :meth:`~main` function.

"""


def spam(divideBy: int) -> float:
    """Spam

    Divides integer 42 by given integer.

    Args:
        divideBy: Integer to divide 42 by.

    Returns:
        Float result of 42 divided by given integer.
    """
    return 42 / divideBy


def main():
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1))  # skipped due to error
    except ZeroDivisionError:
        print('Error: Invalid argument.')


if __name__ == '__main__':
    main()
