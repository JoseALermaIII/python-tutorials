"""Factorial log

This program calculates factorial and logs debug messages.

"""

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # log to terminal
#logging.basicConfig(filename="factorialLog.txt", level=logging.DEBUG,
#                    format=" %(asctime)s - %(levelname)s - %(message)s")  # optional log to file
logging.disable(logging.CRITICAL)  # Stop logging, comment out to debug


def factorial(n: int) -> int:
    """Factorial

    Calculates factorial of given number.

    Args:
        n: Integer number to calculate factorial.

    Returns:
        Factorial of given number.
    """
    logging.debug("Start of factorial(%s%%)" % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug("End of factorial(%s%%)" % n)
    return total


def main():
    logging.debug("Start of program")
    print(factorial(5))
    logging.debug("End of program")


if __name__ == '__main__':
    main()
