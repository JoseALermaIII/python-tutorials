#! python3
"""Mouse now 2.0

Extends :py:mod:`.P2_mouseNow` to display the mouse cursor's current position
and RGB color in terminal.

"""


def main():
    import pyautogui, os

    print('Press Ctrl-C to quit.')
    try:
        while True:
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        files = os.listdir('./')
        for file in files:
            if file.startswith('.screenshot'):
                os.remove(os.path.join('./', file))
        print('\nDone.')


if __name__ == '__main__':
    main()
