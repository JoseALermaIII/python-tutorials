#! python3
"""P5_backupToZip.py

Implements a function that copies an entire folder and its contents into
a ZIP file whose filename increments.

Note:
    Uses provided ``./delicious`` folder as a demonstration.

"""

import zipfile, os


def backupToZip(folder: str) -> None:
    """Backup to ZIP

    Copies given folder and its contents into a ZIP file with the name ``folder_#.zip``,
    where ``folder`` is the given folder and ``#`` is an incremented integer starting from
    ``1``.

    Args:
        folder: String with path to folder that is to be archived.
            Function automatically converts to absolute path, so relative paths are okay.

    Returns:
        None. Prints status updates and creates ZIP file in same folder as given folder.
    """
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % foldername)
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


def main():
    backupToZip('./delicious')


if __name__ == '__main__':
    main()
