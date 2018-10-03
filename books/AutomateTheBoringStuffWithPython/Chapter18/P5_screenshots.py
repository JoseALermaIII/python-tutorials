# This program uses the PyAutoGUI module to take and analyze screenshots
#
# Note:
# - for Linux distros, the scrot program needs to be installed

import pyautogui

# Getting a Screenshot
im = pyautogui.screenshot()

print(im.getpixel((0, 0)))  # returns RGB tuple of pixel
print(im.getpixel((50, 200)))

# Analyzing the Screenshot
im.getpixel((50, 200))  # identify RGB to match
print(pyautogui.pixelMatchesColor(50, 200, (64, 0, 193)))
print(pyautogui.pixelMatchesColor(50, 200, (65, 0, 193)))
