"""Vigenère Cipher (Polyalphabetic Substitution Cipher)

Provides functions that implement a Vigenère cipher.

Attributes:
    LETTERS (str): String containing uppercase latin letters.

Example:
    >>> import books.CrackingCodesWithPython.Chapter18.vigenereCipher as vigenereCipher
    >>> key = 'supercalifragilisticexpialidocious'
    >>> message = 'A soul shines brightest when it stands alongside the darkness. -Anon, probably'
    >>> vigenereCipher.encryptMessage(key, message)
    'S mdyc uhtvjj bxqrplxav aetv ie awoplg udghvwzfe epj uaxsymkl. -Ipsk, ezomieza'

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)

"""

from books.CrackingCodesWithPython.pyperclip import copy

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    # This text can be downloaded from https://www.nostarch.com/crackingcodes/:
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey = 'ASIMOV'
    myMode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    copy(translated)
    print()
    print('The message has been copied to the clipboard.')

    if myMode == 'encrypt':
        print("\nDecrypted message: ")
        print(decryptMessage(myKey, translated))


def encryptMessage(key: str, message: str) -> str:
    """Vigenère cipher encryption

    Wrapper function that encrypts given message with given key using the Vigenère cipher.

    Args:
        key: String encryption key to encrypt with Vigenère cipher.
        message: Message string to encrypt.

    Returns:
        Encrypted message string.
    """
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key: str, message: str) -> str:
    """Vigenère cipher decryption

    Wrapper function that decrypts given message with given key using the Vigenère cipher.

    Args:
        key: String decryption key to encrypt with Vigenère cipher.
        message: Message string to decrypt.

    Returns:
        Decrypted message string.
    """
    return translateMessage(key, message, 'decrypt')


def translateMessage(key: str, message: str, mode: str) -> str:
    """Vigenère cipher

    Implements a Vigenère cipher that can encrypt or decrypt messages depending on the given mode.

    Args:
        key: String containing key used to decrypt/encrypt messages.
        message: String containing message to decrypt/encrypt.
        mode: String specifying whether to 'encrypt' or 'decrypt'.

    Returns:
        Encrypted or decrypted message.
    """
    translated = []  # Stores the encrypted/decrypted message string.

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # Subtract if decrypting.

            num %= len(LETTERS)  # Handle any wraparound.

            # Add the encrypted/decrypted symbol to the end of translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting:
            translated.append(symbol)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
