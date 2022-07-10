# setupper

The script installs or removes packages from an external list provided by the user. It can also do a system update and upgrade.
It should be specifically useful with a fresh Linux install to automate installation of all of the standard apps that require the user to enter "sudo apt-get install <APP_NAME>" for each app separately. 

It should also be useful when using an exported list of apps used from a different distro to be installed on a new distro.
The script works with standard installations i.e.: sudo apt-get <APP_NAME> or sudo pacman -S <APP_NAME>. More complicated installation commands have not been implemented.

The script now is available intwo versions: settuper and settuper2. Latest version has arparsing implemented with some colors in the menu.

# Features:
- The script imports an external file with a list of apps/packages (appList.txt) an installs or removes them.
- All the user needs to do is provide a .txt file listing the packages (appList.txt). The name of the file needs to remain "appList.txt" as for the moment it is hardcoded in the script. 
- The script will automatically detect the package manager required for the distro. At the moment it works with pacman and apt/apt-get.
- In the user options of the script you can choose to update and upgrade the system (recommended before any install).

- User menu options (case insensitive):
  - update the OS (U),
  - install a package (I),
  - remove a package (R),
  - update OS and install a package (UI),
  - update and remove a package (UR).

# Installation:
- git clone https://github.com/betnero/setupper.git
- sudo chmod +x setupper.py
- Prepare the app list file called appList.txt.
- Make sure not to include apps that require more complex installation commands than "sudo apt-get install" or "sudo pacman -S".
- Run the script: python3 ./setupper.py

# TO DO:
- Remove the hardcoded name of the applist.txt file with apps and let the user insert the name.
- Error handling in case of a notification regarding a network failure or package installation/removal failure.
- Overall user prompting to be improved. For the moment the script prompts only about INSTALLING, REMOVING AND PURGING and PERFORMING SYSTEM UPDATE & UPGRADE without verifying the status.
- A summary of successful installs at the end of operation.
- A summary of successful removals at the end of operation.
- Overall code improvement.
