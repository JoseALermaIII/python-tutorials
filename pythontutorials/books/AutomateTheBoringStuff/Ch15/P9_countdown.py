#! python3
"""Countdown

A simple countdown script that plays an alarm after a given number of seconds.

Note:
    * Sound file can be downloaded from http://nostarch.com/automatestuff/

"""


def main():
    import time, subprocess, sys

    # Get timeLeft from command line arguments
    if len(sys.argv) < 2:
        print('Usage: P9_countdown.py seconds')
        sys.exit()
    timeLeft = int(sys.argv[1])

    while timeLeft > 0:
        print(timeLeft)
        time.sleep(1)
        timeLeft -= 1

    # At the end of the countdown, play a sound file.
    subprocess.Popen(['see', 'alarm.wav'])


if __name__ == '__main__':
    main()
