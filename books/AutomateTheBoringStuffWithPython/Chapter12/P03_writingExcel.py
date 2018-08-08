# This program uses the OpenPyXL module to manipulate Excel documents

# Creating and Saving Excel Documents

import openpyxl
wb = openpyxl.Workbook()
print(wb.get_sheet_names())
sheet = wb.get_active_sheet()
print(sheet.title)
sheet.title = "Spam Bacon Eggs Sheet"
print(wb.get_sheet_names())

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb.get_active_sheet()
sheet.title = "Spam Spam Spam"
wb.save("example_copy.xlsx")
