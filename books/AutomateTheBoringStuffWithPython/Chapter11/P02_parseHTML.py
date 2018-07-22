# This program uses requests to fetch an HTML page and BeautifulSoup to parse it

import requests, bs4

# Creating a BeautifulSoup Object from HTML
res = requests.get("http://nostarch.com")
res.raise_for_status()  # Raise error if nothing fetched
noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")  # Specify parser to avoid warning
print(type(noStarchSoup))

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "lxml")
print(type(exampleSoup))
