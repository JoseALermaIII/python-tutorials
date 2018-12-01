"""Vigenère Cipher Dictionary Hacker

Implements a function that can hack a Vigenère cipher encrypted message using a dictionary.

Attributes:
    DICTIONARY_FILE (str): String with absolute location of dictionary.txt file.

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)

"""

from books.CrackingCodesWithPython.pyperclip import copy
from books.CrackingCodesWithPython.Chapter11.detectEnglish import isEnglish
from books.CrackingCodesWithPython.Chapter18.vigenereCipher import decryptMessage

DICTIONARY_FILE = "/home/jose/PycharmProjects/python-tutorials/books/CrackingCodesWithPython/Chapter11/dictionary.txt"


def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackVigenereDictionary(ciphertext: str):
    """Hack Vigenère Dictionary

    Brute-forces ciphertext by using every word in the dictionary file as a key. Checks if decrypted message is
    English with the :func:`~books.CrackingCodesWithPython.Chapter11.detectEnglish.isEnglish` module, and prompts user
    for confirmation by displaying first 100 characters.

    Args:
        ciphertext: String containing Vigenère cipher encrypted message.

    Returns:
         Decrypted message, if confirmed, None otherwise.
    """
    fo = open(DICTIONARY_FILE)
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()  # Remove the newline at the end.
        decryptedText = decryptMessage(word, ciphertext)
        if isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found:
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText


if __name__ == '__main__':
    main()
