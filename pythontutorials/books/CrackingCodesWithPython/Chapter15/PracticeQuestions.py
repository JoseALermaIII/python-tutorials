"""Chapter 15 Practice Questions

Answers Chapter 15 Practice Questions via Python code.
"""


def main():
    # 1. What does 2 ** 5 evaluate to?
    print(2 ** 5)

    # 2. What does 6 ** 2 evaluate to?
    print(6 ** 2)

    # 3. What does the following code print?
    for i in range(5):
        if i == 2:
            continue
        print(i)

    # 4. Does the main() function of affineHacker.py get called if another program
    #    runs import affineHacker?
    # Hint: check page 204

    # Don't do this - imports should be at the top of the file.
    import pythontutorials.books.CrackingCodesWithPython.Chapter15.affineHacker as affineHacker

    affineHacker.hackAffine("Well, I can't figure out just two! So let's pretend you opened 200.")


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
