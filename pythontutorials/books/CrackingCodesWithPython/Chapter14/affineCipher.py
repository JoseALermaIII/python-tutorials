"""Affine Cipher

Provides functions that implement affine cipher encryption and decryption.

Attributes:
    SYMBOLS (str): String containing all symbols that can be encrypted/decrypted.

Example:
    >>> import pythontutorials.books.CrackingCodesWithPython.Chapter14.affineCipher as affineCipher
    >>> someString = 'Enthusiasm is contagious. Not having enthusiasm is also contagious.'
    >>> key = affineCipher.getRandomKey()  # key = 921, in this example
    >>> affineCipher.encryptMessage(key, someString)
    'xq3eBprFpdLrpLf4q3FRr4BpyLi43LeFOrqRL6q3eBprFpdLrpLFQp4Lf4q3FRr4Bpy'

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
    * There must be a "dictionary.txt" file in this directory with all
      English words in it, one word per line. You can download this from
      https://www.nostarch.com/crackingcodes/.
"""

import sys
import random
from pythontutorials.books.CrackingCodesWithPython.pyperclip import copy
from pythontutorials.books.CrackingCodesWithPython.Chapter13.cryptomath import gcd, findModInverse
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    myMessage = """"A computer would deserve to be called intelligent if it 
    could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % myKey)
    print('%sed text:' % (myMode.title()))
    print(translated)
    copy(translated)
    print('Full %sed text copied to clipboard.' % myMode)

    if myMode == 'encrypt':
        print("Decrypted text:")
        translated = decryptMessage(myKey, translated)
        print(translated)

    return None


def getKeyParts(key: int) -> (int, int):
    """Split key into parts

    Splits key into keyA and keyB via floor division and modulus by length of SYMBOLS.

    Args:
         key: Integer key used to encrypt message.

    Returns:
        Tuple containing the integral and remainder.
    """
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def checkKeys(keyA: int, keyB: int, mode: str) -> None:
    """Checks keys for validity.

    Prevents keyA from being 1 and keyB from being 0 (if encrypting).
    Makes sure keyA is relatively prime with the length of SYMBOLS.
    Ensures keyA is greater than 0 and that keyB is between 0 and length of SYMBOLS.

    Args:
        keyA: Integer integral of the original key after floor division by length of SYMBOLS.
        keyB: Integer remainder of the original key after modulus by length of SYMBOLS.
        mode: String specifying whether to 'encrypt' or 'decrypt'.

    Returns:
        None if successful, exits program with error message otherwise.
    """
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s ' % (len(SYMBOLS) - 1))
    if gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.'
                 % (keyA, len(SYMBOLS)))


def encryptMessage(key: int, message: str) -> str:
    """Affine cipher encryption

    Encrypts given message with given key using the affine cipher.

    Args:
        key: Integer encryption key to encrypt with affine cipher.
        message: Message string to encrypt.

    Returns:
        Encrypted message string.
    """
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol  # Append the symbol without encrypting.
    return ciphertext


def decryptMessage(key: int, message: str) -> str:
    """Affine cipher decryption

    Decrypts given affine cipher encrypted message with given key.

    Args:
        key: Integer decryption key to decrypt affine cipher.
        message: Message string to decrypt.

    Returns:
        Decrypted message string.
    """
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol  # Append the symbol without decrypting.
    return plaintext


def getRandomKey() -> int:
    """Affine cipher key generator

    Generates a random key that can be used with the affine cipher.

    Returns:
        Random, valid integer key

    """
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


# If affineCipher.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
