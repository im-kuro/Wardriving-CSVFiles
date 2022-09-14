import Tools, os
from colorama import Fore
from sys import platform

''' 
--INFO
This is mainly a Wardriving script, meaning its meant to be able to be left un attened for up to as long as you need.
This script AUTOMATTICLY finds networks, deAuths them, and gets the CSV file to later brute force for access.

--LATER UPDATES
In future updates we intend to have a loaction pin point of some type to know where you where when you got the file
Along with more loggging to find more info about the area and what kind of network it was.
'''
# airodump is used for getting close wifi networks
# aircrack is for cracking the captured file
if platform == "linux" or platform == "linux2":
    pass
elif platform == "darwin":
    print(Fore.RED + "[!] You have a invalid operating system! Please use linux instead.")
elif platform == "win32":
    print(Fore.RED + "[!] You have a invalid operating system! Please use linux instead.")

def CheckForTools():
    for dir in os.listdir("/usr/sbin"):
        if dir == "airodump-ng":
            print(Fore.RED + "[!] airodump-ng Is Installed...")
        elif dir == "aireplay-ng":
            print(Fore.RED + "[!] aireplay-ng Is Installed...")
        else:
            installToolsYN = input(Fore.RED + "[!] MISSING TOOLS! Would you like to install them now? y/n: ")
            if installToolsYN == "y" or "Y":
                with open("tools.txt", "r") as file:
                    for line in file:
                        os.system(f"sudo apt install {line}")


os.system('ifconfig')
networkInterface = input(Fore.GREEN + "\n[?] Enter the network interface: ")


Networks = Tools.FindNetworks(networkInterface)
print(Networks)



