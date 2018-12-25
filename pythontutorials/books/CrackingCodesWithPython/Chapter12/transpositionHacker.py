"""Transposition Cipher Hacker

Implements a function that can hack a transposition cipher encrypted message.

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

from pythontutorials.books.CrackingCodesWithPython.Chapter11.detectEnglish import isEnglish
from pythontutorials.books.CrackingCodesWithPython.Chapter08.transpositionDecrypt import decryptMessage


def main():
    from pyperclip import copy
    # You might want to copy & paste this text from the source code at
    # https://www.nostarch.com/crackingcodes/:
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage is None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        copy(hackedMessage)


def hackTransposition(message: str):
    """Hacks transposition cipher encrypted messages

    Brute-forces a given encrypted message by looping through all the keys, checking if the result is English, and
    prompting the user for confirmation of decryption.

    Args:
        message: String with message to brute-force.

    Returns:
        Prints out possible results and prompts user for confirmation. If confirmed, prints out and returns
        full decrypted message, otherwise returns None.

    """
    print('Hacking...')

    # Python programs can be stopped at any time by pressing
    # Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux):
    print('(Press Ctl-C (on Windows) or Ctrl-D (on macOS and Linux) to quit at any time.)')

    # Brute-force by looping through every possible key:
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = decryptMessage(key, message)

        if isEnglish(decryptedText):
            # Ask user if this is the correct decryption:
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None


if __name__ == '__main__':
    main()
