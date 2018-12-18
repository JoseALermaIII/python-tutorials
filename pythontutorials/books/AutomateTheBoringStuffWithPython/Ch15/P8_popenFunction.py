# This program uses the subprocess module's Popen function to launch programs

import subprocess

# Launching Other Programs from Python
calcProc = subprocess.Popen('/usr/bin/gnome-calculator')
print(calcProc.poll() is None)
print(calcProc.wait())
print(calcProc.poll())

# Passing Command Line Arguments to Popen()
subprocess.Popen(['/usr/bin/gedit', '/home/jose/Documents/Notepad.py'])  # Using Ubuntu 18.04

# Running Other Python Scripts
subprocess.Popen(['/usr/bin/python3',
                  '/home/jose/PycharmProjects/python-tutorials/pythontutorials/books/'
                  'AutomateTheBoringStuffWithPython/Ch01/P2_hello.py']).communicate()

# Opening Files with Default Applications
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['see', 'hello.txt'])
