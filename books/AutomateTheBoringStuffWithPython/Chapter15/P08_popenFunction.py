# This program uses the subprocess module's Popen function to launch programs

import subprocess

# Launching Other Programs from Python
calcProc = subprocess.Popen('/usr/bin/gnome-calculator')
print(calcProc.poll() is None)
print(calcProc.wait())
print(calcProc.poll())
