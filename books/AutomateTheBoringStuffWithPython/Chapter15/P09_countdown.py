#! python3
# P09_countdown.py - A simple countdown script.
#
# Note:
# - sound file can be downloaded from http://nostarch.com/automatestuff/

import time, subprocess, sys

# Get timeLeft from command line arguments
if len(sys.argv) < 2:
    print('Usage: P09_countdown.py seconds')
    sys.exit()
timeLeft = int(sys.argv[1])

while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['see', 'alarm.wav'])
