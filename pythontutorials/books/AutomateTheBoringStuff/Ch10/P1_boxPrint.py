"""P1_boxPrint.py

This program prints out a box based on input sizes.

"""


def boxPrint(symbol: str, width: int, height: int) -> None:
    """Box print

    Prints a box of given width and height using the given symbol.

    Args:
        symbol: String to use to make sides of box.
        width: Integer width of box.
        height: Integer height of box.

    Returns:
        None. Prints box to specified dimensions.

    Raises:
        Exception: If `symbol` != 1 or if either `width` or `height` <= 2.
    """
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


def main():
    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ("ZZ", 3, 3)):
        try:
            boxPrint(sym, w, h)
        except Exception as err:
            print("An exception happened: " + str(err))


if __name__ == '__main__':
    main()
