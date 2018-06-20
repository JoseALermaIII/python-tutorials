# Write a program that opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.
#
# The results should be printed to the screen.
import os, re

# Get list of all .txt files
allfiles = os.listdir("./")  # use current working directory
textfiles = []
for file in allfiles:
    if file.endswith(".txt"):
        textfiles.append(file)

# Get regular expression
regex = input("Enter regular expression to search for: ")
searchregex = re.compile(regex)

# Open .txt file
for file in textfiles:
    inputfile = open(file)
    inputcontent = inputfile.readlines()
    inputfile.close()

    # Search for regex in file
    for line in inputcontent:
        matchobjects = searchregex.findall(line)
        if matchobjects is not None:
            # Print result
            for match in matchobjects:
                print(match)
