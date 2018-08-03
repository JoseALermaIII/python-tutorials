# 2048 is a simple game where you combine tiles by sliding them up, down, left, or
# right with the arrow keys. You can actually get a fairly high score by repeatedly
# sliding in an up, right, down, and left pattern over and over again.
# Write a program that will open the game at https://gabrielecirulli.github.io/2048/
# and keep sending up, right, down, and left keystrokes to automatically play the game.

from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://gabrielecirulli.github.io/2048/"

# Start Browser and go to 2048 game
browser = webdriver.Firefox()
browser.implicitly_wait(3)  # seconds
browser.get(url)

try:
    htmlElem = browser.find_element_by_tag_name("html")
    # Repeatedly send up, right, down, left
    while not browser.find_element_by_class_name("retry-button").is_displayed():
        htmlElem.send_keys(Keys.ARROW_UP)
        htmlElem.send_keys(Keys.ARROW_RIGHT)
        htmlElem.send_keys(Keys.ARROW_DOWN)
        htmlElem.send_keys(Keys.ARROW_LEFT)
    # Get current score and best score
    scoreElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "score-container")))
    score = scoreElem.text
    bestElem = browser.find_element_by_class_name("best-container")
    best = bestElem.text

    # Display current score and best score
    print("Current score: %s" % score)
    print("Best score: %s" % best)

except common.exceptions.NoSuchElementException as err:
    print("Unable to locate element: %s" % err)

# Close browser
browser.quit()
