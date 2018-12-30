"""Passing references in a function

Demonstrates how to pass a reference to a function.
"""


def eggs(someParameter: list) -> None:
    """Append to a parameter.

    Appends 'Hello' to a given parameter.

    Args:
        someParameter: List of elements.

    Returns:
        None. Only appends a string to a provided parameter.
    """
    someParameter.append('Hello')


def main():
    spam = [1, 2, 3]
    eggs(spam)
    print(spam)


if __name__ == '__main__':
    main()
