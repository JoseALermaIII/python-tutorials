"""Total brought

This program totals everything being brought to a picnic
by storing the guest's names and items brought as a :obj:`dict` of :obj:`dicts <dict>`.

Attributes:
    allGuests (dict): Dictionary of dictionaries with guest names as keys and values of
        dictionaries with items as keys and number of items as values.

"""

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests: dict, item: str) -> int:
    """Total brought

    Totals given item from given guest dictionary and returns result.

    Args:
        guests: Dictionary with guest's names and what they are bringing.
        item:   Specific item in guest dictionary that is to be totaled.

    Returns:
        Integer total of given item that will be brought.
    """
    numBrought = 0
    """int: Total of given item brought."""

    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought


def main():
    print('Number of things being brought:')
    print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
    print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
    print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
    print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
    print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


if __name__ == '__main__':
    main()
