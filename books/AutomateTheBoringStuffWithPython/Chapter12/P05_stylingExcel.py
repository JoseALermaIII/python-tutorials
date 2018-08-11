# This program uses the OpenPyXL module to manipulate Excel documents

import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name("Sheet")

italic24Font = NamedStyle(name="italic24Font")
italic24Font.font = Font(size=24, italic=True)

sheet["A1"].style = italic24Font
sheet["A1"] = "Hello world!"

wb.save("styled.xlsx")
