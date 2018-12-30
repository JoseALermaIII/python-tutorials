#! python3
"""Spiral draw

Program uses :py:mod:`PyAutoGUI` to draw a spiral pattern in an opened drawing program.

"""


def main():
    import pyautogui, time
    time.sleep(5)
    pyautogui.click()  # click to put drawing program in focus
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)  # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)  # move up


if __name__ == '__main__':
    main()
