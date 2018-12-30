#! python3
"""Form filler

Automatically fills in the form at http://autbor.com/form

"""


def main():
    import pyautogui, time

    # Set these to the correct coordinates for your computer.
    nameField = (494, 298)
    submitButton = (468, 658)
    submitButtonColor = (76, 142, 251)  # Must match exact colors of above coordinates
    submitAnotherLink = (562, 236)

    formData = [{'name': 'Alice', 'fear': 'eavesdropers', 'source': 'wand',
                 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
                {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
                 'comments': 'n/a'},
                {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
                 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
                {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
                 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
                ]

    pyautogui.PAUSE = 0.5

    for person in formData:
        # Give the user a chance to kill the script.
        print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(5)

        # Wait until the form page has loaded.
        while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
                                              submitButtonColor):
            time.sleep(0.5)

        print('Entering %s info...' % (person['name']))
        pyautogui.click(nameField[0], nameField[1])

        # Fill out the Name Field.
        pyautogui.typewrite(person['name'] + '\t')

        # Fill out the Greatest Fear(s) field.
        pyautogui.typewrite(person['fear'] + '\t')

        # Fill out the Source of Wizard Powers field.
        source = person['source']
        if source == 'wand':
            pyautogui.typewrite(['down', '\t'])
        elif source == 'amulet':
            pyautogui.typewrite(['down', 'down', '\t'])
        elif source == 'crystal ball':
            pyautogui.typewrite(['down', 'down', 'down', '\t'])
        elif source == 'money':
            pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

        # Fill out the RoboCop field.
        robocop = person['robocop']
        if robocop == 1:
            pyautogui.typewrite([' ', '\t'])
        elif robocop == 2:
            pyautogui.typewrite(['right', '\t'])
        elif robocop == 3:
            pyautogui.typewrite(['right', 'right', '\t'])
        elif robocop == 4:
            pyautogui.typewrite(['right', 'right', 'right', '\t'])
        elif robocop == 5:
            pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

        # Fill out the Additional Comments field.
        pyautogui.typewrite(person['comments'] + '\t')

        # Click Submit.
        pyautogui.press('enter')

        # Wait until form page has loaded.
        print('Clicked Submit.')
        time.sleep(5)

        # Click the Submit another response link.
        pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])


if __name__ == '__main__':
    main()
