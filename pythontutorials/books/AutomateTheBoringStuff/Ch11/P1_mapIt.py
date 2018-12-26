#! python3
"""Map it

Launches a map in the browser using an address from the command line or clipboard.

"""


def main():
    import webbrowser, sys
    from pyperclip import paste

    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = paste()

    webbrowser.open("https://www.google.com/maps/place/" + address)


if __name__ == '__main__':
    main()
