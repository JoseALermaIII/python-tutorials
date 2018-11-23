""" Chapter 5 Practice Question 1

Using caesarCipher.py, encrypt the following sentences with the given keys.

Note:
    Contains spoilers for Chapter 7 (functions)
"""

from books.CrackingCodesWithPython.Chapter01.caesarCipher import caesarCipher


def main():
    messages = ["'You can show black is white by argument,' said Filby, 'but you will never convince me.'",
                "1234567890", "I'm not crazy, I'm just a little unwell"]
    keys = [8, 21, 6]

    for index in range(len(keys)):
        print(caesarCipher(keys[index], messages[index], "encrypt"))

    return None


if __name__ == "__main__":
    main()
