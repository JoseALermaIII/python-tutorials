"""Make wordPatterns.py file

Creates wordPatterns.py based on the words in our dictionary text file, dictionary.txt.
A word pattern assigns a number to each letter in a word, then generates a pattern representation of that word
based on the number assigned to each letter.

Attributes:
    DICTIONARY_FILE (str): String containing absolute path to dictionary.txt file.

Note:
    * Download the dictionary file from https://invpy.com/dictionary.txt
    * https://www.nostarch.com/crackingcodes (BSD Licensed)
"""

import pprint

DICTIONARY_FILE = '/home/jose/PycharmProjects/python-tutorials/books/CrackingCodesWithPython/Chapter11/dictionary.txt'


def getWordPattern(word: str) -> str:
    """Get word pattern

    Returns a string of the pattern form of the given word.

    Args:
        word: String containing word to convert into word pattern.

    Example:
    >>> import books.CrackingCodesWithPython.Chapter17.makeWordPatterns as makeWordPatterns
    >>> makeWordPatterns.getWordPattern('DUSTBUSTER')
    '0.1.2.3.4.1.2.3.5.6'

    Returns:
        String containing word pattern.
    """
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


def main():
    allPatterns = {}

    fo = open(DICTIONARY_FILE)
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        # Get the pattern for each string in wordList:
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement:
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    main()
