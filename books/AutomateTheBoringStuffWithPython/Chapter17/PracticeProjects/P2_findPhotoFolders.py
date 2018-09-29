#! python3
# P2_findPhotoFolders.py - This program identifies all folders with over
# 50% of images of a certain size.

import os
from PIL import Image

FOLDER = '/home/jose'
EXTENSIONS = ['.png', '.jpg', '.jpeg']
MIN_SIZE = 500

for foldername, subfolders, filenames in os.walk(FOLDER):
    photo_files = 0
    non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith(tuple(EXTENSIONS)):
            non_photo_files += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            image = Image.open(os.path.join(foldername, filename))
            width, height = image.size
        except OSError as instance:
            print(f'OSError: {instance}')
            continue  # skip to next filename

        # Check if width & height are larger than 500.
        if width > MIN_SIZE and height > MIN_SIZE:
            # Image is large enough to be considered a photo.
            photo_files += 1
        else:
            # Image is too small to be a photo.
            non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    total_files = photo_files + non_photo_files
    if photo_files > total_files / 2:
        print(f'Found folder: {foldername}')
