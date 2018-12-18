"""Magic 8 ball

This program answers your questions with a function that knows all.

"""


def getAnswer(answerNumber: int) -> str:
    """Get answer

    Uses `if` ... `elif` sequence to return a response based on an inputted number.

    Args:
        answerNumber: Any integer between 1 and 9.

    Returns:
        String containing a response based on the given number.
    """
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


def main():
    import random
    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)  # equivalent: print(getAnswer(random.randint(1, 9)))


if __name__ == '__main__':
    main()
