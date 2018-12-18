"""Same name 2.0

This program has only one variable.

Attributes:
    eggs (str): String denoting global variable.

"""

eggs = 'global'


def spam() -> None:
    """Spam

    Reassigns global variable called eggs.

    Returns:
        None.
    """
    global eggs
    eggs = 'spam'  #: Reassign global variable.


def main():
    spam()
    print(eggs)


if __name__ == '__main__':
    main()
