#! python3
"""Multiclipboard

Saves and loads pieces of text to/from the clipboard into :py:mod:`shelve` based on keywords.

Usage:
    py.exe P2_mcb.pyw save <keyword> - Saves clipboard to keyword.
    py.exe P2_mcb.pyw <keyword> - Loads keyword to clipboard.
    py.exe P2_mcb.pyw list - Loads all keywords to clipboard.
"""


def main():
    import shelve, sys
    import pyperclip

    mcbShelf = shelve.open('mcb')

    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    mcbShelf.close()


if __name__ == '__main__':
    main()
