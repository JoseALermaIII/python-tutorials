# Strong Password Detection - this program ensures passwords entered are "strong"
#
# Write a function that uses regular expressions to make sure the password string
# it is passed is strong. A strong password is defined as one that is at least eight
# characters long, contains both uppercase and lowercase characters, and has at least
# one digit. You may need to test the string against multiple regex patterns to validate
# its strength.
import re


def is_strong_pw(text):
    length_regex = re.compile(r"[\d\w]{8,}")  # at least 8 numbers and characters
    upper_lower_regex = re.compile(r"[a-z|A-Z]?[A-Z]+")  # at least 1 upper and lower character
    digit_regex = re.compile(r"[\d]+")  # at least one digit

    if not length_regex.search(text):
        return False
    if not digit_regex.search(text):
        return False
    if not upper_lower_regex.search(text):
        return False
    return True


password = "AutomateTheBoringStuff1"
print(is_strong_pw(password))
