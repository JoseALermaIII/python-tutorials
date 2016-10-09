#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

import subprocess
def main():
    try:
        print("this small program invokes the print function in the Notepad application")
        #Lets print the file we created in the program above
        subprocess.call(['notepad', '/p', 'numbers.txt'])
    except WindowsError:
        print("The called subprocess does not exist, or cannot be called.")

main()
