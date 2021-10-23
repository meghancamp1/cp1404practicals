"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Cleanup file names so they are consistent. """
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            directory_and_new_name = os.path.join(directory_name, new_name)
            directory_and_file_name = os.path.join(directory_name, filename)
            print("Renaming {} to {}".format(filename, new_name))
            # os.rename(directory_and_file_name, directory_and_new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
