"""Receiving email

This program uses :class:`imapclient.IMAPClient` and `pyzmail36`_ to retrieve emails.

Notes:
    * ``imap_info`` file has each item on a separate line.
    * Email address used is specially created for this chapter.
    * Use :func:`input` for password to prevent storing in unencrypted file.

.. _pyzmail36:
    https://pypi.org/project/pyzmail36/

"""


def main():
    # Connecting to an IMAP Server
    import imapclient

    with open('imap_info') as config:
        email, password, server, port = config.read().splitlines()

    imap_obj = imapclient.IMAPClient(server, ssl=True)

    # Logging in to the IMAP Server
    print(imap_obj.login(email, password))

    # Searching for Email
    import pprint  # Don't do this, imports should be at the top of the file
    pprint.pprint(imap_obj.list_folders())

    imap_obj.select_folder('INBOX', readonly=True)

    uids = imap_obj.search(['SINCE', '01-Jan-2015', 'NOT', 'FROM', 'alice@exmaple.com'])

    print(uids)

    # Increase size limit from 10,000 bytes to 10,000,000 bytes
    import imaplib
    imaplib._MAXLINE = 10000000

    # Fetching an Email and Marking it as Read
    raw_messages = imap_obj.fetch(uids, ['BODY[]'])
    pprint.pprint(raw_messages)

    #imap_obj.select_folder('INBOX', readonly=False)  # Allows marking as read when using fetch()

    # Getting Email Addresses from a Raw Message
    import pyzmail
    message = pyzmail.PyzMessage.factory(raw_messages[uids[0]][b'BODY[]'])

    print(message.get_subject())
    print(message.get_addresses('from'))
    print(message.get_addresses('to'))
    print(message.get_addresses('cc'))
    print(message.get_addresses('bcc'))

    # Getting the Body from a Raw Message
    if message.text_part is not None:
        print(message.text_part.get_payload().decode(message.text_part.charset))
    if message.html_part is not None:
        print(message.html_part.get_payload().decode(message.html_part.charset))

    # Deleting Emails
    imap_obj.select_folder('INBOX', readonly=False)  # Allows deleting of emails
    uids = imap_obj.search(['ON', '15-Sep-2018'])
    print(uids)
    print(imap_obj.delete_messages(uids))
    print(imap_obj.expunge())

    # Disconnecting from the IMAP Server
    imap_obj.logout()


if __name__ == '__main__':
    main()
