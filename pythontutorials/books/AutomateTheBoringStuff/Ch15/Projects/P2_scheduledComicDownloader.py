"""Scheduled comic downloader

Write a program that checks the websites of several web comics and automatically
downloads the images if the comic was updated since the program’s last visit.

Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X,
and cron on Linux) can run your Python program once a day.

The Python program itself can download the comic and then copy it to your desktop
so that it is easy to find. This will free you from having to check the website
yourself to see whether it has updated.

Note:
    This only downloads from http://www.lefthandedtoons.com/ and
    http://buttersafe.com/ because all websites are different.

"""

import os, requests, bs4, datetime, shelve, re


def get_soup(url_arg: str) -> bs4.BeautifulSoup:
    """Get soup

    Downloads given url with :py:mod:`requests` and converts it to :class:`bs4.BeautifulSoup`.

    Args:
        url_arg: String with url to soupify.

    Returns:
        BeautifulSoup object of given url.

    Raises:
        requests.exceptions.HTTPError: If download of website url failed.
    """
    print(f'Downloading page {url_arg}...')
    res = requests.get(url_arg)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'lxml')


def compare_timestamps(timestamp_arg: str, shelf_arg: shelve.open, url_arg: str) -> bool:
    """Compare timestamps

    Compares timestamp of current comic to last downloaded comic timestamp of given url.

    Args:
        timestamp_arg: String with date in ``Month DD, YYYY`` format.
        shelf_arg: :py:mod:`shelve` object with urls as keys and
            :meth:`datetime.datetime.date` as values.
        url_arg: String with website url.

    Returns:
        True if comic's timestamp is after saved timestamp, False otherwise.
    """
    comic_date = datetime.datetime.strptime(timestamp_arg, '%B %d, %Y').date()
    shelf_date = shelf_arg[url_arg]
    if comic_date > shelf_date:  # New comic available, download comic
        return True
    return False


def check_key(shelf_arg: shelve.open, url_arg: str) -> bool:
    """Check key

    Checks if given url is a key in the given shelf.

    Args:
        shelf_arg: :py:mod:`shelve` object with urls as keys and
            :meth:`datetime.datetime.date` as values.
        url_arg: String with website url.

    Returns:
        True if the url is in the shelf, False otherwise.
    """
    keys = shelf_arg.keys
    if url_arg in keys:
        return True
    return False


def save_comic(comic_url_arg: str, shelf_arg: shelve.open, url_arg: str) -> None:
    """Save comic

    Downloads given comic url and saves to desktop, then updates download time of given website url in given shelf.

    Args:
        comic_url_arg: String with url of comic image.
        shelf_arg: :py:mod:`shelve` object with urls as keys and
            :meth:`datetime.datetime.date` as values.
        url_arg: String with website url.

    Returns:
        None. Comic image is saved to desktop.

    Raises:
        requests.exceptions.HTTPError: If download of comic url failed.
    """
    print(f'Downloading image {comic_url_arg}...')
    comic_res = requests.get(comic_url_arg)
    comic_res.raise_for_status()

    # Save the comic to desktop.
    image_file = open(os.path.join(os.path.expanduser('~/Desktop'), os.path.basename(comic_url_arg)), "wb")
    for chunk in comic_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    now = datetime.datetime.now().date()
    shelf_arg[url_arg] = now
    return None


def main():
    comic_shelf = shelve.open('comic')

    # Download page
    url = 'http://www.lefthandedtoons.com/'
    soup = get_soup(url)

    # Get comic url in case it needs to be downloaded
    image_elem = soup.select('.comicimage')
    comic_url = image_elem[0].get('src')

    # Compare page's timestamp to shelve's
    comic_title_elem = soup.select('.comictitlearea')
    if not comic_title_elem:
        print('Could not find comic timestamp.')
    else:
        title_text = comic_title_elem[0].getText()
        match = re.search('\w+ \d+, \d{4}', title_text)
        if not check_key(comic_shelf, url) or compare_timestamps(match.group(), comic_shelf, url):
            save_comic(comic_url, comic_shelf, url)

    # Download page
    url = 'http://buttersafe.com/'
    soup = get_soup(url)

    # Get comic url in case it needs to be downloaded
    div_elem = soup.find('div', attrs={'id': 'comic'})
    comic_url = div_elem.find('img')['src']

    # Compare page's timestamp to shelve's
    comic_header = soup.select('#headernav-date')
    if not comic_header:
        print('Could not find comic timestamp.')
    else:
        header_text = comic_header[0].getText()
        match = re.search('(\w+), (\w+) (\d+).., (\d{4})', header_text)
        comic_timestamp = f'{match.group(2)} {match.group(3)}, {match.group(4)}'
        if not check_key(comic_shelf, url) or compare_timestamps(comic_timestamp, comic_shelf, url):
            save_comic(comic_url, comic_shelf, url)

    comic_shelf.close()


if __name__ == '__main__':
    main()
