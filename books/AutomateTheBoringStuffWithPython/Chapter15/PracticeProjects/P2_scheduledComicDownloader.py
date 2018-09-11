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


def downloadComic(soupObj, shelfObj, page):
    comicElem = soupObj.select('.comicimage')
    comicUrl = comicElem[0].get('src')
    print(f'Downloading image {comicUrl}...')
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the comic to desktop.
    imageFile = open(os.path.join(os.path.expanduser('~/Desktop'), os.path.basename(comicUrl)), "wb")
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    now = datetime.datetime.now(tz=datetime.timezone.utc).date()
    shelfObj[page] = now
    return None


url = 'http://www.lefthandedtoons.com/'
comicShelf = shelve.open('comic')

# TODO: fix logic flow - don't download page unless needed, compare timestamps sooner
# TODO: add more URLs
# Download page
print(f'Downloading page {url}...')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

# Compare page's timestamp to shelve's
comicTitleElem = soup.select('.comictitlearea')
if not comicTitleElem:
    print('Could not find comic timestamp.')
else:
    comicTimestamp = comicTitleElem[0].getText()
    match = re.search('\w+ \d+, \d{4}', comicTimestamp)
    comicDate = datetime.datetime.strptime(match.group(), '%B %d, %Y').date()

    if not list(comicShelf.keys()):  # Shelf empty, download comic
        downloadComic(soup, comicShelf, url)
    else:
        if url not in list(comicShelf.keys()):  # URL not in shelf, download comic
            downloadComic(soup, comicShelf, url)
        else:
            shelfDate = comicShelf[url]
            if comicDate > shelfDate:  # Download new comic
                downloadComic(soup, comicShelf, url)
            else:
                print("No new comic available :(")


comicShelf.close()
