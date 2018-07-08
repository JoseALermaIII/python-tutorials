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


def get_gap(numberlist):
    seqlist = list(range(numberlist[0], numberlist[-1] + 1))
    for element in seqlist:
        if element not in numberlist:
            return element
    return None


def get_filenames(folder):
    files = []
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

            files.append([prefix, number, suffix])
    return files


def get_numbers(files):
    numlist = []
    for file in files:
        numlist.append(int(file[1]))
    return numlist


def fill_gaps(folder):
    files = get_filenames(folder)

    # Get list of numbers used in file names
    numlist = get_numbers(files)

    # Check if numbers are in sequence
    if is_sequence(numlist):
        print("There are no gaps to fill.")
        return None

    # Find gap in sequence
    gap = get_gap(numlist)

    # Rename files to close gap
    for file in files:
        prefix, number, suffix = file[0], file[1], file[2]
        if gap <= int(number):
            # Get file names
            numlen = len(number)
            oldfilename = ''.join(file)
            newfilename = prefix + str(gap).zfill(numlen) + suffix
            gap += 1

            # Get absolute paths
            workingdir = os.path.abspath(folder)
            oldfilepath = os.path.join(workingdir, oldfilename)
            newfilepath = os.path.join(workingdir, newfilename)

            # Rename file
            print("Renaming '%s' to '%s'..." % (oldfilename, newfilename))  # DEBUG
            #os.rename(oldfilepath, newfilepath)  # Uncomment after testing

    return None


def main():
    fill_gaps("./testdir")
    return None


# If P03_fillGaps.py is run instead of imported, run main():
if __name__ == "__main__":
    main()
