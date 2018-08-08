# This program uses the OpenPyXL module to manipulate Excel documents

# Creating and Saving Excel Documents

import openpyxl
wb = openpyxl.Workbook()
print(wb.sheetnames)
sheet = wb.active
print(sheet.title)
sheet.title = "Spam Bacon Eggs Sheet"
print(wb.sheetnames)

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb.active
sheet.title = "Spam Spam Spam"
wb.save("example_copy.xlsx")
