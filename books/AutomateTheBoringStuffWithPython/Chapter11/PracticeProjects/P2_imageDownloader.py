# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting images.
# You could write a program that works with any photo site that has a search feature.

import requests, os, bs4
from selenium import webdriver, common

# Open Browser to photo-sharing site
url = "https://imgur.com"               # starting url
os.makedirs("images", exist_ok=True)    # store images in ./images

browser = webdriver.Firefox()
browser.get(url)

# Search for category of photos

# Download all images
