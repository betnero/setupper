#!/bin/env python3

import os
import distro #for distro detection
import platform #for distro detection
import argparse #for mplementation of user flags
from colorama import Fore, Back, Style

#setting up flags: u - update; i - install; r - remove; l - put all installed apps into txt
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', help='Update and upgrade your OS', action='store_true')
parser.add_argument('-i', '--install', help='Install all packages from the list', action='store_true')
parser.add_argument('-r', '--remove', help='Remove all packages from the list', action='store_true')
parser.add_argument('-l', '--list', help='List all installed packages in apps.txt', action='store_true')
args = parser.parse_args()

#identify hosts Linux distribution
d = distro.id()
print("\nYour Linux distribution")
print(Fore.CYAN + d.upper())

#external list of apps as a variable
apps = "appList.txt"

#Definning functions for update
if args.update:
    def U(): #Update function
        print(Fore.CYAN)
        print("\n--------------------------")
        print("SYSTEM UPDATE & UPGRADE...")
        print("--------------------------\n")
        print(Style.RESET_ALL)
        if d == "debian":
            l = "sudo apt-get update -y && sudo apt-get upgrade -y"             
        elif d == "ubuntu":
            l = "sudo apt update -y && sudo apt upgrade -y"
        elif d == "arch":
            l = "sudo pacman -Syu"
        os.system(l)
    U()       

#Definning functions for installing all apps from an external list
if args.install:
    def I(): #Install function
            
        with open(apps) as f:
                    content = f.read().splitlines()
                    for line in content:   
                        print(Fore.CYAN)     
                        print("\n-----------------------------")
                        print("INSTALLING {}...".format(line))
                        print("-----------------------------\n")
                        print(Style.RESET_ALL)
                        if d == "debian":
                            l = "sudo apt-get install appList.txt"               
                        elif d == "ubuntu":
                            l = "sudo apt install -y {}".format(line) 
                        elif d == "arch":
                            l = "sudo pacman -S {} --noconfirm".format(line) 
                        os.system(l)       
    I() 

#Definning functions for removal of all apps listed on an external list
if args.remove:
    #confirm with the user that -r flag is no mistake
    print(Fore.RED)
    print(Back.YELLOW)
    answer = input("Are you sure you want to remove all listed apps? y/n ")
    print(Style.RESET_ALL)
    if answer.lower() not in ["y","yes"]:
        print('Goodbye!')
        exit()
    if answer.lower() in ["y","yes"]:
        #Remove function
        def R():
                with open(apps) as f:
                    content = f.read().splitlines()
                    for line in content: 
                        print(Fore.CYAN) 
                        print(Fore.RED + "\n-----------------------------------")
                        print(Fore.RED + "REMOVING AND PURGING {}...".format(line))
                        print(Fore.RED + "-----------------------------------\n")
                        print(Style.RESET_ALL)
                        if d == "debian":
                                l = "sudo apt-get remove -y {}".format(line)               
                        elif d == "ubuntu":
                                l = "sudo apt remove -y {}".format(line) 
                        elif d == "arch":
                                l = "sudo pacman -Rns {} --noconfirm".format(line) 
                        os.system(l)
    #purging packages
                        if d == "debian":
                                l = "sudo apt-get purge -y {}".format(line)               
                        elif d == "ubuntu":
                                l = "sudo apt purge {}".format(line) 
                        elif d == "arch": #arch has no "purge" feature
                                continue 
                        os.system(l)
        R()

if args.list:
    def L(): #List function
        print(Fore.CYAN)
        print("\n-------------------------------------------------")
        print("LISTING ALL INSTALLED PACKAGES INTO A TXT FILE...")
        print("-------------------------------------------------\n")
        print(Style.RESET_ALL)
        if d == "debian":
                l = "sudo dpkg-query -f '${binry:Package}\n' -W > apps.txt"               
        elif d == "ubuntu":
                l = "sudo dpkg-query -f '${binry:Package}\n' -W > apps.txt" 
        elif d == "arch":
                l = "sudo pacman -Qqe > apps.txt" 
        os.system(l)
    L()
