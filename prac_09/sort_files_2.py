import os
import shutil

os.chdir("FilesToSort")
extension_to_category = {}
for filename in os.listdir("."):
    extension_name = filename.split(".")[-1]
    if extension_name not in extension_to_category:
        input_category = input(f"What category would you like to sort {extension_name} files into? ")
        extension_to_category.update({extension_name: input_category})
        try:
            os.mkdir(input_category)
        except FileExistsError:
            pass
    shutil.move(filename, extension_to_category[extension_name])
