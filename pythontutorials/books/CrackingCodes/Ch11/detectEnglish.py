"""Detect English Module

Provides functions to determine whether a given string is in the English language.

Attributes:
    UPPERLETTERS (str): String containing all latin-based letters in uppercase.
    LETTERS_AND_SPACE (str): String containing upper and lowercase letters as well as space, newline, and tab.
    DICTIONARY_FILE (str): String containing absolute path of dictionary.txt file.
    ENGLISH_WORDS (dict): Dictionary containing all words from dictionary.txt as keys.

Example:
    >>> import pythontutorials.books.CrackingCodes.Ch11.detectEnglish as detectEnglish
    >>> someString = 'Enthusiasm is contagious. Not having enthusiasm is also contagious.'
    >>> detectEnglish.isEnglish(someString)  # Returns True or False
    True

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
    * There must be a "dictionary.txt" file in this directory with all
      English words in it, one word per line. You can download this from
      https://www.nostarch.com/crackingcodes/.
"""

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
DICTIONARY_FILE = '/home/jose/PycharmProjects/python-tutorials/pythontutorials/books/CrackingCodes/Ch11/dictionary.txt'


def loadDictionary() -> dict:
    """Load dictionary file

    Loads dictionary.txt file and creates a dictionary with all words as keys.

    Returns:
        Dictionary with all words in dictionary.txt as keys.
    """
    dictionaryFile = open(DICTIONARY_FILE)
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message: str) -> float:
    """Get count of English words

    For given message, counts number of words in English
    dictionary and returns ratio of English words out of total words.

    Args:
        message: String with message to check for English words.

    Returns:
         Ratio of number of English words / total number of words.
    """
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if not possibleWords:  # Given [] = False, if possibleWords = [] then if not possibleWords = True
        return 0.0  # No words at all, so return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message: str) -> str:
    """Removes non-letters

    Removes non-letter characters from given message.

    Args:
        message: String with message to remove non-letter characters from.

    Returns:
        New string with non-letter characters removed.
    """
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message: str, wordPercentage: int=20, letterPercentage: int=85) -> bool:
    """Determines whether message is English

    Using given word percentage and letter percentage, determines if a given message is in the English language.

    Args:
        message: String containing message to determine if it is English.
        wordPercentage: Integer representing percentage of words in message that must be English.
        letterPercentage: Integer representing percentage of characters in message that must be letters or spaces.

    Returns:
        True if message is in English language, False otherwise.

    Note:
        * By default, 20% of the words must exist in the dictionary file, and
          85% of all the characters in the message must be letters or spaces
          (not punctuation or numbers).
    """
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
