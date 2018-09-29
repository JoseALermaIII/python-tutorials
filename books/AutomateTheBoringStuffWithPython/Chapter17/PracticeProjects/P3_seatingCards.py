# Chapter 13 included a practice project to create custom invitations from a list of
# guests in a plaintext file. As an additional project, use the pillow module to
# create images for custom seating cards for your guests. For each of the guests listed
# in the guests.txt, generate an image file with the guest name and some flowery
# decoration.
#
# To ensure that each seating card is the same size, add a black rectangle on the edges
# of the invitation image so that when the image is printed out, there will be a
# guideline for cutting. The PNG files that Pillow produces are set to 72 pixels per
# inch, so a 4×5-inch card would require a 288×360-pixel image.

import os
from PIL import Image, ImageFont, ImageDraw

# Get guest list from file

# For each guest, make black 4x5-inch card

# Add guest's name

# Add flowery decoration

# Save seating card
