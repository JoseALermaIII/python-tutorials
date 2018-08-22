#! python3
# P05_readDocx.py - Accepts a filename of a .docx file and returns a single
# string value of its text.

import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)
