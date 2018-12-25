"""Debug coin toss

This program is a simple coin toss guessing game. The player gets two guesses.

"""


def main():
    import random
    guess = ''
    options = ("tails", "heads")
    while guess not in options:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input().lower()

    toss = options[random.randint(0, 1)]  # 0 is tails, 1 is heads

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input().lower()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if __name__ == '__main__':
    main()
