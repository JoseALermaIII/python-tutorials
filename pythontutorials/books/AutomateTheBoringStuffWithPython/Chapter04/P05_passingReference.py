"""Passing reference

This program demonstrates how mutable data types are passed to functions by using
the :meth:`eggs` function to append a string to a list of integers.

"""


def eggs(someParameter: list) -> None:
    """eggs

    Appends `'hello'` to a given list.

    Args:
        someParameter: List to append to.

    Returns:
        None.
    """
    someParameter.append('Hello')


def main():
    spam = [1, 2, 3]
    eggs(spam)
    print(spam)


if __name__ == "__main__":
    main()
