# The resizeAndAddLogo.py program in this chapter works with PNG and JPEG files,
# but Pillow supports many more formats than just these two. Extend
# resizeAndAddLogo.py to process GIF and BMP images as well.
#
# Another small issue is that the program modifies PNG and JPEG files only if their
# file extensions are set in lowercase. For example, it will process zophie.png but
# not zophie.PNG. Change the code so that the file extension check is case insensitive.
#
# Finally, the logo added to the bottom-right corner is meant to be just a small mark,
# but if the image is about the same size as the logo itself, the result will look
# ugly. Modify resizeAndAddLogo.py so that the image must be at least
# twice the width and height of the logo image before the logo is pasted. Otherwise,
# it should skip adding the logo.
