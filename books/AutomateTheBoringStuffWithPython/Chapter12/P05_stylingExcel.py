# This program uses the OpenPyXL module to manipulate Excel documents

import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb["Sheet"]

# Setting the Font Style of Cells
italic24Font = NamedStyle(name="italic24Font")
italic24Font.font = Font(size=24, italic=True)

sheet["A1"].style = italic24Font
sheet["A1"] = "Hello world!"

wb.save("styled.xlsx")

# Font Objects
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name("Sheet")

fontObj1 = Font(name="Times New Roman", bold=True)
styleObj1 = NamedStyle(name="styleObj1")
styleObj1.font = fontObj1
sheet["A1"].style/styleObj1
sheet["A1"] = "Bold Times New Roman"

fontObj2 = Font(size=24, italic=True)
styleObj2 = NamedStyle(name="styleObj2")
styleObj2.font = fontObj2
sheet["B3"].style/styleObj2
sheet["B3"] = "24 pt Italic"

wb.save("styles.xlsx")
