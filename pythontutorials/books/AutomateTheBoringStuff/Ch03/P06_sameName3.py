"""Same name 3.0

This program demonstrates global and local variable rules.

Attributes:
    eggs (int): Integer defining the answer to all life, universe, and everything.

"""

eggs = 42  # this is the global (outside all functions)


def spam() -> None:
    """Spam

    Reassigns the global variable called eggs.

    Returns:
        None.
    """
    global eggs
    eggs = 'spam'  #: this is the global (global statement)


def bacon() -> None:
    """Bacon

    Assigns a local variable called eggs.

    Returns:
        None.
    """
    eggs = 'bacon'  #: this is a local (assignment)


def ham() -> None:
    """Ham

    Prints global variable called eggs.

    Returns:
        None. Prints global variable, eggs.
    """
    print(eggs)  # this is the global (no assignment)


def main():
    spam()
    print(eggs)


if __name__ == '__main__':
    main()
