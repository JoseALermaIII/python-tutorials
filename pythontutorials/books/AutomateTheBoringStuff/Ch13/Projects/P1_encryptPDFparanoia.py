"""Encrypt PDF paranoia

Using :func:`os.walk`, write a script that will go through every PDF
in a folder (and its subfolders) and encrypt the PDFs using a password provided
on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added
to the original filename.

Before deleting the original file, have the program attempt to read and decrypt the
file to ensure that it was encrypted correctly.

Notes:
    * Default folder is parent directory.
    * Default suffix is '_encrypted.pdf'.
    * Running in debug mode, uncomment to delete original file.

"""


def main():
    import PyPDF4, os
    from PyPDF4.utils import PdfReadError

    FOLDER = "../"
    SUFFIX = "_encrypted.pdf"

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
    password = input("Please input encryption password:\n")

    # Encrypt list of PDF files with password
    for file in files:
        pdfFile = open(file, "rb")
        pdfReader = PyPDF4.PdfFileReader(pdfFile)
        pdfWriter = PyPDF4.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))

        pdfWriter.encrypt(password)

        # Append SUFFIX when saving encrypted file
        newfile = file[:-4] + SUFFIX
        resultPdf = open(newfile, "wb")
        pdfWriter.write(resultPdf)
        resultPdf.close()

        # Attempt to read and decrypt encrypted file
        pdfReader = PyPDF4.PdfFileReader(open(newfile, "rb"))
        pdfReader.decrypt(password)
        # If the first page cannot be read, print error and move to next file
        try:
            pdfReader.getPage(0)
        except PdfReadError as err:
            print("PdfReadError: %s" % err)
            print("Skipping: %s" % file)
            continue

        # Delete original file
        print("Deleting: %s" % file)  # DEBUG
        #os.remove(file)  # uncomment if sure


if __name__ == '__main__':
    main()
