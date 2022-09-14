import Tools, os
from colorama import Fore
from sys import platform



# airodump is used for getting close wifi networks
# aircrack is for cracking the captured file
if platform == "linux" or platform == "linux2":
    pass
elif platform == "darwin":
    print(Fore.RED + "[!] You have a invalid operating system! Please use linux instead.")
elif platform == "win32":
    print(Fore.RED + "[!] You have a invalid operating system! Please use linux instead.")
    
os.listdir('/sys/class/net/')
networkInterface = input(Fore.GREEN + "[?] Enter the network interface: ")
