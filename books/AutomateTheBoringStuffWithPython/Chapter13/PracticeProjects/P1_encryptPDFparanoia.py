# Using the os.walk() function, write a script that will go through every PDF
# in a folder (and its subfolders) and encrypt the PDFs using a password provided
# on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added
# to the original filename.
#
# Before deleting the original file, have the program attempt to read and decrypt the
# file to ensure that it was encrypted correctly.

import PyPDF4, os

FOLDER = "../"

# Get all PDF files in FOLDER
files = []
for folderName, subfolders, filenames in os.walk(FOLDER):
    for filename in filenames:
        # If file is in subdirectory, append backslash to folderName
        if folderName.endswith('/'):
            filepath = folderName + filename
        else:
            filepath = folderName + '/' + filename

        if filename.lower().endswith(".pdf") and not PyPDF4.PdfFileReader(open(filepath, "rb")).isEncrypted:
            files.append(filepath)

# Get password from user

# Encrypt list of PDF files with password

# Append suffix when saving encrypted file

# Attempt to read and decrypt encrypted file

# Delete original file
