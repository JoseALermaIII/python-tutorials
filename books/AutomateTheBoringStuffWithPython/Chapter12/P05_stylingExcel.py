# This program uses the OpenPyXL module to manipulate Excel documents

import openpyxl
from openpyxl.styles import Font, Style

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name("Sheet")

italic24Font = Font(size=24, italic=True)
styleObj = Style(font=italic24Font)
sheet["A1"].style = styleObj
sheet["A1"] = "Hello world!"
wb.save("styled.xlsx")
