#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, time

print("Googling...")  # display text while downloading the Google page
res = requests.get("http://google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select(".r a")
numOpen = min(5, len(linkElems))
webbrowser.open("http://google.com" + linkElems[0].get("href"))
time.sleep(10)  # add delay for slow virtual machine
for i in range(1, numOpen):
    webbrowser.open_new_tab("http://google.com" + linkElems[i].get("href"))
    time.sleep(7)
