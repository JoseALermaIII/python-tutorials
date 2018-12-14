"""Caesar Cipher improved.

Rewritten as function with wrapper functions for importing.

Note:
    Contains spoilers from Chapter 5 (caesarCipher) and Chapter 7 (functions)
"""

from pythontutorials.books.CrackingCodesWithPython.Chapter01.constants import SYMBOLS


def decryptMessage(key: int, message: str) -> str:
    """Decrypts encrypted caesar cipher.

    Wrapper function that calls caesarCipher() to decrypt given message with given key.

    Args:
        key: Key to use to decrypt message.
        message: Message to decrypt.

    Returns:
        Decrypted message string.
    """
    return caesarCipher(key, message, "decrypt")


def encryptMessage(key: int, message: str) -> str:
    """Encrypts message with caesar cipher.

    Wrapper function that calls caesarCipher() to encrypt given message with given key.

    Args:
        key: Key to use to encrypt message.
        message: Message to encrypt.

    Returns:
        Encrypted message string.
    """
    return caesarCipher(key, message, "encrypt")


def caesarCipher(key: int, message: str, mode: str) -> str:
    """Implement caesar cipher.

    Encrypts or decrypts given message with given key depending on given mode.

    Args:
        key: Key to use for [de|en]cryption.
        message: Message to encrypt/decrypt.
        mode: Specifies encryption or decryption.

    Returns:
        Encrypted/decrypted message string.

    Example:
        >>> from pythontutorials.books.CrackingCodesWithPython.Chapter01.caesarCipher import caesarCipher
        >>> caesarCipher(4, 'IMPIETY: YOUR IRREVERENCE TOWARD MY DEITY.', 'encrypt')
        'MQTMIXc:AcSYVAMVVIZIVIRGIAXSaEVHAQcAHIMXcD'
    """

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

    return translated
