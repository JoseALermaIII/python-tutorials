# This program uses the PyPDF4 module to manipulate PDF documents
# Note:
# - Example PDFs can be downloaded from http://nostarch.com/automatestuff/
# - Book uses PyPDF2; I'm an overachiever that uses PyPDF4

# Copying Pages

import PyPDF4

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
