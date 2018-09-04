I don't expect to find many more, but I'll update this post if I do.

**Note:** It's an EPUB copy, so I don't know where to get accurate publication date/time. Also, no page numbers, just reference numbers (refNum/949).

In Chapter 10, on reference number 368.7, paragraph 19.30, the code block:

```
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
```

should be:

```
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'  # Changed
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
```

# July 23, 2018 Update:

In Chapter 11, on reference number 447.4, paragraph 20.247, the code block:

```
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
```

outputs `Was not able to find an element with that name.`

The following does give the intended output:

```
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('card-img-top')  # changed
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
```

On reference number 448.7, paragraph 20.249, the code block:

```
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read It Online')
>>> type(linkElem)
<class 'selenium.webdriver.remote.webelement.WebElement'>
>>> linkElem.click() # follows the "Read It Online" link
```

should be:

```
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read Online for Free')  # changed
>>> type(linkElem)
<class 'selenium.webdriver.remote.webelement.WebElement'>
>>> linkElem.click() # follows the "Read Online for Free" link  # changed
```

On reference number 449.3, paragraph 20.252, the line:

>As long as Gmail hasn’t changed the id of the Username and Password text fields since this book was published...

"Gmail" should be "Yahoo Mail" because of line `>>> browser.get('https://mail.yahoo.com')` in the code block

# Aug. 5, 2018 Update:

In Chapter 12, on reference number 459.8, paragraph 21.47, the codeblock:

```
>>> wb.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
<Worksheet "Sheet3">
>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet.title
'Sheet3'
>>> anotherSheet = wb.get_active_sheet()
```

should be:

```
>>> wb.sheetnames  # changed
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet = wb['Sheet3']  # changed
>>> sheet
<Worksheet "Sheet3">
>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet.title
'Sheet3'
>>> anotherSheet = wb.active  # changed
```

because those methods are now depreciated (using OpenPyXL 2.5.5).

# Aug. 6, 2018 Update:

In Chapter 12, on reference number 463.0, paragraph 21.56, the codeblock:

```
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.get_highest_row()
7
>>> sheet.get_highest_column()
3
```

should be:

```
>>> sheet = wb['Sheet1']  # changed
>>> sheet.max_row  # changed
7
>>> sheet.max_column  # changed
3
```

because those methods are also depreciated.

On reference number 463.6, paragraph 21.58, the codeblock:

```
>>> from openpyxl.cell import get_column_letter, column_index_from_string
--snip--  # omitted to save space
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.get_highest_column())
'C'
```

should be:

```
>>> from openpyxl.utils import get_column_letter, column_index_from_string  # changed
--snip-- # omitted to save space
>>> sheet = wb['Sheet1']  # changed
>>> get_column_letter(sheet.max_column)  # changed
'C'
```

because the functions were relocated and methods depreciated. The lines with `openpyxl.cell` in the paragraphs above and below should also be changed. In paragraph 21.59, the line "method like get\_highest\_column() to get an integer" should be changed to "property like max\_column to get an integer."

# Aug. 7, 2018 Update:

In Chapter 12, on reference number 465.0, paragraph 21.60 is another `>>> sheet = wb.get_sheet_by_name('Sheet1')` that ought to be `>>> sheet = wb['Sheet1']`.

On reference number 466.8, paragraph 21.64, the codeblock:

```
--snip--  # omitted to save space
>>> sheet = wb.get_active_sheet()
>>> sheet.columns[1]
(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
<Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
>>> for cellObj in sheet.columns[1]:
        print(cellObj.value)
```

outputs `TypeError: 'generator' object is not subscriptable`

