"""Decrypt PDF paranoia

Write a program that finds all encrypted PDFs in a folder (and its subfolders)
and creates a decrypted copy of the PDF using a provided password. If the
password is incorrect, the program should print a message to the user and
continue to the next PDF.

Note:
    * Default input folder is parent directory.
    * Default output suffix is '_decrypted.pdf'.

"""


def main():
    import PyPDF4, os
    from PyPDF4.utils import PdfReadError

    FOLDER = "../"
    SUFFIX = "_encrypted.pdf"

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
    password = input("Please input decryption password:\n")

    # Decrypt all PDFs with password
    for file in files:
        pdfReader = PyPDF4.PdfFileReader(open(file, "rb"))
        pdfReader.decrypt(password)
        # If incorrect password, print message and continue to next PDF
        try:
            pdfReader.getPage(0)
        except PdfReadError as err:
            print("PdfReadError: %s" % err)
            print("Skipping: %s" % file)
            continue
        else:
            # Read decrypted PDF
            pdfWriter = PyPDF4.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            # Save decrypted PDF by removing SUFFIX, if present
            if file.lower().endswith(SUFFIX):
                newfile = file[:-len(SUFFIX)] + ".pdf"
            else:
                newfile = file
            if os.path.exists(newfile):
                newfile = newfile[:-4] + "_decrypted.pdf"
            resultPdf = open(newfile, "wb")
            pdfWriter.write(resultPdf)
            resultPdf.close()


if __name__ == '__main__':
    main()
