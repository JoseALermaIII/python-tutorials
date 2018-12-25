"""Coin flip

This program simulates flipping a coin 1000 times and prints the number
of times it landed on heads.
"""


def main():
    import random
    heads = 0
    for i in range(1, 1001):
        if random.randint(0, 1) == 1:
            heads += 1
        if i == 500:
            print("Halfway done!")
    print("Heads came up " + str(heads) + " times.")


if __name__ == '__main__':
    main()
