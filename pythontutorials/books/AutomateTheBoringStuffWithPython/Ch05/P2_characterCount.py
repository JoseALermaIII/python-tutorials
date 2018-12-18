"""Character count

This program counts how often each character appears in a string.

"""


def main():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    """str: Message to count characters."""

    count = {}
    """dict: Characters as keys and counts as values."""
    
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    
    print(count)


if __name__ == '__main__':
    main()
