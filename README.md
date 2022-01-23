# setupper

The script installs or removes packages from an external list provided by the user. It can also do an update and upgrade.
It should be specifically useful with a fresh Linux install to automate installation of all of the standard apps that require the user to enter "sudo apt-get install <APP_NAME>" for each app separately. It should also be useful when using an exported list of apps used from a different distro to be installed on a new distro.
The script works with standard installations i.e.: sudo apt-get <APP_NAME> or sudo pacman-S <APP_NAME>. More complicated install commands have not been implemented.

# Features:
- The script imports an external file with a list of apps/packages (a.txt) an installs or removes them.
- All the user needs to do is provide a file listing the packages (a.txt). The name of the file needs to remain "a.txt" as for the moment it is hardcoded in the script. 
- The script will automatically detect the package manager required for the distro. At the moment it works with pacman and apt/apt-get.
- You can choose in the user options of the script to update and upgrade the system (recommended before any install).

- User menu options (case insensitive):
  - update OS (U),
  - install (I),
  - remove (R),
  - update and install (UI),
  - update and remove (UR).

#Installation:
- git clone https://github.com/betnero/setupper.git
- sudo chmod +x setupper.py
- Prepare the app list a.txt.
- Make sure not to include apps that require more complex installation commands than "sudo apt-get install" or "sudo pacman -S".
- python3 ./setupper.py

#TO DO:
- Remove the hardcoded name of the file with apps and let the user insert the name.
- Error handling in case of a notification regarding a network failure or package installation/removal failure.
- Overall user prompting to be improved. For the moment the script prompts only about INSTALLING, REMOVING AND PURGING and PERFORMING SYSTEM UPDATE & UPGRADE without verifying the status.
- A summary of successful installs at the end of operation.
- A summary of successful removals at the end of operation.
- Overall code improvement.
