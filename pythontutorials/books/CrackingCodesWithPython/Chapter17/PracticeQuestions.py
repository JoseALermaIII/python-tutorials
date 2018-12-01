"""Chapter 17 Practice Questions

Answers Chapter 17 Practice Questions via Python code.
"""


def main():
    # 1. What is the word pattern for the word hello?
    from pythontutorials.books.CrackingCodesWithPython.Chapter17.makeWordPatterns import getWordPattern

    wordPat = getWordPattern('hello')
    print(wordPat)

    # 2. Do mammoth and goggles have the same word pattern?
    wordPat1 = getWordPattern('mammoth')
    wordPat2 = getWordPattern('goggles')

    if wordPat1 == wordPat2:
        print("Yes: " + wordPat1)
    else:
        print("No: " + wordPat1 + " and " + wordPat2)

    # 3. Which word could be the possible plaintext word for the cipherword
    #    PYYACAO? Alleged, efficiently, or poodle?
    wordPat = []
    words = ["PYYACAO", "Alleged", "efficiently", "poodle"]
    for word in words:
        wordPat.append(getWordPattern(word))

    for index in range(1, len(wordPat)):
        if wordPat[0] == wordPat[index]:
            print("It's gotta be %s!" % words[index])
            break
        elif index == len(wordPat) - 1:
            print("Match not found (-_-)")


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
