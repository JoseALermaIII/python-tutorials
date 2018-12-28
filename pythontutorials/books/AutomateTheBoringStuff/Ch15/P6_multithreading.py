"""Multithreading

This program demonstrates :class:`threading.Thread` on :func:`print`.

"""


def main():
    import threading

    # Passing Arguments to the Thread's Target Function
    threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
    threadObj.start()


if __name__ == '__main__':
    main()
