# This program permanently deletes files ending with a .txt extension
#
# Note:
# - Demonstrates testing with delete functions
import os
for filename in os.listdir('./'):
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)  # DEBUG
