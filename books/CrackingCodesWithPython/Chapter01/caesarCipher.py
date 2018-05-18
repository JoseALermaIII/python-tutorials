# Caesar Cipher improved
# Rewritten as function with wrapper functions for importing
# SPOILERS: Chapter 5 (caesarCipher), Chapter 7 (functions)

import books.CrackingCodesWithPython.Chapter01.config


def decryptMessage(key, message):
    return caesarCipher(key, message, "decrypt")


def encryptMessage(key, message):
    return caesarCipher(key, message, "encrypt")


def caesarCipher(key, message, mode):

    # Store the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in books.CrackingCodesWithPython.Chapter01.config.SYMBOLS:
            symbolIndex = books.CrackingCodesWithPython.Chapter01.config.SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wraparound, if needed:
            if translatedIndex >= len(books.CrackingCodesWithPython.Chapter01.config.SYMBOLS):
                translatedIndex -= len(books.CrackingCodesWithPython.Chapter01.config.SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(books.CrackingCodesWithPython.Chapter01.config.SYMBOLS)

            translated += books.CrackingCodesWithPython.Chapter01.config.SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    return translated
