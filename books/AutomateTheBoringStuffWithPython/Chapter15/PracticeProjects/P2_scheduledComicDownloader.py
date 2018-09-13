# Write a program that checks the websites of several web comics and automatically
# downloads the images if the comic was updated since the program’s last visit.
#
# Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X,
# and cron on Linux) can run your Python program once a day.
#
# The Python program itself can download the comic and then copy it to your desktop
# so that it is easy to find. This will free you from having to check the website
# yourself to see whether it has updated.

import os, requests, bs4, datetime, shelve, re


def get_soup(url_obj):
    print(f'Downloading page {url_obj}...')
    res = requests.get(url_obj)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'lxml')


def compare_timestamps(timestamp_obj, comic_url_obj, shelf_obj, url_obj):
    comic_date = datetime.datetime.strptime(timestamp_obj, '%B %d, %Y').date()
    comic_shelf_keys = list(shelf_obj.keys())
    if (not comic_shelf_keys) or (url_obj not in comic_shelf_keys):  # Shelf empty or URL not in shelf, download comic
        save_comic(comic_url_obj, shelf_obj, url_obj)
    else:
        shelf_date = shelf_obj[url_obj]
        if comic_date > shelf_date:  # New comic available, download comic
            save_comic(comic_url_obj, shelf_obj, url_obj)
        else:
            print('No new comic available :(')
    return None


def save_comic(comic_url_obj, shelf_obj, url_obj):
    print(f'Downloading image {comic_url_obj}...')
    comic_res = requests.get(comic_url_obj)
    comic_res.raise_for_status()

    # Save the comic to desktop.
    image_file = open(os.path.join(os.path.expanduser('~/Desktop'), os.path.basename(comic_url_obj)), "wb")
    for chunk in comic_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    now = datetime.datetime.now(tz=datetime.timezone.utc).date()
    shelf_obj[url_obj] = now
    return None


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
    compare_timestamps(match.group(), comic_url, comic_shelf, url)

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
    compare_timestamps(comic_timestamp, comic_url, comic_shelf, url)

comic_shelf.close()
