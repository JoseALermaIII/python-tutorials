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

# Creating and Removing Sheets
wb = openpyxl.Workbook()
print(wb.get_sheet_names())
wb.create_sheet()
print(wb.get_sheet_names())
wb.create_sheet(index=0, title="First Sheet")
print(wb.get_sheet_names())
wb.create_sheet(index=2, title="Middle Sheet")
print(wb.get_sheet_names())

wb.remove_sheet(wb.get_sheet_by_name("Middle Sheet"))
wb.remove_sheet(wb.get_sheet_by_name("Sheet1"))
print(wb.get_sheet_names())
