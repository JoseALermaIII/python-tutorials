#! python3
# P09_countdown.py - A simple countdown script.
#
# Note:
# - sound file can be downloaded from http://nostarch.com/automatestuff/

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['see', 'alarm.wav'])
