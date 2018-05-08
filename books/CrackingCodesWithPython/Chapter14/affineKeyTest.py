# This program proves that the keyspace of the affine cipher is limited
# to less than len(SYMBOLS) ^ 2.

from books.CrackingCodesWithPython.Chapter14.affineCipher import encryptMessage, SYMBOLS
from books.CrackingCodesWithPython.Chapter13.cryptomath import gcd

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 80):
    key = keyA * len(SYMBOLS) + 1

    if gcd(keyA, len(SYMBOLS)) == 1:
        print(keyA, encryptMessage(key, message))
