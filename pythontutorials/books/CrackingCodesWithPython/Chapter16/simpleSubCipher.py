"""Simple Substitution Cipher

Provides functions that implement a substitution cipher.

Attributes:
    LETTERS (str): String containing uppercase latin letters.

Example:
    >>> import pythontutorials.books.CrackingCodesWithPython.Chapter16.simpleSubCipher as simpleSubCipher
    >>> key = simpleSubCipher.getRandomKey()  # key = 'VIAXLGJBKSZDUTRPYCEWNFHOMQ', in this example
    >>> message = 'You\\'d be surprised what you can live through.'
    >>> simpleSubCipher.encryptMessage(key, message)
    "Mrn'x il encpckelx hbvw mrn avt dkfl wbcrnjb"

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)

"""

from pythontutorials.books.CrackingCodesWithPython.pyperclip import copy
import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = '''If a man is offered a fact which goes against his
instincts, he will scrutinize it closely, and unless the evidence
is overwhelming, he will refuse to believe it. If, on the other
hand, he is offered something which affords a reason for acting
in accordance to his instincts, he will accept it even on the
slightest evidence. The origin of myths is explained in this way.
-Bertrand Russell'''
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt'  # Set to 'encrypt' or 'decrypt'.

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % myKey)
    print('The %sed message is:' % myMode)
    print(translated)
    copy(translated)
    print()
    print('This message has been copied to the clipboard.')

    if myMode == 'encrypt':
        print("\nDecrypted message is:")
        print(decryptMessage(myKey, translated))


def keyIsValid(key: str) -> bool:
    """Checks key for validity.

    Ensures key contains all letters in LETTERS.

    Args:
        key: String containing key used to encrypt with substitution cipher.

    Returns:
        True if key and LETTERS match, False otherwise.
    """
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key: str, message: str) -> str:
    """Substitution Cipher Encrypt

    Wrapper function that encrypts given message with the given key using the substitution cipher.

    Args:
        key: String containing key used to encrypt with substitution cipher.
        message: String containing message to encrypt.

    Returns:
        Encrypted message.
    """
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key: str, message: str) -> str:
    """Substitution Cipher Decrypt

    Wrapper function that decrypts given substitution cipher encrypted message with the given key.

    Args:
        key: String containing key used to decrypt substitution cipher.
        message: String containing message to decrypt.

    Returns:
        Decrypted message.
    """
    return translateMessage(key, message, 'decrypt')


def translateMessage(key: str, message: str, mode: str) -> str:
    """Substitution Cipher

    Implements a substitution cipher that can encrypt or decrypt messages depending on the given mode.

    Args:
        key: String containing key used to decrypt/encrypt messages.
        message: String containing message to decrypt/encrypt.
        mode: String specifying whether to 'encrypt' or 'decrypt'.

    Returns:
        Encrypted or decrypted message.
    """
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it:
            translated += symbol

    return translated


def getRandomKey() -> str:
    """Substitution cipher key generator

    Generates a random key that can be used with the substitution cipher.

    Returns:
        String with a random, valid key.
    """
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
