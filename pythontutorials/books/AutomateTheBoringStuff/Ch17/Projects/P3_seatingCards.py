"""Seating cards

Chapter 13 included a practice project to create custom invitations from a list of
guests in a plaintext file - :py:mod:`.P3_invitations`. As an additional project, use
:py:mod:`PIL` to create images for custom seating cards for your guests. For each of
the guests listed in ``guests.txt``, generate an image file with the guest's name and
some flowery decoration.

To ensure that each seating card is the same size, add a black rectangle on the edges
of the invitation image so that when the image is printed out, there will be a
guideline for cutting. The PNG files that :py:mod:`PIL.Image` produces are set
to 72 pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.

Note:
    * Flowery decoration from: http://www.reusableart.com/flower-02.html

"""


def main():
    import os
    from PIL import Image, ImageFont, ImageDraw

    GUEST_FILE = '../../Ch13/Projects/guests.txt'
    FLOWER_FILENAME = 'flower-02.png'
    OUTPUT_FOLDER = 'seatingCards'
    FONTS_FOLDER = '/usr/share/fonts/truetype'

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    # Get guest list from file
    with open(GUEST_FILE) as guest_list:
        guests = guest_list.read().splitlines()

    for guest in guests:
        # Open flowery decoration
        deco = Image.open(FLOWER_FILENAME)
        deco_width, deco_height = deco.size

        # Resize decoration if smaller than 4x5-inch card
        if deco_width < 288 or deco_height < 360:
            # Calculate the new width and height to resize to
            if deco_width > deco_height:
                deco_height = int((288 / deco_width) * deco_height)
                deco_width = 288
            else:
                deco_width = int((360 / deco_height) * deco_width)
                deco_height = 360
            print('Resizing decoration...')
            deco = deco.resize((deco_width, deco_height), Image.ANTIALIAS)
            deco = deco.convert(mode='L')  # Convert back to grayscale (if original image is grayscale)

        # Add guest's name
        draw = ImageDraw.Draw(deco)
        if u'\u014d' in guest:  # Replace ō with o since draw.textsize can't translate it
            guest = guest.replace(u'\u014d', 'o')
        text_width, text_height = draw.textsize(guest)
        font = ImageFont.truetype(os.path.join(FONTS_FOLDER, '/liberation/LiberationSerif-Regular.ttf'), 15)
        draw.text((int((deco_width - text_width) / 2), int((deco_height - text_height) / 2)), guest, fill='black'
                  , font=font)

        # Make black card with extra space for cutting
        image = Image.new('RGBA', (deco_width + 10, deco_height + 10), 'black')
        width, height = image.size

        # Add modified decoration to background
        image.paste(deco, (int((width - deco_width) / 2), int((height - deco_height) / 2)))

        # Save seating card
        filename = ''.join(filter(str.isalnum, guest)) + '.png'
        image.save(os.path.join(OUTPUT_FOLDER, filename))


if __name__ == '__main__':
    main()
