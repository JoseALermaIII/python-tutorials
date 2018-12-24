"""Delete

This program permanently deletes files ending with a .txt extension in the current directory
using :py:mod:`os`.

Note:
    Demonstrates testing/debugging using comments.

"""


def main():
    import os
    for filename in os.listdir('./'):
        if filename.endswith('.txt'):
            #os.unlink(filename)
            print(filename)  # DEBUG


if __name__ == '__main__':
    main()
