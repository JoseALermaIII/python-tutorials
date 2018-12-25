"""P3_fillGaps.py

Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).

Have the program rename all the later files to close this gap.

Attributes:
    seqRegex (re.compile): Regular expression object used to group numbers in
        filename.
"""

import os, re

seqRegex = re.compile(r"""
                      ^(.*?)    # All text before numbering
                      (\d+)     # One or more numbers
                      (.*?)$    # All text after numbering
                      """, re.VERBOSE)


def is_sequence(numberlist: list) -> bool:
    """Is sequence

    Can take a list returned by :meth:`get_numbers` and determine if
    it is a sequence based on the property
    ``list_length == (last_element - first_element + 1)``.

    Args:
        numberlist: List containing integers to check for a sequence.

    Returns:
        True if list contains a sequence of numbers, False otherwise.
    """
    return len(numberlist) == (numberlist[-1] - numberlist[0] + 1)


def get_gap(numberlist: list):
    """Get gap

    Can take an integer list returned by :meth:`get_numbers` and determine
    the missing sequence number.

    Args:
        numberlist: List of numbers to find a gap in.

    Returns:
        Missing number in the sequence or None if there is no gap.
    """
    seqlist = list(range(numberlist[0], numberlist[-1] + 1))
    for element in seqlist:
        if element not in numberlist:
            return element
    return None


def get_filenames(folder: str) -> list:
    """Get file names

    Called by :meth:`fill_gaps` to makes a list of all numbered
    file names in a given folder.

    Breaks each file into the prefix (before numbering), numbering,
    and suffix (after numbering).

    Args:
        folder: String containing folder path to get file names of.
            Relative paths are okay.

    Returns:
        List of lists of strings with segmented names of files in
        alphanumerical order.
    """
    folder = os.path.abspath(folder)
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


def get_numbers(files: list) -> list:
    """Get numbers

    Can take a list returned by :meth:`get_filenames` and make
    an integer list of the numerical parts of the file names.

    Args:
        files: List of segmented file names.

    Returns:
        List of integers from file names in numerical order.
    """
    numlist = []
    for file in files:
        numlist.append(int(file[1]))
    return numlist


def fill_gaps(folder: str) -> None:
    """Fill gaps

    Fills gaps in file name numbering of a given folder.

    Args:
        folder: String containing path of folder to fill filename gaps.
            Relative paths are okay.

    Returns:
        None. Prints applicable error message and renames files.

    Note:
        Running in debug mode. Files to be renamed are printed. Uncomment
        after testing to rename files.
    """
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
            # Make file names
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


def main():
    fill_gaps("./testdir")


# If P3_fillGaps.py is run instead of imported, run main():
if __name__ == "__main__":
    main()
