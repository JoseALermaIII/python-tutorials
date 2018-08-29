# Write a program that finds all encrypted PDFs in a folder (and its subfolders)
# and creates a decrypted copy of the PDF using a provided password. If the
# password is incorrect, the program should print a message to the user and
# continue to the next PDF.

import PyPDF4, os

FOLDER = "../"

# Get all encrypted PDFs in FOLDER
files = []
for folderName, subfolders, filenames in os.walk(FOLDER):
    for filename in filenames:
        # If file is in subdirectory, append backslash to folderName
        if folderName.endswith('/'):
            filepath = folderName + filename
        else:
            filepath = folderName + '/' + filename

        if filename.lower().endswith(".pdf") and PyPDF4.PdfFileReader(open(filepath, "rb")).isEncrypted:
            files.append(filepath)

# Get password from user

# Decrypt all PDFs with password

# If incorrect password, print message and continue

# Rename decrypted PDF by removing suffix
