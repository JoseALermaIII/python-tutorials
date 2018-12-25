"""Simple Substitution Cipher Hacker

Implements a function that can hack a substitution cipher encrypted message.

Attributes:
    LETTERS (str): String containing uppercase latin letters.
    nonLettersOrSpacePattern (re._sre.SRE_Pattern): Regular expression object representing all non-letter
        characters and space.

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)

"""

import re
import copy
from pythontutorials.books.CrackingCodesWithPython.Chapter16.simpleSubCipher import decryptMessage
from pythontutorials.books.CrackingCodesWithPython.Chapter17.wordPatterns import allPatterns
from pythontutorials.books.CrackingCodesWithPython.Chapter17.makeWordPatterns import getWordPattern


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')


def main():
    import pyperclip

    message = """Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr
sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa
sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac
ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx
lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia
rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh.
-Facjclxo Ctrramm"""

    # Determine the possible valid ciphertext translations:
    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user:
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping() -> dict:
    """Get blank cipherletter mapping

    Returns a dictionary value that is a blank cipherletter mapping

    Returns:
         Returns dictionary with uppercase latin letters as keys and empty lists as values.
    """
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
            'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
            'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
            'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping: dict, cipherword: str, candidate: str) -> None:
    """Add letters to cipherletter mapping

    The letterMapping parameter takes a dictionary value that
    stores a cipherletter mapping, which is copied by the function.
    The cipherword parameter is a string value of the ciphertext word.
    The candidate parameter is a possible English word that the
    cipherword could decrypt to.

    This function adds the letters in the candidate as potential
    decryption letters for the cipherletters in the cipherletter
    mapping.

    Args:
        letterMapping: Dictionary containing a cipherletter mapping.
        cipherword: String containing an encrypted ciphertext word.
        candidate: String containing an English word the cipherword could potentially decrypt to.

    Return:
        None. Modifies contents of letterMapping by adding letters to the cipherletter mapping.
    """
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])


def intersectMappings(mapA: dict, mapB: dict) -> dict:
    """Intersects two cipherletter mappings

    Checks each letter in LETTERS and adds to intersected map if it exists in both given maps.
    If either map is empty, the non-empty map is copied to the intersected map.

    Args:
        mapA: Dictionary containing potential decryption letters.
        mapB: Dictionary containing potential decryption letters.

    Returns:
        Dictionary containing intersected map of potential decryption letters.

    """
    # To intersect two maps, create a blank map and then add only the
    # potential decryption letters if they exist in BOTH maps:
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely:
        if not mapA[letter]:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif not mapB[letter]:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter],
            # add that letter to intersectedMapping[letter]:
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping: dict) -> dict:
    """Removes solved letters from cipherletter mapping

    Cipherletters in the mapping that map to only one letter are
    "solved" and can be removed from the other letters.

    For example, if 'A' maps to potential letters ['M', 'N'] and 'B'
    maps to ['N'], then we know that 'B' must map to 'N', so we can
    remove 'N' from the list of what 'A' could map to. So 'A' then maps
    to ['M'].

    Note that now that 'A' maps to only one letter, we can
    remove 'M' from the list of letters for every other letter.
    (This is why there is a loop that keeps reducing the map.)

    Args:
        letterMapping: Cipherletter map dictionary to remove solved letters from.

    Returns:
        Dictionary containing cipherletter map with solved letters removed.

    """

    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # solvedLetters will be a list of uppercase letters that have one
        # and only one possible mapping in letterMapping:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, then it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
                for s in solvedLetters:
                    if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                        letterMapping[cipherletter].remove(s)
                        if len(letterMapping[cipherletter]) == 1:
                            # A new letter is now solved, so loop again:
                            loopAgain = True
    return letterMapping


def hackSimpleSub(message: str) -> dict:
    """Hack simple substitution cipher

    Hacks simple substitution cipher and returns dictionary with cipherletter map that may be able
    to decrypt given message.

    Args:
        message: String containing substitution cipher encrypted message.

    Returns:
        Dictionary with cipherletter map that may decrypt given message.

    """
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word:
        candidateMap = getBlankCipherletterMapping()

        wordPattern = getWordPattern(cipherword)
        if wordPattern not in allPatterns:
            continue  # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping:
        for candidate in allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext: str, letterMapping: dict) -> str:
    """Decrypt substitution cipher message with cipherletter map

    Decrypts given substitution cipher encrypted message with given dictionary containing a
    cipherletter map.

    Args:
        ciphertext: Substitution cipher encrypted message to decrypt.
        letterMapping: Dictionary with cipherletter map that may decrypt the ciphertext.

    Returns:
        String containing decrypted ciphertext message.

    Note:
        * Ambiguous decrypted letters are replaced with an underscore, '_'

    """
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key:
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()
