# This program uses the PyAutoGUI module to control mouse interaction

import pyautogui

# Clicking the Mouse
# No delay, so don't blink
pyautogui.click(100, 150, button='left')
pyautogui.click(10, 5)
pyautogui.click(200, 250, button='right')
pyautogui.rightClick(20, 25)
pyautogui.click(300, 350, button='middle')
pyautogui.middleClick(30, 35)

pyautogui.mouseDown()  # pushes left button down at current location
pyautogui.mouseUp()  # releases left button at current location

pyautogui.doubleClick()  # double click left button

# Scrolling the Mouse
pyautogui.scroll(200)  # Units vary depending on OS and application

import books.AutomateTheBoringStuffWithPython.Chapter08.pyperclip as pyperclip  # imports should be at top of file
numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'
pyperclip.copy(numbers)  # 200 lines of numbers

time.sleep(5)
pyautogui.scroll(100)
