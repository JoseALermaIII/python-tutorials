"""Same name 4.0

This program produces an error trying to print a
local global variable while assigning a local variable with the same name.

Attributes:
    eggs (str): String denoting global variable.

"""

eggs = 'global'


def spam() -> None:
    """Spam

    Attempts to print global variable, eggs, while assigning local variable, eggs.

    Returns:
        None.
    """
    print(eggs)  # ERROR!
    eggs = 'spam local'  #: looks ahead and says eggs is local


def main():
    spam()


if __name__ == '__main__':
    main()
