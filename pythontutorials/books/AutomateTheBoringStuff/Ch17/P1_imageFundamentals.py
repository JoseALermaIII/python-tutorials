"""Image fundamentals

This program uses :meth:`PIL.ImageColor.getcolor` to convert color names to RGBA values.

"""


def main():
    # Colors and RGBA Values
    from PIL import ImageColor
    print(ImageColor.getcolor('red', 'RGBA'))
    print(ImageColor.getcolor('RED', 'RGBA'))
    print(ImageColor.getcolor('Black', 'RGBA'))
    print(ImageColor.getcolor('chocolate', 'RGBA'))
    print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))


if __name__ == '__main__':
    main()
