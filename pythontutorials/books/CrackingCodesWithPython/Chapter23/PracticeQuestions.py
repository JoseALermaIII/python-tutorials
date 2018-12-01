"""Chapter 23 Practice Questions

Answers Chapter 23 Practice Questions via Python code.
"""


def main():
    # 1. What is the difference between a symmetric cipher and an asymmetric
    #    cipher?
    # Hint: Check page 336
    message = ".noitpyrced dna noitpyrcne rof yek emas eht esu taht srehpiC :cirtemmyS"
    message2 = ".noitpyrced rof rehtona dna noitpyrcne rof yek eno esu taht srehpiC :cirtemmysA"
    #print(blank[::-1])  # Fill in the blank
    #print(blank[::-1])

    # 2. Alice generates a public key and a private key. Unfortunately, she later
    #    loses her private key.
    #    a.  Will other people be able to send her encrypted messages?
    #    b.  Will she be able to decrypt messages previously sent to her?
    #    c.  Will she be able to digitally sign documents?
    #    d.  Will other people be able to verify her previously signed documents?
    # Hint: Check pages 336 and 338 - 339
    yesno = ["Yes", "No"]
    print("a.: %s" % yesno[8 * 0 + 4 * 5 * 0])
    print("b.: %s" % yesno[3 + 7 - 6 - 3])
    print("c.: %s" % yesno[10 * 10 // 50 - 1])
    print("d.: %s" % yesno[100 // 25 + 6 - 5 * 2])

    # 3. What are authentication and confidentiality? How are they different?
    # Hint: Check page 338
    # Don't do this - imports should be at the top of the file
    import pythontutorials.books.CrackingCodesWithPython.Chapter01.caesarCipher
    message = "L65spy5tnl5tzy:H13zzqH5sl5H8szH0z6'3pHnzxx6ytnl5tyrH8t5sHt4H8szH5sp0H4l0H5sp0Hl3pK"  # Key 11
    message2 = "O1zrupqz6umxu6 :Iwqq2uzsI6tqIyq55msqImI5qo4q6L"  # Key 12
    diff = "X99Tz6?52ABT6 TC52Ty!!8T?A!E612Tz! 3612 C6x96CH,TyDCTxDC52 C6zxC6! T6BT3A2.D2 C9HTyxB21T! TF5!T5xBTC52TA645CT82HW"  # Key 23
    #print(books.CrackingCodesWithPython.Chapter01.caesarCipher.decryptMessage(blank, blank))  # Fill in the blanks
    #print(books.CrackingCodesWithPython.Chapter01.caesarCipher.decryptMessage(blank, blank))
    #print(books.CrackingCodesWithPython.Chapter01.caesarCipher.decryptMessage(blank, blank))

    # 4. What is non-repudiation?
    # Hint: Check page 339
    # Don't do this - imports should be at the top of the file
    import pythontutorials.books.CrackingCodesWithPython.Chapter20.vigenereDictionaryHacker
    message = "Klt axirtvhrv xwuw aofmcav awi kis tchufvtx d uelaotv adh'w je tjzr ks syqg anbvbimca wpam usfjevy db a eihri xxgh."
    #print(books.CrackingCodesWithPython.Chapter20.vigenereDictionaryHacker.hackVigenereDictionary(blank))  # Fill in the blank


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
