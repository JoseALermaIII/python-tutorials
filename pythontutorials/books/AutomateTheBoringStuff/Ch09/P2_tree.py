"""Tree

This program walks a directory tree and prints the contents.

Note:
    Walks the ``./delicious`` directory.

"""


def main():
    import os

    for folderName, subfolders, filenames in os.walk('./delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)

        print('')


if __name__ == '__main__':
    main()
