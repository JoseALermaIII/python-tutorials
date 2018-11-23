"""Chapter 1 Practice Questions.

Answers Chapter 1 Practice Questions via Python code.

Note:
    Contains spoilers from Chapter 5 (caesar cipher), Chapter 6 (caesar hacker), and Chapter 7 (functions)
    Corrections submitted for Questions 1, 3, 4, and 5
"""


def main():
    from books.CrackingCodesWithPython.Chapter01.caesarCipher import decryptMessage, encryptMessage
    from books.CrackingCodesWithPython.Chapter01.caesarHacker import hackCaesar
    import books.CrackingCodesWithPython.Chapter01.config

    # Every possible symbol that can be encrypted (if encrypting by hand):
    books.CrackingCodesWithPython.Chapter01.config.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 1. Encrypt the following entries from Ambrose Bierce's The Devil's Dictionary
    #    with the given keys:
    messages = ["AMBIDEXTROUS: ABLE TO PICK WITH EQUAL SKILL A RIGHT-HAND POCKET OR A LEFT.",
                "GUILLOTINE: A MACHINE WHICH MAKES A FRENCHMAN SHRUG HIS SHOULDERS WITH GOOD REASON.",
                "IMPIETY: YOUR IRREVERENCE TOWARD MY DEITY."]
    keys = [4, 17, 21]

    for index in range(len(keys)):
        print(encryptMessage(keys[index], messages[index]))

    # 2. Decrypt the following ciphertexts with the given keys:
    messages = ["ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTC XC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS.",
                "MQTSWXSV: E VMZEP EWTMVERX XS TYFPMG LSRSVW."]
    keys = [15, 4]

    for index in range(len(keys)):
        print(decryptMessage(keys[index], messages[index]))

    # 3. Encrypt the following sentence with the key 0:
    message = "THIS IS A SILLY EXAMPLE."
    print(encryptMessage(0, message))

    # 4. Here are some words and their encryptions. Which key was used for each word?
    print("\nHacking 'LIMYVOX':")
    hackCaesar("LIMYVOX")
    print("\nHacking 'PRDRDFKF':")
    hackCaesar("PRDRDFKF")
    print("\nHacking 'HZAYVUVTF':")
    hackCaesar("HZAYVUVTF")

    # 5. What does this sentence encrypted with key 8 decrypt to with key 9?
    print("\nHacking 'UMMSVMAA: CVKWUUWV XIBQMVKM QV XTIVVQVO I ZMDMVOM BPIB QA EWZBP EPQTM.':")
    hackCaesar("UMMSVMAA: CVKWUUWV XIBQMVKM QV XTIVVQVO I ZMDMVOM BPIB QA EWZBP EPQTM.")


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
