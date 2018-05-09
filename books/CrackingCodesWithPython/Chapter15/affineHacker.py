# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

from books.CrackingCodesWithPython.pyperclip import copy
from books.CrackingCodesWithPython.Chapter14.affineCipher import decryptMessage, SYMBOLS, getKeyParts
from books.CrackingCodesWithPython.Chapter13.cryptomath import gcd
from books.CrackingCodesWithPython.Chapter11.detectEnglish import isEnglish

SILENT_MODE = False


def main():
    # You might want to copy & paste this text from the source code at
    # https://www.nostarch.com/crackingcodes/.
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQ
ADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage is not None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on macOS and Linux):
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key:
    for key in range(len(SYMBOLS) ** 2):
        keyA = getKeyParts(key)[0]
        if gcd(keyA, len(SYMBOLS)) != 1:
            continue

        decryptedText = decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found:
            print()
            print('Possible encryption hack:')
            print('Key: %s' % key)
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If affineHacker.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
