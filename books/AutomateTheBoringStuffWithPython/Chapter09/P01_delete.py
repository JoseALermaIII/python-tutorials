# This program permanently deletes files ending with a .txt extension
#
# Note:
# - Do not run this program for numerous reasons.
# - Demonstrates testing with delete functions
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)  # DEBUG
