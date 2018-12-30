"""Auto unsubscribe

Write a program that scans through your email account, finds all the unsubscribe
links in all your emails, and automatically opens them in a browser. This program
will have to log in to your email provider’s IMAP server and download all of your
emails. You can use BeautifulSoup to check for any instance where the word
unsubscribe occurs within an HTML link tag.

Once you have a list of these URLs, you can use :func:`webbrowser.open` to automatically
open all of these links in a browser.

Notes:
    * ``imap_info`` file has each item on a separate line.
    * Email address used is specially created for this chapter.
    * Use :func:`input` for password to prevent storing in unencrypted file.

"""


def main():
    import imapclient, pyzmail, bs4, webbrowser, imaplib

    # Increase size limit from 10,000 bytes to 10,000,000 bytes
    imaplib._MAXLINE = 10000000

    # Login to IMAP server
    with open('../imap_info') as config:
        email, password, server, port = config.read().splitlines()

    imap_obj = imapclient.IMAPClient(server, ssl=True)

    imap_obj.login(email, password)

    # Get message and soupify
    imap_obj.select_folder('INBOX', readonly=True)  # Don't mark as read or delete
    uids = imap_obj.search(['SINCE', '21-Sep-2018'])
    raw_messages = imap_obj.fetch(uids, ['BODY[]'])

    for uid in uids:
        message = pyzmail.PyzMessage.factory(raw_messages[uid][b'BODY[]'])
        if message.html_part is not None:
            print(f'Accessing "{message.get_subject()}" from: {message.get_address("from")}...')
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(html, 'lxml')
        else:
            print('RuntimeError: Email is not HTML.')
            print(f'Skipping "{message.get_subject()}" from: {message.get_address("from")}')
            break

        # Check soup for unsubscribe links
        anchors = soup.select('a')
        for anchor in anchors:
            if anchor.getText().lower() == 'unsubscribe':
                # Open link in browser
                url = anchor.get('href')
                print(f'Opening: {url}')
                webbrowser.open(url)

    # Disconnect from IMAP server
    imap_obj.logout()


if __name__ == '__main__':
    main()
