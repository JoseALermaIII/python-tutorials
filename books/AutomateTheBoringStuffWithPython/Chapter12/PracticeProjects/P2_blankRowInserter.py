# Create a program blankRowInserter.py that takes two integers and a filename
# string as command line arguments. Let’s call the first integer N and the second
# integer M. Starting at row N, the program should insert M blank rows into the
# spreadsheet.

import sys
import openpyxl

# Get arguments from commandline
#N = int(''.join(sys.argv[0]))
#M = int(''.join(sys.argv[1]))
#file = ''.join(sys.argv[2])
N = 4
M = 2
file = "multTable.xlsx"

# Open workbooks
readwb = openpyxl.load_workbook(file)
readsheet = readwb.active

writewb = openpyxl.Workbook()
writesheet = writewb.active

# Read readwb and transpose into writewb, TODO: Insert blank lines
for rowOfCellObjects in readsheet.rows:
    for cellObj in rowOfCellObjects:
            writesheet[cellObj.coordinate].value = cellObj.value


# Save workbook
writewb.save("updated" + file)
