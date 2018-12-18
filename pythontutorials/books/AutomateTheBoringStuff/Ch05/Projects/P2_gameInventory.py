"""Fantasy game inventory 2.0

This program models a player's inventory from a fantasy game with the ability to add
to the inventory.

Imagine that a vanquished dragon’s loot is represented as a :obj:`list` of :obj:`strings <str>`
like this::

    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named :meth:`addToInventory(inventory, addedItems) <addToInventory>`,
where the inventory parameter is a :obj:`dictionary <dict>` representing the player’s inventory
(like in the :py:mod:`previous project <.P01_fantasy_game_inventory>`) and the `addedItems`
parameter is a :obj:`list` like `dragonLoot`. The :meth:`addToInventory` function should return a
:obj:`dictionary <dict>` that represents the updated inventory.

Note:
    The `addedItems` list can contain multiples of the same item.
"""


from pythontutorials.books.AutomateTheBoringStuff.Ch05.Projects.P1_gameInventory import displayInventory


def addToInventory(inventory: dict, addedItems: list) -> dict:
    """Add to inventory

    Adds given list of items to given dictionary inventory.

    Args:
        inventory: Dictionary inventory to add items to.
        addedItems: List of strings to add to inventory.

    Note:
        If the item already exists in the dictionary, its count is incremented.
    """
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)


if __name__ == '__main__':
    main()
