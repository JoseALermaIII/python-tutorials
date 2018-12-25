#! python3
"""Extended multiclipboard

Saves and loads pieces of text to/from the clipboard into :py:mod:`shelve` based on keywords.

Extend the multiclipboard program in this chapter so that it has a delete <keyword>
command line argument that will delete a keyword from the shelf. Then add a delete
command line argument that will delete all keywords.

Usage:
    py.exe P1_mcb.pyw save <keyword> - Saves clipboard to keyword.
    py.exe P1_mcb.pyw delete <keyword> - Deletes keyword from database.
    py.exe P1_mcb.pyw <keyword> - Loads keyword to clipboard.
    py.exe P1_mcb.pyw list - Loads all keywords to clipboard.
    py.exe P1_mcb.pyw delete - Deletes all keywords from database.

"""


def main():
    import shelve, sys
    import pyperclip

    mcbShelf = shelve.open('mcb')

    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    # Delete clipboard content.
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

    elif len(sys.argv) == 2:
        # List keywords, delete all keywords, and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcbShelf.clear()
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    mcbShelf.close()


if __name__ == '__main__':
    main()
