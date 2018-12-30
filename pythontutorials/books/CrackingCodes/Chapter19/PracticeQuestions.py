"""Chapter 19 Practice Questions

Answers Chapter 19 Practice Questions via Python code.
"""


def main():
    # 1. What is frequency analysis?
    # Hint: Check page 259
    from pythontutorials.books.CrackingCodes.Chapter18.vigenereCipher import decryptMessage
    # Encrypted with key "ANALYSIS"
    message = "Tue apgkwsf oq bwbwrziygfo zoj fccicwnglj y dmltrr lnhmsrf iy ndiangeirk ifd vn nghpwrgeirk."
    #print(decryptMessage(blank, blank))  # Fill in the blanks

    # 2. What are the six most commonly used letters in English?
    # Hint: Check page 260
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    INDEX = [4, -7, 0, -12]
    answer = []
    for item in INDEX:
        answer.append(LETTERS[item])
    #print(''.join(answer))  # Uncomment it if you got it

    # 3. What does the spam variable contain after you run the following code?
    spam = [4, 6, 2, 8]
    spam.sort(reverse=True)
    print(spam)

    # 4. If the spam variable contains a dictionary, how can you get a list value of
    #    the keys in the dictionary?
    # Hint: Check page 274
    message = "dxsf(keay.ctye())"  # Encrypted with "SPAM"
    #print(decryptMessage(blank, blank))  # Fill in the blanks


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
