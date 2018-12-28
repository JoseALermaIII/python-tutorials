"""Text to Excel

Write a program to read in the contents of several text files (you can make
the text files yourself) and insert those contents into a spreadsheet, with
one line of text per row. The lines of the first text file will be in the
cells of column A, the lines of the second text file will be in the cells of
column B, and so on.

Note:
    * Default folder is ``./p4files/``
    * Default output file is ``textToExcel.xlsx``

"""


def main():
    import openpyxl
    import os

    FOLDER = "./p4files/"

    # Open workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Get list of files
    filelist = os.listdir(FOLDER)
    filelist.sort()

    # Open file
    for file in filelist:
        with open(FOLDER + file) as fileObj:
            index = 1
            for line in fileObj:
                # Transpose line into relevant workbook column
                sheet.cell(row=index, column=(filelist.index(file) + 1)).value = line.strip()
                index += 1

    # Save workbook
    wb.save("textToExcel.xlsx")


if __name__ == '__main__':
    main()
