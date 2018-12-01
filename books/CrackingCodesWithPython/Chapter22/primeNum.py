"""Prime Number Sieve

Implements a series of functions that determine if a given number is prime.

Attributes:
    LOW_PRIMES (list): List containing prime numbers <= 100 (aka 'low primes').

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)

"""

import math, random


def isPrimeTrialDiv(num: int) -> bool:
    """Is prime trial division

    Uses the `trial division`_ algorithm for testing if a given number is prime.

    Args:
         num: Integer to determine if prime.

    Returns:
        True if num is a prime number, otherwise False.

    .. _trial division:
        https://en.wikipedia.org/wiki/Trial_division
    """
    # All numbers less than 2 are not prime:
    if num < 2:
        return False

    # See if num is divisible by any number up to the square root of num:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primeSieve(sieveSize: int) -> list:
    """Prime sieve

    Calculates prime numbers using the `Sieve of Eratosthenes`_ algorithm.

    Args:
        sieveSize: Largest number to check if prime starting from zero.

    Returns:
        List containing prime numbers from 0 to given number.

    .. _Sieve of Eratosthenes:
        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve = [True] * sieveSize
    sieve[0] = False  # Zero and one are not prime numbers.
    sieve[1] = False

    # Create the sieve:
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # Compile the list of primes:
    primes = []
    for i in range(sieveSize):
        if sieve[i] is True:
            primes.append(i)

    return primes


def rabinMiller(num: int) -> bool:
    """Rabin-Miller primality test

    Uses the `Rabin-Miller`_ primality test to check if a given number is prime.

    Args:
         num: Number to check if prime.

    Returns:
        True if num is prime, False otherwise.

    Note:
        * The Rabin-Miller primality test relies on unproven assumptions, therefore it can return false positives when
          given a pseudoprime.

    .. _Rabin-Miller:
        https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if num % 2 == 0 or num < 2:
        return False  # Rabin-Miller doesn't work on even integers.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Keep halving s until it is odd (and use t
        # to count how many times we halve s):
        s = s // 2
        t += 1
    for trials in range(5):  # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:  # This test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


# Most of the time we can quickly determine if num is not prime
# by dividing by the first few dozen prime numbers. This is quicker
# than rabinMiller(), but does not detect all composites.
LOW_PRIMES = primeSieve(100)


def isPrime(num: int) -> bool:
    """Is prime

    This function checks divisibility by LOW_PRIMES before calling
    :func:`~books.CrackingCodesWithPython.Chapter22.primeNum.rabinMiller`.

    Args:
         num: Integer to check if prime.

    Returns:
        True if num is prime, False otherwise.

    Note:
        * If a number is divisible by a low prime number, it is not prime.
    """
    if num < 2:
        return False  # 0, 1, and negative numbers are not prime.

    if num in LOW_PRIMES:
        return True  # Low prime numbers are still prime numbers

    # See if any of the low prime numbers can divide num:
    for prime in LOW_PRIMES:
        if num % prime == 0:
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime:
    return rabinMiller(num)


def generateLargePrime(keysize: int=1024) -> int:
    """Generate large prime number

    Generates random numbers of given bit size until one is prime.

    Args:
         keysize: Number of bits prime number should be.

    Returns:
        Random prime number that is keysize bits in size.

    Note:
        * keysize defaults to 1024 bits.
    """
    while True:
        num = random.randrange(2**(keysize-1), 2**keysize)
        if isPrime(num):
            return num
