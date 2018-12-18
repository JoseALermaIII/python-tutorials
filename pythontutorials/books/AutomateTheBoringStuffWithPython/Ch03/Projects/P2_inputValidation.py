"""Input validation

This program adds input validation to :py:mod:`.P01_make_collatz_seq`

Add try and except statements to the previous project to detect whether
the user types in a noninteger string. Normally, the :obj:`int` function will
raise a :class:`ValueError` error if it is passed a noninteger string, as in `int('puppy')`.
In the except clause, print a message to the user saying they must enter an integer.


"""


def main():
    from .P1_makeCollatzSeq import collatz

    try:
        n = int(input("Input a number: "))
        while n != 1:
            print(n)
            n = collatz(n)
        print(n)  # When n == 1
    except ValueError:
        print("Error: Input must be an integer.")


if __name__ == "__main__":
    main()
