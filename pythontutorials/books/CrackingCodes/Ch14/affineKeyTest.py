"""Test affine cipher keyspace

This program proves that the keyspace of the affine cipher is limited to less than len(SYMBOLS) ^ 2.

Note:
    Tests every key from 2 through 80 and prints it with the encrypted message if the key and
    length of SYMBOLS have a gcd.
"""

from pythontutorials.books.CrackingCodes.Ch14.affineCipher import encryptMessage, SYMBOLS
from pythontutorials.books.CrackingCodes.Ch13.cryptomath import gcd


def main():
    message = 'Make things as simple as possible, but not simpler.'
    for keyA in range(2, 80):
        key = keyA * len(SYMBOLS) + 1

        if gcd(keyA, len(SYMBOLS)) == 1:
            print(keyA, encryptMessage(key, message))


if __name__ == '__main__':
    main()
