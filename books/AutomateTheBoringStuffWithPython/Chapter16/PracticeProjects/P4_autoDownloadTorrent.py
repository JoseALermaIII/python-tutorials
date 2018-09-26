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
#
# Note:
# - Shutting down after downloading is considered "Hit 'n' run" and goes against torrenting
#   - Consider setting up a seed ratio limit and let it stop sharing afterward
# - Transmission torrent client is used since it is available in Ubuntu by default
#   - A bash script is ultimately needed to shutdown Transmission
#   - Remote access is needed to run the bash script (hint)

import imapclient, imaplib, subprocess, smtplib, logging, pyzmail, datetime, time, bs4

# Setup logging
logging.basicConfig(filename='p4Log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)  # Stop logging, comment out to debug

# Increase size limit from 10,000 bytes to 10,000,000 bytes
imaplib._MAXLINE = 10000000


def countdown(time_arg):
    # Wait for time_arg seconds
    logging.info('Start countdown')
    while time_arg > 0:
        time.sleep(1)
        time_arg -= 1
    logging.info('End countdown')
    return True


def login_smtp(file_arg):
    # Login to SMTP server
    with open(file_arg) as config:
        email, password, server, port = config.read().splitlines()

    smtp_obj = smtplib.SMTP_SSL(server, port)  # Using port 465
    logging.debug(f'SMTP EHLO: {smtp_obj.ehlo()}')

    smtp_login = smtp_obj.login(email, password)
    logging.debug(f'SMTP Login: {smtp_login}')
    return smtp_obj, email


def login_imap(file_arg):
    # Login to IMAP server
    with open(file_arg) as config:
        email, password, server, port = config.read().splitlines()

    imap_obj = imapclient.IMAPClient(server, ssl=True)

    imap_login = imap_obj.login(email, password)
    logging.debug(f'IMAP login: {imap_login}')
    return imap_obj


def fetch_emails(imap_obj_arg):
    # Get emails from server
    imap_obj_arg.select_folder('INBOX', readonly=False)  # Enable mark as read and delete
    today = datetime.datetime.today()
    interval = datetime.timedelta(days=1)
    yesterday = (today - interval).strftime('%d-%b-%Y')
    uids = imap_obj_arg.search(['SINCE', yesterday])
    logging.debug(f'UIDs: {uids}')
    raw_messages = imap_obj_arg.fetch(uids, ['BODY[]'])
    return uids, raw_messages


def fetch_torrents(uids_arg, raw_messages_arg):
    urls = {}
    for uid in uids_arg:
        message = pyzmail.PyzMessage.factory(raw_messages_arg[uid][b'BODY[]'])
        subject = message.get_subject()
        logging.info(f'Current subject line: {subject}')
        # Check subject line for command and password
        if (message.html_part is not None) and ('torrent bot' and 'password' in subject.lower()):
            logging.info(f'Accessing UID#{uid}: {subject} from: {message.get_address("from")}...')

            # Soupify message
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(html, 'lxml')

            # Look for torrent link in email body
            anchors = soup.select('a')
            logging.info(f'Anchor list: {anchors}')
            for anchor in anchors:
                url = anchor.get('href')
                if url.endswith('.torrent') or url.startswith('magnet:'):
                    urls[uid] = url
        else:
            logging.error(f'RuntimeError: Email is not HTML, missing command, or password.\n'
                          f'Skipping UID#{uid}: {subject} from: {message.get_address("from")}')
            continue
    return urls


def autodownload_torrent(url_arg):
    # Send link to torrent client
    logging.info(f'Opening: {url_arg}')
    torrent_proc = subprocess.Popen(['/usr/bin/transmission-gtk', url_arg])

    # Wait for torrent client to finish download
    torrent_proc.wait()
    if torrent_proc.poll() is None:
        logging.error('Torrent client did not quit properly.')


def main():
    logging.info('Start of program')
    wait_time = datetime.timedelta(minutes=15)
    countdown(wait_time.total_seconds())

    imap_obj = login_imap('../imap_info')
    uids, raw_messages = fetch_emails(imap_obj)

    urls = fetch_torrents(uids, raw_messages)

    if urls == {} or uids == []:
        logging.error('No torrents to download.')
        print('No torrents to download.')
        return False

    smtp_obj, email = login_smtp('../smtp_info')

    for uid in urls.keys():
        url = urls[uid]
        # Compose and send start email
        logging.info(f'Starting torrent...')
        message = 'Subject: Starting torrent\nGreetings!\nI have received instructions ' \
                  'to download\n %s\n\nRegards,\nTorrent Bot' % url
        unsent = smtp_obj.sendmail(email, 'contact.me@JoseALerma.com', message)
        logging.debug(f'Unsent emails: {unsent}')

        autodownload_torrent(url)

        # Compose and send end email
        logging.info(f'Torrent finished...')
        message = 'Subject: Finished torrent\nGreetings!\nI have finished downloading\n %s\n' \
                  '\nRegards,\nTorrent Bot' % url
        unsent = smtp_obj.sendmail(email, 'contact.me@JoseALerma.com', message)
        logging.debug(f'Unsent emails: {unsent}')

        # Mark completed command email for deletion
        logging.info(f'Deleting UID#{uid}...')
        delete = imap_obj.delete_messages(uid)
        logging.debug(f'Marked for deletion: {delete}')

    # Delete marked emails
    deleted = imap_obj.expunge()
    logging.debug(f'Deleted: {deleted}')

    # Disconnect from SMTP server
    smtp_logoff = smtp_obj.quit()
    logging.debug(f'SMTP Logoff: {smtp_logoff}')

    # Disconnect from IMAP server
    imap_logoff = imap_obj.logout()
    logging.debug(f'IMAP Logoff: {imap_logoff}')
    logging.info('End of program')


# If run directly (instead of imported), run main()
if __name__ == '__main__':
    main()
