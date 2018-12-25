"""Error Example

This program raises an exception and automatically displays the traceback.

"""


def spam() -> None:
    """Spam

    Calls :meth:`bacon`.

    Returns:
        None.
    """
    bacon()


def bacon() -> None:
    """Bacon

    Raises base exception.

    Returns:
        None.

    Raises:
        Exception: Always
    """
    raise Exception("This is the error message.")


def main():
    spam()


if __name__ == '__main__':
    main()
