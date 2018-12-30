"""Caesar Hacker improved.

Rewritten as function for importing.

Note:
    Contains spoilers from Chapter 6 (caesarHacker) and Chapter 7 (functions)
"""

from pythontutorials.books.CrackingCodes.Chapter01.constants import SYMBOLS


def hackCaesar(message: str) -> None:
    """Hacks caesar cipher.

    Loops through and displays every possible key.

    Args:
        message: Message to be decrypted.

    Returns:
        Prints each decryption with every possible key.
    """

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared:
        translated = ''

        # The rest of the program is almost the same as the Caesar program:

        # Loop through each symbol in message:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wraparound:
                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                # Append the decrypted symbol:
                translated += SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated += symbol

        # Display every possible decryption:
        print('Key #%s: %s' % (key, translated))
    return None
