# Write a program that checks the websites of several web comics and automatically
# downloads the images if the comic was updated since the program’s last visit.
#
# Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X,
# and cron on Linux) can run your Python program once a day.
#
# The Python program itself can download the comic and then copy it to your desktop
# so that it is easy to find. This will free you from having to check the website
# yourself to see whether it has updated.

import os, requests, bs4, datetime, shelve

# Download page

# Compare page's timestamp to shelve's

# Download comic to desktop

# Repeat for next URL
