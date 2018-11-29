"""Frequency Finder

Analyzes frequency of letters in given message compared to the most common occurring
letters to determine if message is in the English language.

Attributes:
    ETAOIN (str): String containing uppercase latin letters in order from most to least common.
    LETTERS (str): String containing uppercase latin letters in alphabetical order.

Note:
    * Compares six most and six least common letters in the English language.
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getLetterCount(message: str) -> dict:
    """Get letter count

    Counts the frequency of all latin letters in a given message.

    Args:
        message: String containing message to analyze letter frequency.

    Returns:
        Dictionary with keys of single letters and values of the count of how many
        times they appear in the message parameter.
    """
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                   'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                   'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                   'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def getItemAtIndexZero(items: tuple):
    """Get element at index zero

    Helper function that returns the first element of a given tuple.

    Args:
        items: Tuple containing a latin letter and its frequency count.

    Returns:
        The first element of the given tuple: the latin letter.
    """
    return items[0]


def getFrequencyOrder(message: str) -> str:
    """Get frequency order

    Analyzes frequency of each letter in given message and returns string with each letter from most to least frequent.

    Args:
         message: String containing message to analyze frequency.

    Returns:
        String of the alphabet letters arranged in order of most frequently occurring in the message parameter.
    """

    # First, get a dictionary of each letter and its frequency count:
    letterToFreq = getLetterCount(message)

    # Second, make a dictionary of each frequency count to the letter(s)
    # with that frequency:
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # Third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string:
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # Fourth, convert the freqToLetter dictionary to a list of
    # tuple pairs (key, value), and then sort them:
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # Fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string:
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def englishFreqMatchScore(message: str) -> int:
    """English Frequency Match Score

    Calculates number of matches that the string in the message parameter has when its letter frequency is
    compared to English letter frequency.

    Args:
         message: String containing message to calculate English match score.

    Returns:
        Number representing message's matches to English letter frequency.

    Note:
        * A "match" is how many of its six most frequent and six least frequent letters are among the six
          most frequent and six least frequent letters for English.
        * A "perfect score" is 12

    """
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # Find how many matches for the six most common letters there are:
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # Find how many matches for the six least common letters there are:
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore
