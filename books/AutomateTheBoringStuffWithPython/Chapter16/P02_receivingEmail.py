# This program uses the IMAPClient and pyzmail36 modules to retrieve emails
#
# Note:
# - imap_info file has each item on separate line
# - email address used is specially created for this chapter
# - use input() for password to prevent storing in unencrypted file

# Connecting to an IMAP Server
import imapclient

with open('imap_info') as config:
    # imap_cfg = [email, password, imap server, port]
    imap_cfg = config.read().splitlines()

imap_obj = imapclient.IMAPClient(imap_cfg[2], ssl=True)

# Logging in to the IMAP Server
print(imap_obj.login(imap_cfg[0], imap_cfg[1]))

# Searching for Email
import pprint  # Don't do this, imports should be at the top of the file
pprint.pprint(imap_obj.list_folders())

imap_obj.select_folder('INBOX', readonly=True)

uids = imap_obj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@exmaple.com'])

print(uids)

# Increase size limit from 10,000 bytes to 10,000,000 bytes
import imaplib
imaplib._MAXLINE = 10000000
