"""Assign chores

Write a program that takes a list of people’s email addresses and a list of chores
that need to be done and randomly assigns chores to people. Email each person their
assigned chores.

If you’re feeling ambitious, keep a record of each person’s previously assigned
chores so that you can make sure the program avoids assigning anyone the same chore
they did last time.

For another possible feature, schedule the program to run once a week automatically.

Notes:
    * ``smtp_info`` file has each item on a separate line.
    * Use :func:`input` for password to prevent storing in unencrypted file.
    * It may be easier to:

      * Setup a crontab to run weekly.
      * Store `saved_time` and `prev_chores` in a :py:mod:`shelve` database.

"""


def main():
    import openpyxl, random, smtplib, datetime

    # Open the spreadsheet and get the lists of data.
    wb = openpyxl.load_workbook('choresList.xlsx')
    sheet = wb['Sheet1']

    names, emails, chores, prev_chores = [], [], [], []

    for row in range(2, sheet.max_row + 1):  # skip title row
        name = sheet['A' + str(row)].value
        email = sheet['B' + str(row)].value
        chore = sheet['C' + str(row)].value
        prev_chore = sheet['D' + str(row)].value

        names.append(name)
        emails.append(email)
        chores.append(chore)
        prev_chores.append(prev_chore)

    # Run weekly
    saved_time = sheet['E2'].value
    interval = datetime.timedelta(days=7)
    now = datetime.datetime.now()
    if saved_time is None:
        saved_time = now - interval  # First run, so it's been a week
    timedelta = saved_time + interval
    if timedelta > now:
        time_left = round((timedelta - now).total_seconds()/60, 2)
        print(f"RuntimeError: Need to wait {time_left} minutes before running again.")
        raise RuntimeError
    else:
        sheet['E2'].value = now  # save to spreadsheet

    # Log in to email account.
    with open('../smtp_info') as config:
        myEmail, password, server, port = config.read().splitlines()

    smtpObj = smtplib.SMTP_SSL(server, port)  # Using port 465
    smtpObj.ehlo()
    smtpObj.login(myEmail, password)

    # Randomly assign chores
    for i in range(0, len(names)):
        random_chore = random.choice(chores)
        # Check previous chore before assignment
        while random_chore == prev_chores[i] and len(chores) > 1:
            random_chore = random.choice(chores)
        # Keep track of chores assigned
        sheet['D' + str(i + 2)].value = random_chore
        chores.remove(random_chore)  # remove assigned chore from pool

        # Send email.
        body = "Subject: Chore for the Week: %s.\nDear %s,\n\nThis week, you're in charge of:\n%s. " \
               "\n\nThank you in advance for your efforts!" % (random_chore, names[i], random_chore)
        print(f'Sending email to {emails[i]}...')
        sendmailStatus = smtpObj.sendmail(myEmail, emails[i], body)
        if sendmailStatus != {}:
            print(f'There was a problem sending email to {emails[i]}: {sendmailStatus}')
    smtpObj.quit()
    wb.save('choresList.xlsx')


if __name__ == '__main__':
    main()
