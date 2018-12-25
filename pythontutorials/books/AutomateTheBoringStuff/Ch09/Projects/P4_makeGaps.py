"""P4_makeGaps.py

Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).

Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered
files so that a new file can be added.

Note:
    By default, uses not provided `./testdir` and a gap of `2`.
"""

from pythontutorials.books.AutomateTheBoringStuff.Ch09.Projects.P3_fillGaps \
    import is_sequence, get_filenames, get_numbers

import os


def make_gaps(folder: str, gap: int) -> None:
    """Make gaps

    Makes given integer a gap in a sequence of numerical file names from a
    given folder.

    Args:
        folder: String containing path to folder to make gaps in file names.
            Relative paths are okay.
        gap: Integer number to make a gap.

    Returns:
        None. Prints applicable error message and renames files.

    Example:
        If folder `test` has files `text1.txt`, `text2.txt`, and `text3.txt`. Then,

        >>> make_gaps('test', 2)

        would change the file names to `text1.txt`, `text3.txt`, and `text4.txt`.

    Note:
        Running in debug mode. Files to be renamed are printed. Uncomment
        after testing to rename files.
    """
    # Get names of all files
    files = get_filenames(folder)

    # Get list of numbers used in file names
    numlist = get_numbers(files)

    # Check if there is a sequence
    if not is_sequence(numlist):
        print("There is already a gap in the files.")
        return None

    # Rename files after gap point to create gap
    files.sort(reverse=True)  # Start from end to prevent overwrites
    for file in files:
        prefix, number, suffix = file[0], file[1], file[2]
        if gap <= int(number):
            # Make file names
            numlen = len(number)
            oldfilename = ''.join(file)
            newfilename = prefix + str(int(number) + 1).zfill(numlen) + suffix

            # Get absolute paths
            workingdir = os.path.abspath(folder)
            oldfilepath = os.path.join(workingdir, oldfilename)
            newfilepath = os.path.join(workingdir, newfilename)

            # Rename file
            print("Renaming '%s' to '%s'..." % (oldfilename, newfilename))  # DEBUG
            #os.rename(oldfilepath, newfilepath)  # Uncomment after testing


def main():
    make_gaps("./testdir", 2)


# If P4_makeGaps.py is run instead of imported, run main():
if __name__ == "__main__":
    main()
