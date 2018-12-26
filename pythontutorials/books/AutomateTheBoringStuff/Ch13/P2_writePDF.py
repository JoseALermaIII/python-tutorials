"""Write PDF

This program uses :py:mod:`PyPDF4` to write PDF documents.

Note:
    * Example PDFs can be downloaded from http://nostarch.com/automatestuff/
    * Book uses PyPDF2; I'm an overachiever that uses PyPDF4

"""


def main():
    import PyPDF4

    # Copying Pages
    pdf1File = open("meetingminutes.pdf", "rb")
    pdf2File = open("meetingminutes2.pdf", "rb")
    pdf1Reader = PyPDF4.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF4.PdfFileReader(pdf2File)
    pdfWriter = PyPDF4.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOutputFile = open("combinedminutes.pdf", "wb")
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

    # Rotating Pages
    minutesFile = open("meetingminutes.pdf", "rb")
    pdfReader = PyPDF4.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    print(page.rotateClockwise(90))

    pdfWriter = PyPDF4.PdfFileWriter()
    pdfWriter.addPage(page)
    resultPdfFile = open("rotatedPage.pdf", "wb")
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()

    # Overlaying Pages
    minutesFile = open("meetingminutes.pdf", "rb")
    pdfReader = PyPDF4.PdfFileReader(minutesFile)
    minutesFirstPage = pdfReader.getPage(0)
    pdfWatermarkReader = PyPDF4.PdfFileReader(open("watermark.pdf", "rb"))  # lol
    minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF4.PdfFileWriter()
    pdfWriter.addPage(minutesFirstPage)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    resultPdfFile = open("watermarkedCover.pdf", "wb")
    pdfWriter.write(resultPdfFile)
    minutesFile.close()
    resultPdfFile.close()

    # Encrypting PDFs
    pdfFile = open("meetingminutes.pdf", "rb")
    pdfReader = PyPDF4.PdfFileReader(pdfFile)
    pdfWriter = PyPDF4.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt("swordfish")
    resultPdf = open("encryptedminutes.pdf", "wb")
    pdfWriter.write(resultPdf)
    resultPdf.close()


if __name__ == '__main__':
    main()
