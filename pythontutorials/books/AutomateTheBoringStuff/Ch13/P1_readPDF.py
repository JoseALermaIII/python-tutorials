"""Read PDF

This program reads PDF files.

Note:
    * Example PDFs can be downloaded from http://nostarch.com/automatestuff/
    * Book uses PyPDF2; I'm an overachiever that uses PyPDF4

"""


def main():
    import PyPDF4
    from PyPDF4.utils import PdfReadError

    # Extracting Text from PDFs
    pdfFileObj = open("meetingminutes.pdf", "rb")
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

    # Decrypting PDFs
    pdfReader = PyPDF4.PdfFileReader(open("encrypted.pdf", "rb"))
    print(pdfReader.isEncrypted)

    try:
        print(pdfReader.getPage(0))
    except PdfReadError as err:
        print("PdfReadError: %s" % err)

    pdfReader = PyPDF4.PdfFileReader(open("encrypted.pdf", "rb"))
    print(pdfReader.decrypt("rosebud"))
    pageObj = pdfReader.getPage(0)


if __name__ == '__main__':
    main()
