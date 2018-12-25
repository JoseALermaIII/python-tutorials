"""P2_deleteBigFiles.py

It’s not uncommon for a few unneeded but humongous files or folders to take up the
bulk of the space on your hard drive. If you’re trying to free up room on your
computer, you’ll get the most bang for your buck by deleting the most massive of
the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than 100MB.
(Remember, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.

Note:
    * ``testfile.txt`` was created by typing ``truncate -s 101M testfile.txt`` in terminal.
    * Defaults to current working directory and > 100 MiB files
"""

import os


def delete_big_files(folder: str = None, filesize: str = None) -> None:
    """Delete big files

    Checks files in given folder (and subfolders) for given filesize. If greater,
    file is deleted.

    Args:
        folder: String with folder to check files of. Relative paths are okay.
        filesize: Maximum allowed size for files in given folder.

    Returns:
        None. Deletes files.

    Raises:
        AttributeError: If `folder` or `filesize` are not given.

    Note:
        In debug mode - files to delete are printed to terminal.
        Uncomment after testing.
    """
    if folder is None:
        raise AttributeError('folder must be given.')
    if filesize is None:
        raise AttributeError('filesize must be given.')

    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(filename) > filesize:
                print(filename)  # DEBUG
                #os.unlink(filename)  # Uncomment after testing


def main():
    folder = "./"
    filesize = 100 * (1024 ** 2)  # Where (1024 ** 2) == 1 MiB

    delete_big_files(folder, filesize)


if __name__ == '__main__':
    main()
