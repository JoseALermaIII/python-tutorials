"""Parse HTML

This program uses :py:mod:`requests` to fetch an HTML page and :py:mod:`bs4` to parse it.

"""


def main():
    import requests, bs4

    # Creating a BeautifulSoup Object from HTML
    res = requests.get("http://nostarch.com")
    res.raise_for_status()  # Raise error if nothing fetched
    noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")  # Specify parser to avoid warning
    print(type(noStarchSoup))

    exampleFile = open("example.html")
    exampleSoup = bs4.BeautifulSoup(exampleFile, "lxml")
    print(type(exampleSoup))

    # Finding an Element with the select() Method
    exampleFile = open("example.html")
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
    elems = exampleSoup.select("#author")
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)

    pElems = exampleSoup.select('p')
    print(str(pElems[0]))
    print(pElems[0].getText())
    print(str(pElems[1]))
    print(pElems[1].getText())
    print(str(pElems[2]))
    print(pElems[2].getText())

    # Getting Data from an Element's Attributes
    soup = bs4.BeautifulSoup(open("example.html"), "lxml")
    spanElem = soup.select('span')[0]
    print(str(spanElem))
    print(spanElem.get("id"))
    print(spanElem.get("some_nonexistent_addr") is None)
    print(spanElem.attrs)


if __name__ == '__main__':
    main()
