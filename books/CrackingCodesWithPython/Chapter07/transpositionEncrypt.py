"""Transposition Cipher Encryption

Demonstrates how to implement a transposition cipher.

Note:
    https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

from books.CrackingCodesWithPython.pyperclip import copy


def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')

    # Copy the encrypted string in cipher text to the clipboard:
    copy(ciphertext)


def encryptMessage(key: int, message: str) -> str:
    """Transposition Cipher Encrypt

    Encrypts given message using a transposition cipher with given key.

    Args:
        key: Numeric key to encrypt with.
        message: Message to encrypt.

    Returns:
        Message encrypted in a string.

    Example:
        >>> encryptMessage(9, 'Underneath a huge oak tree there was of swine a huge company,')
        'Uhot  on ahoamdakef pe  r harhtesunnur wgyegewie,aeean t  sec'
    """
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()
