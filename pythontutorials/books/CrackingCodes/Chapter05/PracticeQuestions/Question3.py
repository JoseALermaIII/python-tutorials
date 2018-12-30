""" Chapter 5 Practice Question 3

Which Python instruction would import a module named watermelon.py?

Note:
    Contains spoilers for Chapter 7 (functions)
"""

import pythontutorials.books.CrackingCodes.Chapter05.PracticeQuestions.watermelon as watermelon


def main():
    watermelon.nutrition()


# If Question3.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
