#! python3
# P03_sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

import openpyxl, smtplib, sys

# Open the spreadsheet and get the latest dues status.
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

lastCol = sheet.max_column
latestMonth = sheet.cell(row=1, column=lastCol).value

# Check each member's payment status.
for r in range(2, sheet.max_row + 1):
    payment = sheet.cell(row=r, column=lastCol).value
    if payment != 'paid':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaidMembers[name] = email

# Log in to email account.
with open('smtp_info') as config:
    # smtp_cfg = [email, password, smtp server, port]
    smtp_cfg = config.read().splitlines()

smtpObj = smtplib.SMTP_SSL(smtp_cfg[2], smtp_cfg[3])  # Using port 465
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(smtp_cfg[0], smtp_cfg[1])

# Send out reminder emails.
for name, email in upaidMembers.items():
    body = "Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not paid dues for %s." \
           "Please make this payment as soon as possible. Thank you!'" % (latestMonth, name, latestMonth)
    print('Sending email to %s...' % email)
    sendmailStatus = smtpObj.sendmail(smtp_cfg[0], email, body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email, sendmailStatus))
smtpObj.quit()
