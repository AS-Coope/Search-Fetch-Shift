# Search Fetch Shift (SFS)
This is a command-line application that allows you to move files of similar file type from one directory to the next, all at once!

<img src="img/Search_Fetch_Shift_Menu.png" height=auto width=550px alt="Screenshot: Voice Recorder App Audio List">

## Motivation

Sometimes, when users want to do something very quickly with a file they need to download, they download and use it, but forget to move it to the desired folder they intended to move it to. Eventually, when searching for it, they realize that they can't find it. This gets even more cumbersome when there are many files to move and you have to search for each of them across varying dates in the file explorer.

Inspired by this [video](https://www.youtube.com/watch?v=vGxR98gI930), around 40 seconds in, [Internet Made Coder](https://www.youtube.com/@InternetMadeCoder) talks about making a Python Automation Script, and something he mentions would be a solution to the problem I had mentioned earlier, which is moving files to where I want them to actually reside on disk.   
And even more recently, in trying to create a [mobile app that replicates a Generation 1 PokéDex](https://github.com/AS-Coope/Gen1Dex), I realized I'd have to be moving a lot of images around. And those situations combined gave birth to this project.

Additionally, I stumbled upon this [project](https://github.com/brentvollebregt/auto-py-to-exe) which has inspired me to see this through long-term (at least to get a good looking graphical user interface up alongside, hopefully, quality code).

## Usage:
**IMPORTANT NOTICE**: This is currently being developed and tested on a device operating a Windows OS. As such, it may not work as desired on Linux, Mac or other operating systems.

### Installation
Download and install [Python](https://www.python.org/downloads/) (ensure it is added to [PATH](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/)).


#### Create a virtual environment
- Python projects generally have a virtual environment to isolate its dependencies. This project is no exception. To create a virtual environment run the following command via the command-line/terminal: `python -m venv [name of your virtual environment]`. Conventionally, `venv` is used as the name of the virtual environment, but you can name it whatever you desire.

- Activate the virtual environment by entering the following via the command-line/terminal `.\venv\Scripts\activate` on Windows. For MacOS or Linux: `source venv/bin/activate`.

- [Before doing this step, please ensure that the virtual environment **is** activated] A requirements.txt file is part of the repo. To install the external dependencies, run the following command in the command-line/terminal: `pip install -r requirements.txt` (**NOTE**: This project currently does not rely on external dependencies, so there is no need to follow this step).

- To start the program, run the following command: `python search_fetch_shift.py`.

- To deactivate the virtual environment, run the following command: `deactivate`.

## Deliverables
For v1.0:
- [X] Allow the user to move files of a particular file extension from one directory to another.
- [ ] Allow the user to move files of a particular file extension and name (whether matching full  name or substring) from one directory to another.
- [ ] Allow the user to move files of a particular name (whether matching full name or a substring) from one directory to another.
- [ ] Allow the user to store regularly used directory paths.
- [ ] Allow the user to view stored directory paths.
- [ ] Allow the user to remove stored directory paths.
- [ ] Provide the user with the option to use an Interactive/Menu mode (where the user is provided a menu to go through to complete their action) and a Command/Utility mode (where the user passes the command immediately at the command prompt and the command is executed without further interaction needed from the user unless an error occurs).
- [ ] Determine the user's operating system and operate on directories based on the file system structure.

For v2.0
- [ ] Allow the user to copy files of a particular file extension from one directory to another.
- [ ] Allow the user to copy files of a particular file extension and name (whether matching full name or substring) from one directory to another.
- [ ]  Allow the user to copy files of a particular name (whether matching full name or substring) from one directory to another.
- [ ] Parse a directory's path received to determine whether it is relative or not, and if so, break it down to its absolute path.
- [ ] Provide a help/man-page.