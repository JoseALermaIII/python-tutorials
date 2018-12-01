"""Caesar Cipher

Demonstrates the use of a caesar cipher. Prints output and copies to clipboard.

Note:
    https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

from pythontutorials.books.CrackingCodesWithPython.pyperclip import copy


def main():
    # The string to be encrypted/decrypted:
    message = 'This is my secret message.'

    # The encryption/decryption key:
    key = 13

    # Whether the program encrypts or decrypts:
    mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Store the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    # Output the translated string:
    print(translated)
    copy(translated)


if __name__ == '__main__':
    main()
