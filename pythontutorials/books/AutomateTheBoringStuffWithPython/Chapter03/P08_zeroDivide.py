"""Zero Divide

This program also produces an error by dividing by zero.

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
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


if __name__ == '__main__':
    main()
