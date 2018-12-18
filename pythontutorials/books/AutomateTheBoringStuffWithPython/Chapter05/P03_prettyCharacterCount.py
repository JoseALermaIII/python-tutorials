"""Pretty character count

This program also counts the number of times a character appears in a string
but with a prettier output via the :py:mod:`pprint` module.

"""


def main():
    import pprint

    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    """str: Message to count characters."""

    count = {}
    """dict: Characters as keys and counts as values."""

    for character in message:
        count.setdefault(character, 0)
        count[character] += 1

    pprint.pprint(count)


if __name__ == '__main__':
    main()
