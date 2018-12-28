"""Thread demo

This program uses :py:mod:`threading` to demonstrate multithreading.

"""

import time
print('Start of program.')


def takeANap() -> None:
    """Take a nap

    Simple 5 second timer using :func:`time.sleep` followed by a 'Wake up!' print statement.

    Returns:
        None. Waits 5 seconds, then prints an exclamation.
    """
    time.sleep(5)
    print('Wake up!')


def main():
    import threading
    threadObj = threading.Thread(target=takeANap)
    threadObj.start()

    print('End of program.')


if __name__ == '__main__':
    main()
