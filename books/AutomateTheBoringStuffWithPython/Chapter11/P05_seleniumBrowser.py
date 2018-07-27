# This program uses selenium to parse and interact with websites
#
# Note:
# - geckodriver is needed for Linux
#   - download from https://github.com/mozilla/geckodriver/releases
#   - place in /usr/local/bin
#   - more info https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst

from selenium import webdriver, common

# Starting a Selenium-Controlled Browser
browser = webdriver.Firefox()
print(type(browser))
browser.get("http://inventwithpython.com")

# Finding Elements on the Page
try:
    elem = browser.find_element_by_class_name("card-img-top")
    print("Found <%s> element with that class name!" % elem.tag_name)
except common.exceptions.NoSuchElementException as err:
    print("Unable to locate element: %s" % err)

# Clicking the Page
linkElem = browser.find_element_by_link_text("Read Online for Free")
print(type(linkElem))
linkElem.click()  # follows the "Read Online for Free" link

# Filling Out and Submitting Forms
browser.get("https://mail.yahoo.com")
emailElem = browser.find_element_by_id("login-username")
emailElem.send_keys("not_my_real_email")
emailElem.submit()
try:
    passwordElem = browser.find_element_by_id("login-passwd")
    passwordElem.send_keys("12345")
    passwordElem.submit()
except common.exceptions.NoSuchElementException as err:
    print("Unable to locate element: %s" % err)

# Sending Special Keys
from selenium.webdriver.common.keys import Keys  # Don't do this - imports should be at the top of the file
browser.get("http://nostarch.com")
htmlElem = browser.find_element_by_tag_name("html")
htmlElem.send_keys(Keys.END)  # scrolls to bottom
htmlElem.send_keys(Keys.HOME)  # scrolls to top

# Clicking Browser Buttons