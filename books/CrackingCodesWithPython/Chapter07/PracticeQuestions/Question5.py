"""Chapter 7 Practice Question 5

What are the four augmented assignment operators?

Note:
    Hint: Table 7-1 on pg 92
"""


def main():
    word = "Bo"
    number = 42

    word += "Bo"
    print(word)

    number -= 2
    print(number)

    word *= 10
    print(word)

    number /= 4
    print(number)


# If Question5.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
