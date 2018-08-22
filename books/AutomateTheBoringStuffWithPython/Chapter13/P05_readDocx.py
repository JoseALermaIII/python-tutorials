#! python3
# P05_readDocx.py - Accepts a filename of a .docx file and returns a single
# string value of its text.
#
# Note:
# - Example .docx files can be downloaded from http://nostarch.com/automatestuff/

import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        #fullText.append(' ' + para.text)  # Alt: indent each paragraph
    return "\n".join(fullText)
    #return "\n\n".join(fullText)  # Alt: double space between paragraphs
