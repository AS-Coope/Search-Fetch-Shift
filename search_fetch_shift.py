import os
import shutil
from os import path, listdir
from os.path import isfile, join

# your desired source and destination directories are to be placed here respectively
# Example of file path: "C:\\Users\\your_user_name\\Downloads" [make sure that there are 2 backslashes]
src_dir = ""
dest_dir = ""

# lists to hold files and folders in src directory
all_items_in_src = listdir(src_dir)
all_files_in_src = []

def get_all_files():
    for item in all_items_in_src:

        # getting all the files in the source directory
        if(isfile(join(src_dir, item))):
            all_files_in_src.append(item)

def shift_image_files():

    # creating the destination directory if it does not exist yet (as a failsafe)
    if not path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    get_all_files()

    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( ('.jpg', '.png') ) ):
            shutil.move(join(src_dir, file), dest_dir)
            print(file, "successfully moved from", src_dir, "to", dest_dir, "!")

shift_image_files()
