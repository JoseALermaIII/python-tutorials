"""Chapter 7 Practice Question 1

Encrypt the following with the transposition cipher (with paper and pencil, *cough*).

Note:
    Contains spoilers for Chapter 9 (importing transpositionEncrypt)
"""

from books.CrackingCodesWithPython.Chapter07.transpositionEncrypt import encryptMessage


def main():
    key = 9
    message1 = "Underneath a huge oak tree there was of swine a huge company,"
    message2 = "That grunted as they crunched the mast: For that was ripe and fell full fast."
    message3 = "Then they trotted away for the wind grew high: One acorn they left, and no more might you spy."

    print("%s| Len: %s" % (encryptMessage(key, message1), len(message1)))
    print("%s| Len: %s" % (encryptMessage(key, message2), len(message2)))
    print("%s| Len: %s" % (encryptMessage(key, message3), len(message3)))


# If Question1.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
