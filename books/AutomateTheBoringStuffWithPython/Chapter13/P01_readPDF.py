# This program manipulates PDF files
# Note:
# - Example PDFs can be downloaded from http://nostarch.com/automatestuff/
# - Book uses PyPDF2; I'm an overachiever that uses PyPDF4

import PyPDF4

# Extracting Text from PDFs
pdfFileObj = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
