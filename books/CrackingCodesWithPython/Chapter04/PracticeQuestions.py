# Chapter 4 Practice Questions


def main():
    # 1. What does the following piece of code print to the screen?
    print(len("Hello") + len("Hello"))

    # 2. What does this code print?
    i = 0
    while i < 3:
        print("Hello")
        i = i + 1

    # 3. How about this code?
    i = 0
    spam = "Hello"
    while i < 5:
        spam = spam + spam[i]
        i = i + 1
    print(spam)

    # 4. And this?
    i = 0
    while i < 4:
        while i < 6:
            i = i + 2
            print(i)


# If PracticeQuestions.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
