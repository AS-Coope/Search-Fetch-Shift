import os
import sys
import shutil
import json
from os import path, listdir
from os.path import isfile, join

######## Directory path setup ########
# your desired source and destination directories are to be placed here respectively
# Example of file path: "C:\\Users\\your_user_name\\Downloads" [make sure that there are 2 backslashes]

## NOTE: The PUBLIC folder in the C drive is available to all users of the system ##
public_downloads = "C:\\Users\\Public\\Public Downloads"
public_documents = "C:\\Users\\Public\\Public Documents" 
directory_file = ".\\sample.json"
#src_dir = public_downloads
#dest_dir = public_documents
pdf_dest_dir = public_downloads
imgs_dest_dir = public_downloads
current_dir = os.getcwd()

######## Directory Existence Checks ########
def create_dest_dir(the_dest_dir):
    # creating the destination directory if it does not exist yet (as a failsafe)
    if not path.exists(the_dest_dir):
        os.makedirs(the_dest_dir)
        
def create_src_dir():
    # creating the source directory if it does not exist yet (as a failsafe)
    if not path.exists(src_dir):
        os.makedirs(src_dir)

def create_dir(dir):
    if not path.exists(dir):
        os.makedirs(dir)
        print(dir, "has been created.")

def check_same_src_dest_dir():
    if (imgs_dest_dir == dest_dir and pdf_dest_dir == dest_dir):
        create_dest_dir(dest_dir)
    else:
        create_dest_dir(imgs_dest_dir)
        create_dest_dir(pdf_dest_dir)

# creating the source directory and destination directories if they don't exist yet (as a failsafe)
#create_src_dir()
#check_same_src_dest_dir()

######## List Declarations for file storage ########
# lists to hold files and folders in src directory
#all_items_in_src = listdir(src_dir)
all_files_in_src = []

######## Business Logic for file shifting ########
def get_all_files(src_dir):
    # check for the existence of the src_dir using create_src_dir
    all_items_in_src = listdir(src_dir)
    for item in all_items_in_src:

        # getting all the files in the source directory
        if(isfile(join(src_dir, item))):
            all_files_in_src.append(item)

### obsolete method
'''
def shift_image_files(img_func_dest_dir):
    
    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( ('.jpg', '.png') ) ):
            shutil.move(join(src_dir, file), img_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", img_func_dest_dir, "!")
'''
### obsolete method
'''
def shift_pdf_files(pdf_func_dest_dir):

    # find all image files (specifically .jpg and .png)
    for file in all_files_in_src:
        # searching specifically for image files and MOVING them from the source directory to the destination directory 
        if ( join(src_dir, file).endswith( '.pdf' ) ):
            shutil.move(join(src_dir, file), pdf_func_dest_dir)
            print(file, "successfully moved from", src_dir, "to", pdf_func_dest_dir, "!")
'''
def shift_files(dest_dir, src_dir, file_ext):
    # Saves all files in the source directory in a list #
    get_all_files(src_dir)
    for file in all_files_in_src:
            # searching specifically for files of a specified file type/extension and MOVING them from the source directory to the destination directory 
            if ( join(src_dir, file).endswith( file_ext ) ):
                shutil.move(join(src_dir, file), dest_dir)
                print(file, "successfully moved from '", src_dir, "' to '", dest_dir, "'!")
    all_files_in_src.clear()


def exitProgram():
    print("Program now closing!")
    sys.exit()
######## Function Calls ########

# dictionary that selects a specific 'shift' function based on the user's choice in the main menu
'''option = {
    1: shift_image_files,
    2: shift_pdf_files,
    3: shift_files
}'''

# dictonary that selects the directory to push files to depending on the user's input
'''dest_dirs = {
    1 : imgs_dest_dir,
    2 : pdf_dest_dir
    #3 : dest_dir
}'''

saved_dirs = {}

def create_directory_store():
    if not os.path.exists(directory_file):
        json_data = json.dumps(saved_dirs)
        with open('sample.json', 'w') as file:
            file.write(json_data)
        print("Directory Store JSON file successfully created!")

def main_menu():
    print("|Search Fetch Shift")
    print("|1. Moves Image Files (.png, .jpg)")
    print("|2. Move PDF files (.pdf)")
    print("|3. Move files of another type")
    print("|4. Add a directory")
    print("|5. Look at directories")
    print("|0. Exit program")
    optionVal = int(input("|Enter the number beside the operation you want to perform: "))

    if (optionVal == 0):
        exitProgram()
    elif(optionVal == 3):
        # How this should work
        # First, ask the file type the user would like to move
        file_ext_input = input("Enter the file extension (Do not add the period in front of the extension)\n" + 
              "Example: to use text files, enter 'txt' instead of '.txt': ")
        #option[optionVal](dest_dirs[optionVal], file_ext_input)
        # Then, display all saved directories (name and actual path)
        # Ask, for the source directory
        # Then, ask the user if they would like to use an existing (saved) directory or use another one
        # If they want to use an existing directory, then they should choose from the list
        # If not, ask them if they would like to save the directory they are about to use
        # If yes, let them enter a name and the absolute path of the directory
        src_dir = input("Enter the path of the sending directory: ")
        create_dir(src_dir)
        print(src_dir)
        dest_dir = input("Enter the path of the receiving directory: ")
        create_dir(dest_dir)
        print(dest_dir)
        # For both src_dir and dest_dir, do failure checks to make sure the path is valid (starts with C:\, etc)
        # Will need to setup relevant functions to accept different paths depending on if the OS is Windows or Linux
        # There should be a design pattern that allows that accommodation
        shift_files(dest_dir, src_dir, file_ext_input)
        # Store that directory in the directory store JSON file
        # Use that directory to move the files and inform the user of the outcome of the operation
        # If not, ask for the absolute path of the directory alone
        # Set the dest_dir to the absolute path, then perform the operation to move files
        # informing the user of the outcome of the operation
    elif(optionVal == 4):
        dir_name = input("Please enter the directory name: ")
        dir_path = input("Please add the directory's absolute path: ")
        try:
            with open('sample.json', 'r') as openfile:
                # Reading from json file
                saved_dirs = json.load(openfile)
        
            saved_dirs[dir_name] = dir_path
            y = json.dumps(saved_dirs)
            print(y)
            with open("sample.json", "w") as outfile:
                outfile.write(y)
        except FileNotFoundError as e:
            print(e)
            print("An error occurred while trying to open the JSON file.")
            print("The file may not have been created.")
        

    elif(optionVal == 5):
        try:
            with open('sample.json', 'r') as openfile:
    
            # Reading from json file
                json_object = json.load(openfile)
    
                print(json_object)
                print(type(json_object))
            pass
        except FileNotFoundError as e:
            print(e)
            print("An error occurred while trying to open the JSON file.")
            print("The file may not have been created.")
    else:
        option[optionVal](dest_dirs[optionVal])

create_directory_store()
main_menu()
'''
Ask the user for a directory
Ask the user if they'd like to save the directory
If yes, prompt the user to assign a name
If no... don't save it...

Before shifting, ask the user if the directory is already saved
Present them a list of all directories, and give them the option to choose one
'''
#shift_image_files()
#shift_pdf_files()