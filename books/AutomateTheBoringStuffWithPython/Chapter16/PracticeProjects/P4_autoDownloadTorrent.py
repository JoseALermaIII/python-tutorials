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

import imapclient, imaplib, subprocess, smtplib, logging, pyzmail, datetime, time, bs4

# Setup logging
logging.basicConfig(filename='p4Log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)  # Stop logging, comment out to debug

# Increase size limit from 10,000 bytes to 10,000,000 bytes
imaplib._MAXLINE = 10000000


def countdown(time_arg):
    # Wait for time_arg seconds
    while time_arg > 0:
        logging.debug(f'Time left: {time_arg}', end='')
        time.sleep(1)
        time_arg -= 1
    return True


def email_myself(smtp_arg, email_arg, message_arg):
    unsent = smtp_arg.sendmail(email_arg, 'contact.me@JoseALerma.com', message_arg)
    logging.debug(f'Unsent emails: {unsent}')
    return unsent


def autodownload_torrent():
    # Login to IMAP server
    with open('../imap_info') as config:
        email, password, server, port = config.read().splitlines()

    imap_obj = imapclient.IMAPClient(server, ssl=True)

    imap_login = imap_obj.login(email, password)
    logging.debug(f'IMAP login: {imap_login}')

    # Get emails from server
    imap_obj.select_folder('INBOX', readonly=False)  # Enable mark as read and delete
    uids = imap_obj.search(['SINCE', '21-Sep-2018'])
    raw_messages = imap_obj.fetch(uids, ['BODY[]'])

    for uid in uids:
        message = pyzmail.PyzMessage.factory(raw_messages[uid][b'BODY[]'])
        if message.html_part is not None:
            # Check subject line for command and password
            logging.info(f'Accessing "{message.get_subject()}" from: {message.get_address("from")}...')
            # TODO: Parse command and password from subject line

            # Soupify message
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(html, 'lxml')
        else:
            logging.error(f'RuntimeError: Email is not HTML. Skipping "{message.get_subject()}"'
                          f'from: {message.get_address("from")}')
            break

        # Look for torrent link in email body
        anchors = soup.select('a')
        logging.debug(f'Anchor list: {anchors}')
        for anchor in anchors:
            url = anchor.get('href')
            if url.endswith('.torrent'):
                # Send link to torrent client and send status email
                logging.info(f'Opening: {url}')
                # TODO: Subprocess torrent client

                # Login to SMTP server
                with open('../smtp_info') as config:
                    email, password, server, port = config.read().splitlines()

                smtp_obj = smtplib.SMTP_SSL(server, port)  # Using port 465
                logging.debug(f'SMTP EHLO: {smtp_obj.ehlo()}')

                smtp_login = smtp_obj.login(email, password)
                logging.debug(f'SMTP Login: {smtp_login}')

                # Compose and send start email
                logging.debug(f'Starting torrent...')
                message_send = 'Subject: Starting torrent\nGreetings!\nI have received instructions to download\n %s\n' \
                               '\nRegards,\nTorrent Bot' % url
                email_myself(smtp_obj, email, message_send)

                # Delete completed command email
                logging.info(f'Deleting {message.get_subject()}...')
                delete = imap_obj.delete_messages(uid)
                logging.debug(f'Marked for deletion: {delete}')
                deleted = imap_obj.expunge()
                logging.debug(f'Deleted: {deleted}')

                # TODO: Wait for torrent client to finish download and send status email

                # Compose and send end email
                logging.debug(f'Torrent finished...')
                message_send = 'Subject: Finished torrent\nGreetings!\nI have finished downloading\n %s\n' \
                               '\nRegards,\nTorrent Bot' % url
                email_myself(smtp_obj, email, message_send)

                # Disconnect from SMTP server
                smtp_logoff = smtp_obj.quit()
                logging.debug(f'SMTP Logoff: {smtp_logoff}')
    # Disconnect from IMAP server
    imap_logoff = imap_obj.logout()
    logging.debug(f'IMAP Logoff: {imap_logoff}')
    return None


def main():
    logging.debug('Start of program')
    wait_time = datetime.timedelta(minutes=15)
    countdown(wait_time.total_seconds())
    autodownload_torrent()
    logging.debug('End of program')
    return None


# If run directly (instead of imported), run main()
if __name__ == '__main__':
    main()
