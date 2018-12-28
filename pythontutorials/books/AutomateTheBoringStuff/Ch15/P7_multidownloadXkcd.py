#! python3
"""Multidownload XKCD

Downloads 1400 `XKCD`_ comics much faster by using :py:mod:`threading`.

Note:
    Default output directory is ``./xkcd``.

.. _XKCD:
    https://xkcd.com/

"""

import requests, os, bs4

def downloadXkcd(startComic: int, endComic: int) -> None:
    """Download XKCD

    Uses :py:mod:`requests` and :py:mod:`bs4' to download all comics in a given range.

    Args:
        startComic: Comic ID number to start from.
        endComic: Comic ID number to end at.

    Returns:
        None. Prints status updates and downloads comics to download directory.

    """
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


def main():
    import threading
    os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

    # Create and start the Thread objects.
    downloadThreads = []  # a list of all the Thread objects
    for i in range(0, 1400, 100):  # loops 14 times, creates 14 threads
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    # Wait for all threads to end.
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('Done.')


if __name__ == '__main__':
    main()
