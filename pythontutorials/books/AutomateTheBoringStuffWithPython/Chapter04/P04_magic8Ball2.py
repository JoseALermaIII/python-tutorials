"""Magic 8 Ball 2.0

This program more efficiently answers your questions by indexing a
list with the answer strings.

"""


def main():
    import random

    messages = ['It is certain',
                'It is decidedly so',
                'Yes definitely',
                'Reply hazy try again',
                'Ask again later',
                'Concentrate and ask again',
                'My reply is no',
                'Outlook not so good',
                'Very doubtful']

    print(messages[random.randint(0, len(messages) - 1)])


if __name__ == "__main__":
    main()
