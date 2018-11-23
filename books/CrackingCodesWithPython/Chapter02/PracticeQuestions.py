"""Chapter 2 Practice Questions

Answers Chapter 2 Practice Questions via Python code.

Note:
    To check these questions, they should be entered in IDLE; otherwise print statements would be needed.
"""


def main():
    # 1. Which is the operator for division, / or \?
    # Uncomment lines to test
    # 4 / 2
    # 4 \ 2

    # 2. Which of the following is an integer value, and which is a floating-point value?
    type(42)
    type(3.141592)

    # 3. Which of the following lines are not expressions?
    # Uncomment lines to test
    # 4 x 10 + 2
    # 3 * 7 + 1
    # 2 +
    # 42
    # 2 + 2
    # spam = 42

    # 4. If you enter the following lines of code into the interactive shell, what do
    #    lines (1) and (2) print?

    spam = 20
    spam + 20  # (1)
    SPAM = 30
    spam  # (2)


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
