import os
import shutil

os.chdir("FilesToSort")

for filename in os.listdir("."):
    extension_name = filename.split(".")[-1]
    try:
        os.mkdir(extension_name)
    except FileExistsError:
        pass
    shutil.move(filename, extension_name)
