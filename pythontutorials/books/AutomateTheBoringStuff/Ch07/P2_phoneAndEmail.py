#! python3
"""Phone and email

Finds phone numbers and email addresses in the clipboard using :py:mod:`re` and
:py:mod:`pyperclip`.

Attributes:
    phoneRegex (re.compile): Regular expression object representing a phone number pattern.
    emailRegex (re.compile): Regular expression object representing an email pattern.

"""


import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)
)''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)


def main() -> None:
    """P2_phoneAndEmail.py

    Checks clipboard text for phone numbers and emails using :py:mod:`re`. If found,
    matches are copied to the clipboard and printed to terminal.

    Returns:
        None. Prints and copies matches to clipboard or prints status message.
    """
    import pyperclip
    # Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # Copy the results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


if __name__ == '__main__':
    main()
