"""Chapter 13 Practice Questions

Answers Chapter 13 Practice Questions via Python code.
"""


def main():
    # 1. What do the following expressions evaluate to?
    print(17 % 1000)
    print(5 % 5)

    # 2. What is the GCD of 10 and 15?
    # Don't do this - imports should be at the top of the file
    from pythontutorials.books.CrackingCodes.Chapter13.cryptomath import gcd
    print(gcd(10, 15))

    # 3. What does spam contain after executing spam, eggs = 'hello', 'world'?
    spam, eggs = 'hello', 'world'
    print(spam)

    # 4. The GCD of 17 and 31 is 1. Are 17 and 31 relatively prime?
    if not gcd(17, 31) == 1:
        print("No")
    else:
        print("Yes")

    # 5. Why aren't 6 and 8 relatively prime?
    print(gcd(6, 8))

    # 6. What is the formula for the modular inverse of A mod C?
    # Hint: check page 183
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    print("The modular inverse of %s mod %s is number %s such that (%s * %s) mod %s == %s" %
          (SYMBOLS[0], SYMBOLS[2], SYMBOLS[34], SYMBOLS[0], SYMBOLS[34], SYMBOLS[2], SYMBOLS[-14]))


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
