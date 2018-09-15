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

