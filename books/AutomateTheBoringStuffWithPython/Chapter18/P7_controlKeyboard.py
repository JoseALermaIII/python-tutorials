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
