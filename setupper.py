#!/bin/env python3

import os
import platform #for distro detection

def force_sudo(): # Enforce sudo on the user
    if not 'SUDO_UID' in os.environ.keys():
        print("Please use sudo.")
        exit()

force_sudo()

d = platform.node() #a variable that contains info 
print("Your on:", d)

apps = "a.txt" #a list of packages to be installed or removed

x = input('''Enter your option: update OS (U), install (I), remove (R), update and install (UI), update and remove (UR): ''')

#Definning functions for update, install and removal
def U(): #Update function
    print("--------------------")
    print("PERFORMING SYSTEM UPDATE & UPGRADE...")
    print("--------------------")
    if d == "debian":
        l = "sudo apt-get update -y && sudo apt-get upgrade -y"             
    elif d == "ubuntu":
        l = "sudo apt update -y && sudo apt upgrade -y"
    elif d == "arch":
        l = "sudo pacman -Syyu -y" 
    os.system(l)         
    print("--------------------")
    print("SYSTEM UP TO DATE...")
    print("--------------------")

def I(): #Install function
        
    with open(apps) as f:
                content = f.read().splitlines()
                for line in content:        
                    print(" ")
                    print("--------------------")
                    print("INSTALLING {}...".format(line))
                    print("--------------------")
                    print(" ")
                    if d == "debian":
                        l = "sudo apt-get install -y {}".format(line)               
                    elif d == "ubuntu":
                        l = "sudo apt install -y {}".format(line) 
                    elif d == "arch":
                        l = "sudo pacman -S -y {}".format(line) 
                    os.system(l)        

def R(): #Remove function
        with open(apps) as f:
            content = f.read().splitlines()
            for line in content: 
                print(" ")
                print("--------------------")
                print("REMOVING AND PURGING {}...".format(line))
                print("--------------------")
                print(" ")
                if d == "debian":
                        l = "sudo apt-get remove -y {}".format(line)               
                elif d == "ubuntu":
                        l = "sudo apt remove -y {}".format(line) 
                elif d == "arch":
                        l = "sudo pacman -Rns -y {}".format(line) 
                os.system(l)

                if d == "debian":
                        l = "sudo apt-get purge -y {}".format(line)               
                elif d == "ubuntu":
                        l = "sudo apt purge -y {}".format(line) 
                elif d == "arch":
                        continue 
                os.system(l)

#calling functions for each of the possibilities: ur, ui, i, r
if x == "U" or x == "u":
    U()

elif x == "I" or x == "i":
    I()
   
elif x == "R" or x == "r":
    R()

elif x == "UR" or x == "RU" or x == "ru" or x == "ur":
    U()
    R()

elif x == "UI" or x == "IU" or x == "iu" or x == "ui":
    U()
    I()


#Print a summary of apps that have been installed or removed but only in cases other than U
if x == "U":
    pass
else:
    print("Your list of apps " + x)
    f = open('a.txt', 'r')
    file_contents = f.read()
    print(file_contents)
