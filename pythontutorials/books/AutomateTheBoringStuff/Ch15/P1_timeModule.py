"""Time module

This program uses :py:mod:`time` to reference the `Unix epoch`_ as a timestamp.

.. _Unix epoch:
    https://en.wikipedia.org/wiki/Unix_time
"""


def main():
    # The time.time() Function
    import time
    print(time.time())

    # The time.sleep() Function
    for i in range(3):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)

    time.sleep(5)

    for i in range(30):  # 30 second timer that can be CTRL-C'd from within IDLE
        time.sleep(1)

    # Rounding Numbers
    now = time.time()
    print(now)
    print(round(now, 2))
    print(round(now, 4))
    print(round(now))


if __name__ == '__main__':
    main()
