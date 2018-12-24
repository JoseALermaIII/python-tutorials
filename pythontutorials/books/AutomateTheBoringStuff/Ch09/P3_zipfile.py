"""ZIP file

This program manipulates a compressed file using :py:mod:`zipfile` and :py:mod:`os`.

Note:
    Works with provided ZIP file ``example.zip``.

"""


def main():
    import zipfile, os
    os.chdir('./')  # move to the folder with example.zip
    exampleZip = zipfile.ZipFile('example.zip')

    # Reading ZIP Files
    print(exampleZip.namelist())
    # ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
    spamInfo = exampleZip.getinfo('spam.txt')
    print(spamInfo.file_size)  # in bytes
    # 25
    print(spamInfo.compress_size)  # in bytes
    # 25
    print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
    # Compressed file is 1.0x smaller!

    # Extracting from ZIP Files
    #exampleZip.extractall()  # extracts all files to current working directory
    exampleZip.extractall('./testdir')  # auto-creates folder
    exampleZip.close()

    # Creating and Adding to ZIP Files
    newZip = zipfile.ZipFile('new.zip', 'w')  # use 'a' to append
    newZip.write('./delicious/spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()


if __name__ == '__main__':
    main()
