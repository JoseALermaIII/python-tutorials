"""Prettified stopwatch

Expand :py:mod:`.P3_stopwatch` from this chapter so that it uses :meth:`str.rjust` and
:meth:`str.ljust` string methods to “prettify” the output.

Instead of output such as this::

    Lap #1: 3.56 (3.56)
    Lap #2: 8.63 (5.07)
    Lap #3: 17.68 (9.05)
    Lap #4: 19.11 (1.43)

... the output will look like this::

    Lap # 1:  3.56 (  3.56)
    Lap # 2:  8.63 (  5.07)
    Lap # 3: 17.68 (  9.05)
    Lap # 4: 19.11 (  1.43)

Next, use :py:mod:`pyperclip` to copy the text output to the clipboard
so the user can quickly paste the output to a text file or email.

"""


def main():
    import time
    import pyperclip

    # Display the program's instructions
    print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. "
          "Press CTRL-C to quit.")
    input()  # Press Enter to begin
    print('Started.')
    startTime = time.time()  # Get the first lap's start time
    lastTime = startTime
    lapNum = 1

    # Start tracking the lap times.
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)

            output = 'Lap #' + str(lapNum).rjust(2) + ':' + str(totalTime).rjust(6) + ' (' + str(lapTime).rjust(6) + ')'
            print(output, end='')
            pyperclip.copy(output)  # copy to clipboard

            lapNum += 1
            lastTime = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        # Handle the CTRL-C exception to keep its error message from displaying.
        print("\nDone.")


if __name__ == '__main__':
    main()
