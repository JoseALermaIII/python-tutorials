"""Looking busy

Write a script to nudge your mouse cursor slightly every ten seconds.
The nudge should be small enough so that it won’t get in the way if
you do happen to need to use your computer while the script is running.

"""

import pyautogui, time


def main():
    while True:
        time.sleep(10)
        pyautogui.moveRel(1, 0)


# If run directly (instead of imported), run main()
if __name__ == '__main__':
    main()
