"""Link verification

Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages that have a
404 “Not Found” status code and print them out as broken links.

"""


def main():
    import requests, bs4, os
    from urllib.request import urlretrieve

    # Fetch page
    res = requests.get("http://JoseALerma.com")
    res.raise_for_status()  # raise error if nothing fetched

    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Parse page for all links
    anchors = soup.find_all('a')
    links = []

    for anchor in anchors:
        link = anchor.get("href")
        if str(link).startswith("http"):
            links.append(link)

    # Add code 404 pages
    links.append("http://JoseALerma.com/potato")
    links.append("http://JoseALerma.com/carrot")

    # Download every linked page
    os.makedirs("pages", exist_ok=True)  # Save in ./pages

    for link in links:
        try:
            res = requests.head(link)  # Only fetch head tag for speed
            if res.status_code == 404:
                # Print code 404 pages
                print("Page not found: %s" % link)
            else:
                filepath = os.path.join("pages", os.path.basename(link + ".html"))
                urlretrieve(link, filepath)
        except requests.exceptions.ConnectionError:
            print("Unable to connect to: %s" % link)


if __name__ == '__main__':
    main()
