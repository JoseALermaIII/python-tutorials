"""Fantasy game inventory

This program models a player's inventory from a fantasy game.

You are creating a fantasy video game. The data structure to model the player’s
inventory will be a :obj:`dictionary <dict>` where the keys are :obj:`string <str>`
values describing the item in the inventory and the value is an :obj:`integer <int>`
value detailing how many of that item the player has.

For example, the dictionary value::

    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named :meth:`displayInventory` that would take any possible “inventory”
and display it like the following::

    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger

    Total number of items: 62

Attributes:
    stuff (dict): Dictionary with item names as keys and their counts as values.
"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory: dict) -> None:
    """Display inventory

    Displays each key in a given inventory dictionary.

    Args:
        inventory: Inventory dictionary to display.

    Returns:
        None. Prints out inventory.

    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))


def main():
    displayInventory(stuff)


if __name__ == '__main__':
    main()
