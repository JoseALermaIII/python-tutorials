# This program uses the OpenPyXL module to manipulate Excel documents

# Opening Excel Documents with OpenPyXL
import openpyxl
wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))

# Getting Sheets from the Workbook
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name("Sheet3")
print(sheet)
print(type(sheet))
print(sheet.title)
anotherSheet = wb.get_active_sheet()
print(anotherSheet)
