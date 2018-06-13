# This program makes a Collatz Sequence for a given number

# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps calling
# collatz() on that number until the function returns the value 1.

# Sample output:
# Enter number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1


def collatz(number):
    if not number % 2:
        return number // 2
    else:
        return 3 * number + 1


def main():
    n = int(input("Input a number: "))
    while n != 1:
        print(n)
        n = collatz(n)
    print(n)  # When n == 1


# If program is run (instead of imported), call main():
if __name__ == "__main__":
    main()
