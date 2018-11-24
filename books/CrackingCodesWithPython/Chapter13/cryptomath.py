"""Cryptomath Module

Provides mathematical functions for use in cryptography. (Discrete mathematics FTW!)

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""


def gcd(a: int, b: int) -> int:
    """Greatest common divisor

    Returns greatest common divisor of given inputs using Euclid's algorithm.

    Args:
        a: First integer input.
        b: Second integer input.

    Returns:
        Integer representing GCD.
    """
    # Return the GCD of a and b using Euclid's algorithm:
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a: int, m: int):
    """Modular inverse

    Returns modular inverse of given inputs using Euclid's extended algorithm.

    Args:
        a: First integer input.
        m: Second integer input.

    Returns:
        Modular inverse as an integer if it exists, None otherwise.
    """
    # Return the modular inverse of a % m, which is
    # the number x such that a * x % m = 1

    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.

    # Calculate using the extended Euclidean algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
