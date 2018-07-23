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
browser.get("http://inventwithpython.com")

# Finding Elements on the Page
try:
    elem = browser.find_element_by_class_name("card-img-top")
    print("Found <%s> element with that class name!" % elem.tag_name)
except:
    print("Was not able to find an element with that name.")
