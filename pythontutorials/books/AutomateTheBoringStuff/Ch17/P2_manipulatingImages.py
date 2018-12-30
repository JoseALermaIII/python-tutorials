"""Manipulating images

This program uses :py:mod:`PIL.Image` to manipulate digital images.

"""


def main():
    from PIL import Image
    catIm = Image.open('zophie.png')
    print(type(catIm))

    # Working with the Image Data Type
    print(catIm.size)
    width, height = catIm.size
    print(width)
    print(height)
    print(catIm.filename)
    print(catIm.format)
    print(catIm.format_description)
    catIm.save('zophie.jpg')

    im = Image.new('RGBA', (100, 200), 'purple')
    im.save('purpleImage.png')
    im2 = Image.new('RGBA', (20, 20))
    im2.save('transparentImage.png')

    # Cropping Images
    croppedIm = catIm.crop((335, 345, 565, 560))  # (origin-x, origin-y, x + 1, y + 1), where (x/y + 1) are exclusive
    croppedIm.save('cropped.png')

    # Copying and Pasting Images onto Other Images
    catIm = Image.open('zophie.png')
    catCopyIm = catIm.copy()

    faceIm = catIm.crop((335, 345, 565, 560))
    print(faceIm.size)
    catCopyIm.paste(faceIm, (0, 0))
    catCopyIm.paste(faceIm, (400, 500))
    catCopyIm.save('pasted.png')

    catImWidth, catImHeight = catIm.size
    faceImWidth, faceImHeight = faceIm.size
    catCopyTwo = catIm.copy()
    for left in range(0, catImWidth, faceImWidth):
        for top in range(0, catImHeight, faceImHeight):
            print(left, top)
            catCopyTwo.paste(faceIm, (left, top))
    catCopyTwo.save('tiled.png')

    # Resizing an Image
    width, height = catIm.size
    quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    quartersizedIm.save('quartersized.png')
    svelteIm = catIm.resize((width, height + 300))
    svelteIm.save('svelte.png')

    # Rotating and Flipping Images
    catIm.rotate(90).save('rotated90.png')  # counterclockwise rotations
    catIm.rotate(180).save('rotated180.png')
    catIm.rotate(270).save('rotated270.png')  # Sometimes uses black bars to fill gaps at 90° and 270°

    catIm.rotate(6).save('rotated6.png')
    catIm.rotate(6, expand=True).save('rotated6_expanded.png')  # fit image

    catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

    # Changing Individual Pixels
    im = Image.new('RGBA', (100, 100))
    print(im.getpixel((0, 0)))

    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210))

    from PIL import ImageColor  # Don't do this - imports should be at the top of the file
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

    print(im.getpixel((0, 0)))
    print(im.getpixel((0, 50)))
    im.save('putPixel.png')


if __name__ == '__main__':
    main()
