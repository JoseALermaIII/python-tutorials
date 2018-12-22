#! python3
"""Bullet point adder

Adds `Wikipedia style`_ bullet points to the start of each line of text on the clipboard.

.. _Wikipedia style:
    https://en.wikipedia.org/wiki/Help:List

"""


def main():
    import pythontutorials.books.AutomateTheBoringStuff.Ch08.pyperclip as pyperclip

    text = pyperclip.paste

    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)):  # loop through all the indexes in the "lines" list
        lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
    text = '\n'.join(lines)
    pyperclip.copy(text)


if __name__ == '__main__':
    main()
