"""Strong password detection

This program ensures passwords entered are "strong."

Write a function, :meth:`is_strong_pw`, that uses regular expressions to make sure
the password string it is passed is strong.

A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.

Note:
    You may need to test the string against multiple regex patterns to validate its strength.

"""

import re


def is_strong_pw(text: str) -> bool:
    """Is strong password

    Uses three :py:mod:`re` object patterns to check if a given text is at least 8 numbers
    and characters long, has at least one uppercase and lowercase character, and has at least
    one digit.

    Args:
        text: String containing password to test strength of.

    Returns:
        True if the given text matches the regex patterns, False otherwise.
    """
    length_regex = re.compile(r"[\d\w]{8,}")  #: At least 8 numbers and characters
    upper_lower_regex = re.compile(r"[a-z|A-Z]?[A-Z]+")  #: At least 1 upper and lower character
    digit_regex = re.compile(r"[\d]+")  #: At least one digit

    if not length_regex.search(text):
        return False
    if not digit_regex.search(text):
        return False
    if not upper_lower_regex.search(text):
        return False
    return True


def main():
    password = "AutomateTheBoringStuff1"
    print(is_strong_pw(password))


if __name__ == '__main__':
    main()
