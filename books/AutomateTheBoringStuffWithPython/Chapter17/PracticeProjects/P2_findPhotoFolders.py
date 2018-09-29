#! python3
# P2_findPhotoFolders.py - This program identifies all folders with over
# 50% of images of a certain size.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    photo_files = 0
    non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if TODO:
            non_photo_files += 1
            continue    # skip to next filename

        # Open image file using Pillow.

        # Check if width & height are larger than 500.
        if TODO:
            # Image is large enough to be considered a photo.
            photo_files += 1
        else:
            # Image is too small to be a photo.
            non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if TODO:
        print(TODO)
