# Chapter 20 Practice Questions


def main():
    # 1. What is a dictionary attack?
    # Hint: Check page 279
    from books.CrackingCodesWithPython.Chapter20.vigenereDictionaryHacker import hackVigenereDictionary
    answer = "A ukuvo-fhkcg wemaof esbgg gfekr wqbd bg tjo dbvtkyntky cc a dxy."
    print(hackVigenereDictionary(answer))

    # 2. What does Kasiski examination of a ciphertext reveal?
    # Hint: Check page 282
    # Don't do this - imports should be at the top of the file
    from books.CrackingCodesWithPython.Chapter20.vigenereHacker import hackVigenere
    answer = "Uakqkuq oxsuaxidigv ac i zrgkwca dhsb oo kkn maw dw nelmjwqxe lpw vmxglp gp bre Nqyovorw swi ccev bg ovmrqxl k kspzmjdmht. Om ukv dhwv mcm prwymovmy svsvgcik bg lzoac msmp yf lpw cclkwgk svnehmfnmxtdg."
    print(hackVigenere(answer))

    # 3. What two changes happen when converting a list value to a set value
    #    with the set() function?
    # Hint: Check page 298, but you'll need to go to the website for the second change
    answer = "Vyidmvsxx neemil svx jifgzxv egv xaw skvik gj mzi ospnww bk phkx (nfpbci eawmk, ztdyxk mg kimk hh fsm zeow eg gvwwv)"
    print(hackVigenereDictionary(answer))

    # 4. If the spam variable contains ['cat', 'dog', 'mouse', 'dog'], this
    #    list has four items in it. How many items does the list returned from
    #    list(set(spam)) have?
    # Hint: Check page 298
    spam = ['cat', 'dog', 'mouse', 'dog']
    spam = list(set(spam))
    print("Spam contains %s and has %s items." % (spam, len(spam)))

    # 5. What does the following code print?
    # Hint: Check page 306
    print('Hello', end='')
    print('World')


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
