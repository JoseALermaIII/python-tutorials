"""Chapter 7 Practice Question 3

What value does each of the following expressions evaluate to?

Note:
    aka "The power of lists"
"""


def main():
    print([0, 1, 2, 3, 4][2])
    print([[1, 2], [3, 4]][0])
    print([[1, 2], [3, 4]][0][1])
    print(['hello'][0][1])
    print([2, 4, 6, 8, 10][1:3])
    print(list('Hello world!'))  # Nifty?
    print(list(range(10))[2])  # Huh
    print(list(range(10)))  # Oh, okay (added for clarity)


# If Question3.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
