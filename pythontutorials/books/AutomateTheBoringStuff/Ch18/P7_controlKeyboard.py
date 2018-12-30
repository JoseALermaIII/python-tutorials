"""Control Keyboard

This program uses :py:mod:`PyAutoGUI` to manipulate keyboard input.

"""

import pyautogui, time


def commentAfterDelay() -> None:
    """Comment after delay

    Automatically types then comments out a line in IDLE after waiting two seconds.

    Returns:
        None. Executes keyboard commands.
        
    """
    pyautogui.click(100, 100)  # focus IDLE file editor
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt', '3')


def main():
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

    commentAfterDelay()


if __name__ == '__main__':
    main()
