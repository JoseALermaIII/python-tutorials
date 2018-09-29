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
#
# Note:
# - flowery decoration from: http://www.reusableart.com/flower-02.html

import os
from PIL import Image, ImageFont, ImageDraw

GUEST_FILE = '../../Chapter13/PracticeProjects/guests.txt'
FLOWER_FILENAME = 'flower-02.png'
OUTPUT_FOLDER = 'seatingCards'
FONTS_FOLDER = '/usr/share/fonts/truetype'

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
# Get guest list from file
with open(GUEST_FILE) as guest_list:
    guests = guest_list.read().splitlines()


for guest in guests:
    # Make black 4x5-inch card
    image = Image.new('RGBA', (288, 360), 'black')
    width, height = image.size

    # Add flowery decoration
    deco = Image.open(FLOWER_FILENAME)
    deco_width, deco_height = deco.size

    # Resize decoration if less than half of size of card
    if deco_width < width / 2 or deco_height < height / 2:
        # Calculate the new width and height to resize to
        if deco_width > deco_height:
            deco_height = int((width / deco_width) * deco_height)
            deco_width = width
        else:
            deco_width = int((height / deco_height) * deco_width)
            deco_height = height
        print('Resizing decoration...')
        deco = deco.resize((deco_width, deco_height))
    image.paste(deco, (int((width - deco_width) / 2), int((height - deco_height) / 2)))

    # Add guest's name
    draw = ImageDraw.Draw(image)
    if u'\u014d' in guest:  # Replace ō with o since draw.textsize can't translate it
        guest = guest.replace(u'\u014d', 'o')
    text_width, text_height = draw.textsize(guest)
    font = ImageFont.truetype(os.path.join(FONTS_FOLDER, '/liberation/LiberationSerif-Regular.ttf'), 15)
    draw.text((int((width - text_width) / 2), int((height - text_height) / 2)), guest, fill='gray'
              , font=font)  # FIXME: Not all names fit in decoration (e.g., Ed, John Jacob)
    # Save seating card
    filename = ''.join(filter(str.isalnum, guest)) + '.png'
    image.save(os.path.join(OUTPUT_FOLDER, filename))
