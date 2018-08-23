# This program uses the python-docx module to manipulate Word documents
#
# Note:
# - Example .docx files can be downloaded from http://nostarch.com/automatestuff/


import docx

# Changing Run Attributes
doc = docx.Document("demo.docx")
print(doc.paragraphs[0].text)
print(doc.paragraphs[0].style)
doc.paragraphs[0].style = "Normal"
print(doc.paragraphs[1].text)
print((doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text,
       doc.paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text))
doc.paragraphs[1].runs[0].style = "Quote Char"
doc.paragraphs[1].runs[1].underline = True
doc.paragraphs[1].runs[3].underline = True
doc.save("restyled.docx")

# Writing Word Documents
doc = docx.Document()
print(doc.add_paragraph("Hello world!"))
doc.save("helloworld.docx")

doc = docx.Document()
print(doc.add_paragraph("Hello world!"))
paraObj1 = doc.add_paragraph("This is a second paragraph.")
paraObj2 = doc.add_paragraph("This is yet another paragraph.")
print(paraObj1.add_run(" This text is being added to the second paragraph."))
print(doc.add_paragraph("Hello world!", "Title"))
doc.save("multipleParagraphs.docx")
