# This program uses the PyAutoGUI module to control mouse movement

import pyautogui

# Pauses and Fail-Safes
pyautogui.PAUSE = 1  # pause 1 second for every pyautogui function call
pyautogui.FAILSAFE = True  # cause FailSafeException by moving mouse cursor to upper-left corner

# Moving the Mouse
print(pyautogui.size())
width, height = pyautogui.size()

for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

# Getting the Mouse Position
print(pyautogui.position())
print(pyautogui.position())
print(pyautogui.position())
