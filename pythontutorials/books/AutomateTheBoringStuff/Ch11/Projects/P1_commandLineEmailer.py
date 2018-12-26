"""Command line emailer

Write a program that takes an email address and string of text on the command line
and then, using Selenium, logs into your email account and sends an email of the
string to the provided address.
(You might want to set up a separate email account for this program.)

Note:
    * "string of text" must be within quotes, like shown
    * "new" gmail layout is used with keyboard shortcuts enabled
    * not fully tested because account could end up banned for going against TOS

"""


def main():
    import sys
    from selenium import webdriver, common
    from selenium.webdriver.common.keys import Keys

    # Get arguments from command line
    email = ''.join(sys.argv[1])
    message = ''.join(sys.argv[2])

    # Open browser to email account
    browser = webdriver.Firefox()
    browser.get("https://www.gmail.com/")

    # Login to e-mail account
    try:
        emailElem = browser.find_element_by_id("identifierId")
        emailElem.send_keys("not_my_real_email")
        emailElem.submit()

        passwordElem = browser.find_element_by_name("password")
        passwordElem.send_keys("not_my_real_password")
        passwordElem.submit()
    except common.exceptions.NoSuchElementException as err:
        print("Unable to locate element: %s" % err)

    # Open new message and fill To and Message fields
    try:
        buttonElem = browser.find_element_by_link_text("Compose")
        buttonElem.submit()

        toElem = browser.find_element_by_name("to")
        toElem.send_keys(email)

        subjectElem = browser.find_element_by_name("subjectbox")
        subjectElem.send_keys("Auto Generated Message")

        messageElem = browser.find_element_by_id(":ia")
        messageElem.send_keys(message)

        # Send e-mail with keyboard shortcut
        subjectElem.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)
    except common.exceptions.NoSuchElementException as err:
        print("Unable to locate element: %s" % err)

    # Close browser
    browser.quit()


if __name__ == '__main__':
    main()
