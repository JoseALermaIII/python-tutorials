"""Picnic table

This program prints a table of everything taken to a picnic using a dictionary
with two different sets of left and right justification.

"""


def printPicnic(itemsDict: dict, leftWidth: int, rightWidth: int) -> None:
    """Print picnic

    Prints given picnic dictionary with given justification.

    Args:
         itemsDict: Dictionary with picnic items as keys and amounts as values.
         leftWidth: Left justification of keys.
         rightWidth: Right justification of values.

    Returns:
        None. Prints out dictionary with justification.
    """
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


def main():
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)


if __name__ == '__main__':
    main()
