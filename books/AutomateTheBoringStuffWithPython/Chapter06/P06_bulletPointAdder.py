#! python3
# P06_bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import books.CrackingCodesWithPython.pyperclip
text = books.CrackingCodesWithPython.pyperclip.paste

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all the indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
books.CrackingCodesWithPython.pyperclip.copy(text)
