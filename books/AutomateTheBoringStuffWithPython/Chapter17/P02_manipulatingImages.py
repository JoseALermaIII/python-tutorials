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
