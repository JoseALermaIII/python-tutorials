#! python3
"""Password locker

An insecure password locker program. This program stores different passwords as
key value pairs in a dictionary. Keys are the name of the account and the values
are the passwords for each account.

"""


def main() -> None:
    """P5_pw.py

    If given account name is in the dictionary, the matching password is copied to the
    clipboard via :py:mod:`pyperclip`.
    Otherwise, an error is printed.

    Returns:
        None. Status or error messages are printed.

    Note:
        If called without arguments, program exits with error message.
    """
    import sys
    import pyperclip

    PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                 'luggage': '12345'}
    """dict: Dictionary with account names as keys and passwords as values."""

    if len(sys.argv) < 2:
        print('Usage: python P5_pw.py [account] - copy account password')
        sys.exit()

    account = sys.argv[1]  # first command line arg is the account name

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)


if __name__ == '__main__':
    main()
