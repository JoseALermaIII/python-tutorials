#! python3
# combinePDFs.py - Combines all the PDFs in the current working directory into
# a single PDF.
# Note:
# - Example PDFs can be downloaded from http://nostarch.com/automatestuff/
# - Book uses PyPDF2; I'm an overachiever that uses PyPDF4

import PyPDF4, os

# Get all the PDF filenames.
if os.path.exists("allminutes.pdf"):
    os.remove("allminutes.pdf")
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF4.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, "rb")
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted and filename == "encrypted.pdf":
        pdfReader.decrypt("rosebud")
    if pdfReader.isEncrypted and filename == "encryptedminutes.pdf":
        pdfReader.decrypt("swordfish")
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open("allminutes.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()
