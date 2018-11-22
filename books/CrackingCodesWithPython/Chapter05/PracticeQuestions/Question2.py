# Using caesarCipher.py, decrypt the following ciphertexts with the given keys
# SPOILERS for chapter 7 (functions)

import books.CrackingCodesWithPython.Chapter05.PracticeQuestions.Question1 as Question1


def main():
    ciphertexts = ["Kv?uqwpfu?rncwukdng?gpqwijB",
                   "XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V",
                   "O'sCtuzCixg65,CO'sCp1yzCgCrozzrkC1t3krr"]
    keys = [2, 22, 6]

    for index in range(len(keys)):
        print(Question1.caesarCipher(keys[index], ciphertexts[index], "decrypt"))


# If Question2.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
