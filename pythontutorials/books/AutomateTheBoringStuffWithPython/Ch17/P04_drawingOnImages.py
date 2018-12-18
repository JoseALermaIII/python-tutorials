# This program uses the pillow module to draw on digital images

from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# Drawing Shapes
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('drawing.png')

# Drawing Text
from PIL import ImageFont  # Don't do this - imports should be at the top of the file
import os

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = '/usr/share/fonts/truetype'  # e.g. 'Library/Fonts' on OS X
liberationFont = ImageFont.truetype(os.path.join(fontsFolder, '/liberation/LiberationSerif-Regular.ttf')
                                    , 32)  # where font size is in points and 1 point is 1/72 of an inch
draw.text((100, 150), 'Howdy', fill='gray', font=liberationFont)
im.save('text.png')
