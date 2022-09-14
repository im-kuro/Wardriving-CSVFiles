
# airodump is used for getting close wifi networks
# aircrack is for cracking the captured file
import subprocess
from colorama import Fore
import pyrcrack, os





def DeAuthNetwork(NetWrkInterface, TarNetwork):
    print(Fore.GREEN + f"[!] De-Authing Network\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\nTarget Network SSID ==> {TarNetwork}\n")



def ListenAndCaptureFile(NetWrkInterface):
    print(Fore.GREEN + f"[!] Listening For File to Capture\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\n")




def FindNetworks(NetWrkInterface):
    print(Fore.GREEN + f"[!] Listening For Nearby Networks\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\n")
    subprocess.check_output(f"xterm -e 'sudo airodump-ng {NetWrkInterface}'")









