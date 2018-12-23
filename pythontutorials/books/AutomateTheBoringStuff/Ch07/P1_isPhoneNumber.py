"""Is phone number

This program demonstrates :meth:`isPhoneNumber` which returns True if a string is a
phone number and False if not.

However, :meth:`isPhoneNumber` is not very efficient because it uses if statements
and for loops to check 12-segment chunks for a phone number pattern.


"""


def isPhoneNumber(text: str) -> bool:
    """Is phone number

    Function tests if given text is a phone number by checking a given text
    for two consecutive '###-` patterns followed by a '####' pattern using
    if statements and for loops.

    Args:
        text: String to check for a phone number pattern.

    Returns:
        True if the given string is a phone number, False otherwise.
    """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def main():
    print('415-555-4242 is a phone number:')
    print(isPhoneNumber('415-555-4242'))
    print('Moshi moshi is a phone number:')
    print(isPhoneNumber('Moshi moshi'))

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i + 12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')


if __name__ == '__main__':
    main()
