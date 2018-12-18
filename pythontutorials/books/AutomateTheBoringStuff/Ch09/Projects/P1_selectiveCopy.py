# Write a program that walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import os, shutil

FOLDER = "../"
EXTENSION = ".zip"
NEW_FOLDER = "new_folder"

os.chdir(FOLDER)
os.mkdir(NEW_FOLDER)
# Walk through a folder tree
for foldername, subfolders, filenames in os.walk("./"):
    print("Looking in folder: %s..." % foldername)
    # Find files with a specific extension
    for filename in filenames:
        if filename.endswith(EXTENSION):
            # Copy files to a new folder
            print("Copying file: %s..." % filename)
            shutil.copy(filename, NEW_FOLDER)
print("Done.")
