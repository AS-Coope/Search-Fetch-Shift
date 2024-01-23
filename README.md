# Search Fetch Shift (SFS)
This is a command line application that allows you to move files of similar file type from one directory to the next, all at once!

## Motivation

Sometimes, when users want to do something very quickly with a file they need to download, they download and use it, but forget to move it to the desired folder they intended to move it to. Eventually, when searching for it, they realize that they can't find it. This gets even more cumbersome when there are many files to move and you have to search for each of them across varying dates in the file explorer.

Inspired by this [video](https://www.youtube.com/watch?v=vGxR98gI930), around 40 seconds in, [Internet Made Coder](https://www.youtube.com/@InternetMadeCoder) talks about making a Python Automation Script, and something he mentions would be a solution to the problem I had mentioned earlier, which is moving files to where I want them to actually reside on disk.   
And even more recently, in trying to create a [mobile app that replicates a Generation 1 PokéDex](https://github.com/AS-Coope/Gen1Dex), I realized I'd have to be moving a lot of images around. And those situations combined gave birth to this project.

Additionally, I stumbled upon this [project](https://github.com/brentvollebregt/auto-py-to-exe) which has inspired me to see this through long-term (at least to get a good looking graphical user interface up alongside, hopefully, quality code).

## Usage:
IMPORTANT NOTICE: This is being developed and tested on a device operating with a Windows OS. As such, it may not work as desired on Linux, Mac or other operating systems.
- Download and install [Python](https://www.python.org/downloads/) (ensure it is added to [PATH](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/)).
- Clone this repository to your machine.
- Open your favourite text editor/IDE and be sure to add the source directory (where the images you want to move currently reside) and the destination directory (where you want your images to be) absolute paths for the corresponding variables (please follow the format specified in the code in providing the path).
- Open command prompt and navigate to the directory where the code is housed. Alternatively, you can click in the address bar of that directory, type cmd and press Enter to open the command prompt to that file path.
- Type: ```python search_fetch_shift.py``` and press Enter.

## Deliverables
For v1.0:
- [X] The software shall allow the user to move files of the same file type from one directory to another.

For v1.5
- [ ] The software shall allow the user to copy files of the same file type from one directory to another.
- [ ] The software shall provide the user with a set of commonly used file types for them to choose from when
deciding which files to move.
- [ ] The software shall allow the user to enter a specific file type.

For v2.0
- [ ] The software shall allow the user to store regularly used (whether as a source or destination) directory paths and store them persistently.
- [ ] The software shall allow the user to choose the directory (whether source or destination) via a dialog box 
(file explorer).
- [ ] The software shall determine the user's Operating System and operate on directories based on the file system structure.
- [ ] Create a test suite to ensure proper functionality of all features.