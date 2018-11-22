# Chapter 3 Practice Questions


def main():
    spam = "Cats"
    # 1. If you assign spam = "Cats", what do the following lines print?
    print(spam + spam + spam)
    print(spam * 3)

    # 2. What do the following lines print?
    print("Dear Alice, \nHow are you?\nSincerely,\nBob")
    print("Hello" + "Hello")

    spam = "Four score and seven years is eighty seven years."
    # 3. If you assign spam = "Four score and seven years is eighty seven years.",
    #    what would each of the following lines print?
    print(spam[5])
    print(spam[-3])
    print(spam[0:4] + spam[5])
    print(spam[-3:-1])
    print(spam[:10])
    print(spam[-5:])
    print(spam[:])

    # 4. Which window displays the >>> prompt, the interactive shell or the file editor?
    # Hint: Check page 30
    answers = ["interactive shell", "file editor"]
    print("The window that displays the >>> prompt is the %s." % answers[-2 + 5 * 7 * 9 * 0])

    # 5. What does the following line print?

    #print("Hello, world!")


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
