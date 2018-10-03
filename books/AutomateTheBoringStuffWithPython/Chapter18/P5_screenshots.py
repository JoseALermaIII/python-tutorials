# This program uses the PyAutoGUI module to take and analyze screenshots
#
# Note:
# - for Linux distros, the scrot program needs to be installed

import pyautogui

# Getting a Screenshot
im = pyautogui.screenshot()

print(im.getpixel((0, 0)))  # returns RGB tuple of pixel
print(im.getpixel((50, 200)))
