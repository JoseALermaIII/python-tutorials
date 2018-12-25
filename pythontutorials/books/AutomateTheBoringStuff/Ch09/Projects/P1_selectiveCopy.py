"""Selective copy

Write a function, :meth:`selective_copy`, that walks through a folder tree and
searches for files with a certain file extension (such as .pdf or .jpg). Copy
these files from whatever location they are in to a new folder.

Note:
    Defaults are to check parent directory for `.zip` files and put them in a
    folder called `new_folder`.
"""

import os, shutil


def selective_copy(src_folder: str = None, ext: str = None, dest_folder: str = None) -> None:
    """Selective copy

    Searches for given extension in given source folder (and sub folders) then copies files
    to given destination folder.

    Args:
        src_folder: String with path to source folder. Relative paths are okay.
        ext: Extension to look for in source folder.
        dest_folder: String with name of destination folder.

    Returns:
        None. Prints status messages and makes copies within destination folder.

    Raises:
        AttributeError: If `src_folder`, `ext`, or `dest_folder` are not given.

    Note:
        Destination folder is made inside source folder. Absolute path of source folder is
        automatically found.
    """
    if src_folder is None:
        raise AttributeError('src_folder must be given.')
    if ext is None:
        raise AttributeError('ext must be given.')
    if dest_folder is None:
        raise AttributeError('dest_folder must be given.')

    src_folder = os.path.abspath(src_folder)
    os.chdir(src_folder)
    os.mkdir(dest_folder)
    # Walk through a folder tree
    for foldername, subfolders, filenames in os.walk("./"):
        print("Looking in folder: %s..." % foldername)
        # Find files with a specific extension
        for filename in filenames:
            if filename.endswith(ext):
                # Copy files to a new folder
                print("Copying file: %s..." % filename)
                shutil.copy(filename, dest_folder)
    print("Done.")


def main():
    selective_copy('../', '.zip', 'new_folder')


if __name__ == '__main__':
    main()
