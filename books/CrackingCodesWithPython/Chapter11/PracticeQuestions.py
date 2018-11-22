# Chapter 11 Practice Questions


def main():
    # 1. What does the following code print?
    spam = {'name': 'Al'}
    print(spam['name'])

    # 2. What does this code print?
    spam = {'eggs': 'bacon'}
    print('bacon' in spam)

    # 3. What for loop code would print the values in the following spam
    #    dictionary?
    spam = {'name': 'Zophie', 'species': 'cat', 'age': 8}

    for key in spam:
        print(spam[key])

    # 4. What does the following line print?
    print('Hello, world!'.split())

    # 5. What will the following code print?
    def spam(eggs=42):
        print(eggs)

    spam()
    spam('Hello')

    # 6. What percentage of words in this sentence are valid English words?
    sentence = "Whether it's flobulllar in the mind to quarfalog the slings and arrows of outrageous guuuuuuuuur."

    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

    def loadDictionary():
        dictionaryFile = open('dictionary.txt')
        englishWords = {}
        for word in dictionaryFile.read().split('\n'):
            englishWords[word] = None
        dictionaryFile.close()
        return englishWords

    ENGLISH_WORDS = loadDictionary()
    #  Not in dictionary. Too small?
    ENGLISH_WORDS['IN'] = None
    ENGLISH_WORDS['TO'] = None
    ENGLISH_WORDS['OF'] = None

    def getEnglishCount(message):
        message = message.upper()
        message = removeNonLetters(message)
        possibleWords = message.split()

        if not possibleWords:  # Given [] = False, if possibleWords = [] then if not possibleWords = True
            return 0.0  # No words at all, so return 0.0

        matches = 0
        for word in possibleWords:
            if word in ENGLISH_WORDS:
                matches += 1
        print(matches, possibleWords)
        return float(matches) / len(possibleWords)

    def removeNonLetters(message):
        lettersOnly = []
        for symbol in message:
            if symbol in LETTERS_AND_SPACE:
                lettersOnly.append(symbol)
        return ''.join(lettersOnly)

    print(getEnglishCount(sentence) * 100)


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
