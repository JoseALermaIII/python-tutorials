# Write a program that finds all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
#
# Have the program rename all the later files to close this gap.

import os, re

seqRegex = re.compile(r"""
                      ^(.*?)    # All text before numbering
                      (\d+)     # One or more numbers
                      (.*?)$    # All text after numbering
                      """, re.VERBOSE)


def is_sequence(numberlist):
    return len(numberlist) == (numberlist[-1] - numberlist[0] + 1)


def fill_gaps(folder):
    # Get list of numbers used in file names
    numlist = []
    for foldername, subfolders, filenames in os.walk(folder):
        filenames.sort()
        for filename in filenames:
            match_object = seqRegex.search(filename)

            # Skip files without numbering
            if match_object is None:
                continue

            # Get numbers
            number = match_object.group(2)
            numlist.append(int(number))

    # Check if numbers are in sequence
    if is_sequence(numlist):
        print("There are no gaps to fill.")
        return None

    # TODO: Determine missing number in sequence
    sequence = list(range(numlist[0], numlist[-1] + 1))

    # TODO: Rename folders
    for foldername, subfolders, filenames in os.walk(folder):
        filenames.sort()
        for filename in filenames:
            match_object = seqRegex.search(filename)

            # Skip files without numbering
            if match_object is None:
                continue

            # Get parts of filename
            prefix = match_object.group(1)
            number = match_object.group(2)
            suffix = match_object.group(3)


def main():
    fill_gaps("./testdir")
    return None


# If P03_fillGaps.py is run instead of imported, run main():
if __name__ == "__main__":
    main()
