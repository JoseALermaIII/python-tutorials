# This program uses the OpenPyXL module to manipulate Excel documents

# Opening Excel Documents with OpenPyXL
import openpyxl
wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))