The best way to fix it is [debatable](https://stackoverflow.com/a/42604017), but the easiest was to use the list function:

```
 --snip--  # omitted to save space
>>> sheet = wb.active  # changed
>>> list(sheet.columns)[1]  # changed
(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
<Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
>>> for cellObj in list(sheet.columns)[1]:  # changed
        print(cellObj.value)
```

On reference number 468.0, paragraph 21.67 the list item `4. Call the get_active_sheet() or get_sheet_by_name() workbook method.` ought to be something like `4. Use the .active property or the ["UseThisSheet"] workbook key.`

On reference number 470.6, paragraph 21.90 the codeblock:

```
--snip--  # omitted to save space
➌ sheet = wb.get_sheet_by_name('Population by Census Tract')
   countyData = {}

   # TODO: Fill in countyData with each county's population and tracts.
   print('Reading rows...')
➍ for row in range(2, sheet.get_highest_row() + 1):
--snip-- # omitted to save space
```

ought to be:

```
--snip--  # omitted to save space
➌ sheet = wb['Population by Census Tract']  # changed
   countyData = {}

   # TODO: Fill in countyData with each county's population and tracts.
   print('Reading rows...')
➍ for row in range(2, sheet.max_row + 1):  # changed
```

because of depreciated methods. The codeblock on paragraph 21.96 ought to be updated as well.

# Aug. 8, 2018 Update:

In Chapter 12, on reference number 477.4, paragraph 21.111, the codeblock:

```
>>> wb.get_sheet_names()
['Sheet']
>>> sheet = wb.get_active_sheet()
>>> sheet.title
'Sheet'
>>> sheet.title = 'Spam Bacon Eggs Sheet'
>>> wb.get_sheet_names()
```

ought to be:

```
>>> wb.sheetnames  # changed
['Sheet']
>>> sheet = wb.active  # changed
>>> sheet.title
'Sheet'
>>> sheet.title = 'Spam Bacon Eggs Sheet'
>>> wb.sheetnames  # changed
```

In paragraph 21.113 (codeblock directly below) another `>>> sheet = wb.get_active_sheet()` ought to be `>>> sheet = wb.active`.

On reference number 478.6, paragraph 21.116, the codeblock:

```
>>> wb.get_sheet_names()
['Sheet']
>>> wb.create_sheet()
<Worksheet "Sheet1">
>>> wb.get_sheet_names()
['Sheet', 'Sheet1']
>>> wb.create_sheet(index=0, title='First Sheet')
<Worksheet "First Sheet">
>>> wb.get_sheet_names()
['First Sheet', 'Sheet', 'Sheet1']
>>> wb.create_sheet(index=2, title='Middle Sheet')
<Worksheet "Middle Sheet">
>>> wb.get_sheet_names()
['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
```

ought to be:

```
>>> wb.sheetnames  # changed
['Sheet']
>>> wb.create_sheet()
<Worksheet "Sheet1">
>>> wb.sheetnames  # changed
['Sheet', 'Sheet1']
>>> wb.create_sheet(index=0, title='First Sheet')
<Worksheet "First Sheet">
>>> wb.sheetnames  # changed
['First Sheet', 'Sheet', 'Sheet1']
>>> wb.create_sheet(index=2, title='Middle Sheet')
<Worksheet "Middle Sheet">
>>> wb.sheetnames  # changed
```

In paragraph 21.118 (codeblock directly below):

```
>>> wb.get_sheet_names()
['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
>>> wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
>>> wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
>>> wb.get_sheet_names()
```

ought to be

```
>>> wb.sheetnames  # changed
['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
>>> wb.remove(wb['Middle Sheet'])  # changed
>>> wb.remove(wb['Sheet1'])  # changed
>>> wb.sheetnames  # changed
```

# Aug. 11, 2018 Update:

In paragraph 21.121 (codeblock directly below), and on reference number 483.6, paragraph 21.144 (updateProduce.py) are more `>>> sheet = wb.get_sheet_by_name('Sheet')` that should be `>>> sheet = wb['Sheet']`.

On reference number 484.8, paragraph 21.146 (updateProduce.py), the line `➊ for rowNum in range(2, sheet.get_highest_row()): # skip the first row` ought to be `➊ for rowNum in range(2, sheet.max_row): # skip the first row`.

On reference number 486.5, paragraph 21.158, the line:

>To customize font styles in cells, important, import the Font() and Style() functions from the openpyxl.styles module.

Unless, of course, that's an intended pun.

On reference number 486.8, paragraph 21.158, the codeblock:

```
   >>> import openpyxl
   >>> from openpyxl.styles import Font, Style
   >>> wb = openpyxl.Workbook()
   >>> sheet = wb.get_sheet_by_name('Sheet')
➊ >>> italic24Font = Font(size=24, italic=True)
➋ >>> styleObj = Style(font=italic24Font)
➌ >>> sheet['A1'].style = styleObj
   >>> sheet['A1'] = 'Hello world!'
   >>> wb.save('styled.xlsx')
```

should be:

```
   >>> import openpyxl
   >>> from openpyxl.styles import Font, NamedStyle  # changed
   >>> wb = openpyxl.Workbook()
   >>> sheet = wb['Sheet']  # changed
➊ >>> italic24Font = NamedStyle(name="italic24Font")  # changed
➋ >>> italic24Font.font = Font(size=24, italic=True)  # changed
➌ >>> sheet['A1'].style = italic24Font  # changed
   >>> sheet['A1'] = 'Hello world!'
   >>> wb.save('styled.xlsx')
```

because the Style class is now depreciated.

# Aug. 12, 2018 Update:

In Chapter 12, on reference number 488.9, paragraph 21.178, the codeblock:

```
>>> import openpyxl
>>> from openpyxl.styles import Font, Style
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_sheet_by_name('Sheet')

>>> fontObj1 = Font(name='Times New Roman', bold=True)
>>> styleObj1 = Style(font=fontObj1)
>>> sheet['A1'].style/styleObj
>>> sheet['A1'] = 'Bold Times New Roman'

>>> fontObj2 = Font(size=24, italic=True)
>>> styleObj2 = Style(font=fontObj2)
>>> sheet['B3'].style/styleObj
>>> sheet['B3'] = '24 pt Italic'

>>> wb.save('styles.xlsx')
```

should be:

```
>>> import openpyxl
>>> from openpyxl.styles import Font, NamedStyle  # changed
>>> wb = openpyxl.Workbook()
>>> sheet = wb['Sheet']  # changed

>>> fontObj1 = Font(name='Times New Roman', bold=True)
>>> styleObj1 = NamedStyle(name="styleObj1")  # changed
>>> styleObj1.font = fontObj1  # added
>>> sheet['A1'].style = styleObj1  # changed
>>> sheet['A1'] = 'Bold Times New Roman'

>>> fontObj2 = Font(size=24, italic=True)
>>> styleObj2 = NamedStyle(name="StyleObj2")  # changed
>>> styleObj2.font = fontObj2  # added
>>> sheet['B3'].style = styleObj2 # changed
>>> sheet['B3'] = '24 pt Italic'

>>> wb.save('styles.xlsx')
```

# Aug. 13, 2018 Update:

In Chapter 12, reference number 491.5, paragraphs 21.185 and 21.187 are more `>>> sheet = wb.get_active_sheet()` that should be `>>> sheet = wb.active`. However, the formula evaluation doesn't work for me:

```
>>> import openpyxl
>>> wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
>>> sheet = wbFormulas.active  # changed
>>> sheet['A3'].value
'=SUM(A1:A2)'

>>> wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
>>> sheet = wbDataOnly.active  # changed
>>> sheet['A3'].value  # not working with LibreOffice 6.0.3.2
500
```

From what I've researched on [openpyxl.load\_workbook()](https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook),

>data\_only controls whether cells with formulae have either the formula (default) or the value stored the last time Excel read the sheet.

TODO: can someone else confirm with another LibreOffice version?

Reference numbers 493.3, 495.0, 496.2, and 497.6 have more  `>>> sheet = wb.get_active_sheet()` that should be `>>> sheet = wb.active`.

# Aug. 17, 2018 Update:

In Chapter 12, reference number 500.4, paragraph 21.234, the codeblock:

```
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_active_sheet()
>>> for i in range(1, 11):         # create some data in column A
        sheet['A' + str(i)] = i

>>> refObj = openpyxl.charts.Reference(sheet, (1, 1), (10, 1))

>>> seriesObj = openpyxl.charts.Series(refObj, title='First series')

>>> chartObj = openpyxl.charts.BarChart()
>>> chartObj.append(seriesObj)
>>> chartObj.drawing.top = 50       # set the position
>>> chartObj.drawing.left = 100
>>> chartObj.drawing.width = 300    # set the size
>>> chartObj.drawing.height = 200

>>> sheet.add_chart(chartObj)
>>> wb.save('sampleChart.xlsx')
```

works slightly better as:

```
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active  # changed
>>> for i in range(1, 11):         # create some data in column A
        sheet['A' + str(i)] = i

>>> refObj = openpyxl.chart.Reference(sheet, min_row=1, min_col=1, max_row=10, max_col=1)  # changed

>>> seriesObj = openpyxl.chart.Series(refObj, title='First series')  # changed FIXME: Chart layout is wrong (LibreOffice 6.0.3.2)

>>> chartObj = openpyxl.chart.BarChart()  # changed
>>> chartObj.append(seriesObj)
>>> chartObj.anchor = "B3"  # set the position; changed
>>> chartObj.width = 7.94  # set the size (in centimeters, where 1 cm = 37.8 pixels); changed
>>> chartObj.height = 5.29  # changed

>>> sheet.add_chart(chartObj)
>>> wb.save('sampleChart.xlsx')
```

but the layout of the chart is all wrong. TODO: can someone else confirm it works in Excel?

# Aug. 19, 2018 Update:

In Chapter 13 (I made it! Woot!), reference number 511.7, paragraph 22.13, the line:

>PyPDF2 uses a zero-based index for getting pages: The first page is page 0, the second is Introduction, and so on.

"Introduction" links to the introduction of the book. Maybe "page 1" was auto-referenced?

On reference number 513.2, paragraph 22.15, the codeblock:

```
➌ >>> pdfReader.decrypt('rosebud')
   1
   >>> pageObj = pdfReader.getPage(0)
```

gave me an `IndexError`, but the following works:

```
   >>> pdfReader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))  # added
➌ >>> pdfReader.decrypt('rosebud')
   1
   >>> pageObj = pdfReader.getPage(0)
```

# Aug. 21, 2018 Update:

In Chapter 13, reference number 524.8, paragraph 22.60, the codeblock:

```
   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # into a single PDF

   import PyPDF2, os

   # Get all the PDF filenames.
   pdfFiles = []
   for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
➋         pdfFiles.append(filename)
➌ pdfFiles.sort(key = str.lower)
```

should be:

```
   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # a single PDF  # changed

   import PyPDF2, os

   # Get all the PDF filenames.
   pdfFiles = []
   for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
➋         pdfFiles.append(filename)
➌ pdfFiles.sort(key=str.lower)  # changed
```

# Aug. 22, 2018 Update

In Chapter 13, reference number 531.0, paragraph 22.79, the codeblock:

```
➎ >>> len(doc.paragraphs[1].runs)
   4
➏ >>> doc.paragraphs[1].runs[0].text
   'A plain paragraph with some '
➐ >>> doc.paragraphs[1].runs[1].text
   'bold'
➑ >>> doc.paragraphs[1].runs[2].text
   ' and some '
➒ >>> doc.paragraphs[1].runs[3].text
   'italic'
```

outputs the following in LibreOffice 6.0.3.2 with Python-Docx 0.8.7:

```
➎ >>> len(doc.paragraphs[1].runs)
   5    # changed
➏ >>> doc.paragraphs[1].runs[0].text
   'A plain paragraph with'     # changed
➐ >>> doc.paragraphs[1].runs[1].text
   ' some ' # changed
➑ >>> doc.paragraphs[1].runs[2].text
   'bold'   # changed
➒ >>> doc.paragraphs[1].runs[3].text
   ' and some '     # changed
  >>> doc.paragraphs[1].runs[4].text    # added
   'italic'
```

TODO: can someone confirm in Word on Windows?

On reference number 540.1, paragraph 22.163, the codeblock:

```
--snip--  # omitted to save space
>>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
>>> doc.paragraphs[1].runs[1].underline = True
>>> doc.paragraphs[1].runs[3].underline = True
>>> doc.save('restyled.docx')
```

gives a `UserWarning: style lookup by style_id is deprecated. Use style name as key instead.
  return self._get_style_id_from_style(self[style_name], style_type)` but the following fixes it:

```
--snip--  # omitted to save space
>>> doc.paragraphs[1].runs[0].style = 'Quote Char'  # changed for python-docx 0.8.7
>>> doc.paragraphs[1].runs[1].underline = True
>>> doc.paragraphs[1].runs[3].underline = True
>>> doc.save('restyled.docx')
```

# Aug. 23, 2018 Update

In Chapter 13, reference number 540.1, paragraph 22.164, the line:

>We can see that it’s simple to divide a paragraph into runs and access each run individiaully.

On reference number 546.9, paragraph 22.183, the codeblock:

```
➊ >>> doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
   >>> doc.add_paragraph('This is on the second page!')
   <docx.text.Paragraph object at 0x00000000037855F8>
   >>> doc.save('twoPage.docx')
```

ought to be:

```
➊ >>> doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)  # changed
   >>> doc.add_paragraph('This is on the second page!')
   <docx.text.Paragraph object at 0x00000000037855F8>
   >>> doc.save('twoPage.docx')
```

# Aug. 31, 2018 Update

In Chapter 13, reference number 552.0, paragraph 22.228, the line:

>You should try both the uppercase and lower-case form of each word.

In Chapter 14, reference number 561.2, paragraph 23.33, the codeblock:

```
   >>> import csv
   >>> csvFile = open('example.tsv', 'w', newline='')
➊ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
   24
   >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   17
   >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
   32
```

outputs:

```
   >>> import csv
   >>> csvFile = open('example.tsv', 'w', newline='')
➊ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
   23  # changed
   >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   16  # changed
   >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
   31  # changed
```

# Sept. 1, 2018 Update:

In Chapter 14, reference number 565.5, paragraph 23.54, the codeblock:

```
#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

--snip--
# Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue    # skip first row
    csvRows.append(row)
csvFileObj.close()

# TODO: Write out the CSV file.
```

needs to be indented to match the previous codeblock:

```
#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

    --snip--
    print('Removing header from ' + csvFilename + '...')  # added
    
    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()

# TODO: Write out the CSV file.
```

On reference number 568.2, paragraph 23.58:

>The CSV Writer object will write the list to a CSV file in headerRemoved
using csvFilename (which we also used in the CSV reader).
This will overwrite the original file.

I thought the original file won't be overwritten because the new file is in
the `headerRemoved` folder?  TODO: Can someone please confirm?

On reference number 575.4, paragraph 23.98, the link `http://api.openweathermap.org
/data/2.5/forecast/daily?q=%3CLocation%3E&cnt=3` no longer works. The
OpenWeatherMap.org API [now needs an API key.](https://openweathermap.org/appid) So,
 [sign up](http://home.openweathermap.org/users/sign_up) if you _really_ want to 
 run quickWeather.py.
 
 Alternatively, the [Weather.gov API](https://www.weather.gov/documentation/services-web-api)
 (United States only, at the moment) does not require an API key (only a User Agent),
 but it will require one in the future.
 
# Sept. 4, 2018 Update:
 
In Chapter 14, reference number 582.0, paragraph 23.130, the codeblock:
 
```
for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                # Append each cell's data to rowData.

            # Write the rowData list to the CSV file.

        csvFile.close()
```

should be:

```
 for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.sheetnames:  # changed
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]  # changed

        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):  # changed
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):  # changed
                # Append each cell's data to rowData.

            # Write the rowData list to the CSV file.

        csvFile.close()
```
