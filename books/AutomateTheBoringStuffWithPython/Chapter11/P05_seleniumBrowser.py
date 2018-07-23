# This program uses selenium to parse and interact with websites
#
# Note:
# - geckodriver is needed for Linux
#   - download from https://github.com/mozilla/geckodriver/releases
#   - place in /usr/local/bin
#   - more info https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst

from selenium import webdriver

# Starting a Selenium-Controlled Browser
browser = webdriver.Firefox()
print(type(browser))
