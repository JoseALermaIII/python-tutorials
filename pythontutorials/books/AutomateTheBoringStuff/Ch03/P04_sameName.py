"""Same name

This program uses the same variable name throughout.

Attributes:
    eggs (str): String denoting global variable.

Note:
    Not recommended, but possible.

"""

eggs = 'global'


def spam() -> None:
    """Spam

    Prints its local variable called eggs.

    Returns:
        None. Prints the local variable.
    """
    eggs = 'spam local'  #: String denoting local variable.
    print(eggs)  # prints 'spam local'


def bacon() -> None:
    """Bacon

    Prints its local variable called eggs and also calls :meth:`spam`.

    Returns:
        None. Prints local variables.
    """
    eggs = 'bacon local'  #: String denoting local variable.
    print(eggs)  # prints 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'


def main():
    bacon()
    print(eggs)  # prints 'global'


if __name__ == '__main__':
    main()
