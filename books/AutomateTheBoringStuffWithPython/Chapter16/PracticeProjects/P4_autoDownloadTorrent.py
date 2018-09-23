# Write a program that checks an email account every 15 minutes for any instructions
# you email it and executes those instructions automatically.
#
# For example, BitTorrent is a peer-to-peer downloading system. Using free BitTorrent
# software such as qBittorrent, you can download large media files on your home computer.
# If you email the program a (completely legal, not at all piratical) BitTorrent link,
# the program will eventually check its email, find this message, extract the link, and
# then launch qBittorrent to start downloading the file. This way, you can have your
# home computer begin downloads while you’re away, and the (completely legal, not at
# all piratical) download can be finished by the time you return home.

import imapclient, subprocess, smtplib, logging, pyzmail

# Wait 15 minutes
import time

# Login to IMAP server

# Get emails and check subject line for command and password

    # Look for torrent link in email body

    # Send link to torrent client and send status email
        # Login to SMTP server

        # Compose and send email

        # Delete completed command email

    # Wait for torrent client to finish download and send status email
        # Compose and send email

        # Disconnect from SMTP server

# Disconnect from IMAP server
