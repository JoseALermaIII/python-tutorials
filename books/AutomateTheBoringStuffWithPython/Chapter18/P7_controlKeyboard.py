# This program uses the PyAutoGUI module to manipulate keyboard input

import pyautogui
# Sending a String from the Keyboard
pyautogui.click(100, 100)  # put file editor in focus
pyautogui.typewrite('Hello world!')
pyautogui.typewrite('!dlrow olleH', 0.25)

# Key Names
pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'])

# Press and Release Keyboard Keys
pyautogui.press('end')
pyautogui.press('enter')
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

# Hotkey Combinations
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

pyautogui.hotkey('ctrl', 'c')

import time  # imports should be at the top of the file


def commentAfterDelay():
    pyautogui.click(100, 100)  # focus IDLE file editor
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt', '3')


commentAfterDelay()
