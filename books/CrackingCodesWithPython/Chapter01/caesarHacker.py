# Caesar Hacker improved
# Rewritten as function for importing
# SPOILERS: Chapter 6 (caesarHacker), Chapter 7 (functions)

import books.CrackingCodesWithPython.Chapter01.config


def hackCaesar(message):

    # Loop through every possible key:
    for key in range(len(books.CrackingCodesWithPython.Chapter01.config.SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared:
        translated = ''

        # The rest of the program is almost the same as the Caesar program:

        # Loop through each symbol in message:
        for symbol in message:
            if symbol in books.CrackingCodesWithPython.Chapter01.config.SYMBOLS:
                symbolIndex = books.CrackingCodesWithPython.Chapter01.config.SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wraparound:
                if translatedIndex < 0:
                    translatedIndex += len(books.CrackingCodesWithPython.Chapter01.config.SYMBOLS)

                # Append the decrypted symbol:
                translated += books.CrackingCodesWithPython.Chapter01.config.SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated += symbol

        # Display every possible decryption:
        print('Key #%s: %s' % (key, translated))
    return None
