import os
import shutil
from os import path, listdir
from os.path import isfile, join

# your desired source and destination directories are to be placed here respectively
# Example of file path: "C:\\Users\\your_user_name\\Downloads" [make sure that there are 2 backslashes]
src_dir = "C:\\Users\\Test_Downloads_Folders"
dest_dir = ""
pdf_dest_dir = "C:\\Users\\Test_Downloads_PDFs"
imgs_dest_dir = "C:\\Users\\Test_Downloads_Images"

def create_dest_dir(the_dest_dir):
    # creating the destination directory if it does not exist yet (as a failsafe)
    if not path.exists(the_dest_dir):
        os.makedirs(the_dest_dir)
        
def create_src_dir():
    # creating the source directory if it does not exist yet (as a failsafe)
    if not path.exists(src_dir):
        os.makedirs(src_dir)

# lists to hold files and folders in src directory
all_items_in_src = listdir(src_dir)
all_files_in_src = []

# creating the source directory if it does not exist yet (as a failsafe)
create_src_dir()

def get_all_files():
    for item in all_items_in_src:

        # getting all the files in the source directory
        if(isfile(join(src_dir, item))):
            all_files_in_src.append(item)

def shift_image_files(img_func_dest_dir):
    
    get_all_files()
    create_dest_dir(img_func_dest_dir)
    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( ('.jpg', '.png') ) ):
            shutil.move(join(src_dir, file), img_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", img_func_dest_dir, "!")

def shift_pdf_files(pdf_func_dest_dir):

    get_all_files()
    create_dest_dir(pdf_func_dest_dir)
    
    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( '.pdf' ) ):
            shutil.move(join(src_dir, file), pdf_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", pdf_func_dest_dir, "!")

shift_image_files()
shift_pdf_files()
