"""Write logfile

This program raises an exception but outputs traceback to a logfile.

Note:
    Default logfile is ``errorInfo.txt``
"""


def main():
    import traceback

    try:
        raise Exception('This is the error message.')
    except Exception:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')


if __name__ == '__main__':
    main()
