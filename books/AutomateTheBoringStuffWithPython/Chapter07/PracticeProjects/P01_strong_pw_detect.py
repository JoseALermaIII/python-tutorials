# Strong Password Detection - this program ensures passwords entered are "strong"
#
# Write a function that uses regular expressions to make sure the password string
# it is passed is strong. A strong password is defined as one that is at least eight
# characters long, contains both uppercase and lowercase characters, and has at least
# one digit. You may need to test the string against multiple regex patterns to validate
# its strength.
import re


def isStrongPW(text):
    lengthRegex = re.compile(r"[\d\w]{8,}")  # at least 8 numbers and characters
    upperLowerRegex = re.compile(r"[a-z|A-Z]?[A-Z]+")  # at least 1 upper and lower character
    digitRegex = re.compile(r"[\d]+")  # at least one digit

    if not lengthRegex.search(text):
        return False
    if not digitRegex.search(text):
        return False
    if not upperLowerRegex.search(text):
        return False
    return True


password = "AutomateTheBoringStuff1"
print(isStrongPW(password))
