import os
import shutil
from os import path, listdir
from os.path import isfile, join

######## Directory path setup ########
# your desired source and destination directories are to be placed here respectively
# Example of file path: "C:\\Users\\your_user_name\\Downloads" [make sure that there are 2 backslashes]

## NOTE: The PUBLIC folder in the C drive is available to all users of the system ##
src_dir = "C:\\Users\\Public\\Public Downloads"
dest_dir = "C:\\Users\\Public\\Public Documents"
pdf_dest_dir = "C:\\Users\\Public\\Public Documents"
imgs_dest_dir = "C:\\Users\\Public\\Public Documents"

######## Directory Existence Checks ########
def create_dest_dir(the_dest_dir):
    # creating the destination directory if it does not exist yet (as a failsafe)
    if not path.exists(the_dest_dir):
        os.makedirs(the_dest_dir)
        
def create_src_dir():
    # creating the source directory if it does not exist yet (as a failsafe)
    if not path.exists(src_dir):
        os.makedirs(src_dir)

def check_same_src_dest_dir():
    if (imgs_dest_dir == dest_dir and pdf_dest_dir == dest_dir):
        create_dest_dir(dest_dir)
    else:
        create_dest_dir(imgs_dest_dir)
        create_dest_dir(pdf_dest_dir)

# creating the source directory and destination directories if they don't exist yet (as a failsafe)
create_src_dir()
check_same_src_dest_dir()

######## List Declarations for file storage ########
# lists to hold files and folders in src directory
all_items_in_src = listdir(src_dir)
all_files_in_src = []

######## Business Logic for file shifting ########
def get_all_files():
    for item in all_items_in_src:

        # getting all the files in the source directory
        if(isfile(join(src_dir, item))):
            all_files_in_src.append(item)

######## Saves all files in the source directory in a list ########
get_all_files()

def shift_image_files(img_func_dest_dir):
    
    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( ('.jpg', '.png') ) ):
            shutil.move(join(src_dir, file), img_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", img_func_dest_dir, "!")

def shift_pdf_files(pdf_func_dest_dir):

    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( '.pdf' ) ):
            shutil.move(join(src_dir, file), pdf_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", pdf_func_dest_dir, "!")

######## Function Calls ########

# dictionary that selects a specific 'shift' function based on the user's choice in the main menu
option = {
    1: shift_image_files,
    2: shift_pdf_files
}

# dictonary that selects the directory to push files to depending on the user's input
dest_dirs = {
    1 : imgs_dest_dir,
    2 : pdf_dest_dir
}

def main_menu():
    print("|Search Fetch Shift")
    print("|1. Moves Image Files (.png, .jpg)")
    print("|2. Move PDF files (.pdf)")
    optionVal = int(input("|Enter the number beside the operation you want to perform: "))
    option[optionVal](dest_dirs[optionVal])

main_menu()    
#shift_image_files()
#shift_pdf_files()
