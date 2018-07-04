# t’s not uncommon for a few unneeded but humongous files or folders to take up the
# bulk of the space on your hard drive. If you’re trying to free up room on your
# computer, you’ll get the most bang for your buck by deleting the most massive of
# the unwanted files. But first you have to find them.
#
# Write a program that walks through a folder tree and searches for exceptionally
# large files or folders—say, ones that have a file size of more than 100MB.
# (Remember, to get a file’s size, you can use os.path.getsize() from the os module.)
# Print these files with their absolute path to the screen.
#
# Note:
# - testfile.txt was created by typing truncate -s 101M testfile.txt in a terminal

import os

FOLDER = "./"
FILESIZE = 100 * (1024 ** 2)  # 1024 ** 2 == 1 MB

for foldername, subfolders, filenames in os.walk(FOLDER):
    for filename in filenames:
        if os.path.getsize(filename) > FILESIZE:
            #os.unlink(filename)
            print(filename)  # DEBUG
