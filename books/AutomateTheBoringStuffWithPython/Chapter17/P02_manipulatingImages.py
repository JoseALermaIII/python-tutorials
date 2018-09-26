# This program uses the pillow module to manipulate digital images

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
