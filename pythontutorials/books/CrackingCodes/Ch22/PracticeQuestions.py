"""Chapter 22 Practice Questions

Answers Chapter 22 Practice Questions via Python code.
"""

from pythontutorials.books.CrackingCodes.Ch18.vigenereCipher import decryptMessage


def main():
    # 1. How many prime numbers are there?
    # Hint: Check page 322
    message = "Iymdi ah rv urxxeqfi fjdjqv gu gzuqw clunijh."  # Encrypted with key "PRIMES"
    #print(decryptMessage(blank, blank))  # Fill in the blanks

    # 2. What are integers that are not prime called?
    # Hint: Check page 323
    message = "Vbmggpcw wlvx njr bhv pctqh emi psyzxf czxtrwdxr fhaugrd."  # Encrypted with key "NOTCALLEDEVENS"
    #print(decryptMessage(blank, blank))  # Fill in the blanks

    # 3. What are two algorithms for finding prime numbers?
    # Hint: Check page 323
    # Encrypted with key "ALGORITHMS"
    message = "Tsk hyzxl mdgzxwkpfz gkeo ob kpbz ngov gfv: bkpmd dtbwjqhu, eaegk cw Mkhfgsenseml, hzv Rlhwe-Ubsxwr."
    #print(decryptMessage(blank, blank))  # Fill in the blanks


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
