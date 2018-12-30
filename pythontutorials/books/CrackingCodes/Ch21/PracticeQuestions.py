"""Chapter 21 Practice Questions

Answers Chapter 21 Practice Questions via Python code.
"""

from pythontutorials.books.CrackingCodes.Ch18.vigenereCipher import decryptMessage


def main():
    # 1. Why isn't a one-time pad program presented in this chapter?
    # Hint: Check page 315
    message = "Pxronhs mws hcs-mxax eow rwiwsk xg mws lpax pg mws Oxuxcskt Qbevxg!"  # Encrypted with key "OTP"
    #print(decryptMessage(blank, blank))  # Fill in the blanks

    # 2. Which cipher is the two-time pad equivalent to?
    # Hint: Check page 319
    message = "Mat mpd-mbbx ipw bh xjjbopexcm md mat Obvxgtkx Rbiwxk!"  # Encrypted with key "TTP"
    #print(decryptMessage(blank, blank))  # Fill in the blanks

    # 3. Would using a key twice as long as the plaintext message make the one-
    #    time pad twice as secure?
    # Hint: Check page 317, but a more specific explanation is on the website
    message = "Xs, zpgnall dlc cifz zvow syyfkw. Pd mq uyfz tz ciafvr."  # Encrypted with key "KEYLENGTH"
    #print(decryptMessage(blank, blank))  # Fill in the blanks


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
