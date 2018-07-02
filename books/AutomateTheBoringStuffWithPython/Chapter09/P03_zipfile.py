# This file manipulates a compressed file
import zipfile, os
os.chdir('./')  # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
# ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)  # in bytes
# 25
print(spamInfo.compress_size)  # in bytes
# 25
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
# Compressed file is 1.0x smaller!
exampleZip.close()
