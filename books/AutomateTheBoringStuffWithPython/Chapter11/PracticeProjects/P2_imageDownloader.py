# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting images.
# You could write a program that works with any photo site that has a search feature.

import requests, os, bs4
from selenium import webdriver, common

# Open Browser to photo-sharing site
url = "https://imgur.com/search?q="     # starting url
os.makedirs("images", exist_ok=True)    # store images in ./images

browser = webdriver.Firefox()

# Search for category of photos
browser.get(url + "Cats")

# Download all images
try:
    imageElems = browser.find_elements_by_css_selector("a.image-list-link")
    print(imageElems)
    for element in imageElems:
        downloadUrl = element.__getattribute__("href") + "#"
        # TODO: Save image to ./images
except common.exceptions.NoSuchElementException as err:
    print("Unable to locate element: %s" % err)
