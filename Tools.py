# airodump is used for getting close wifi networks
# aircrack is for cracking the captured file
from colorama import Fore
import pyrcrack


airmon = pyrcrack.AirmonNg()


def DeAuthNetwork(NetWrkInterface, TarNetwork):
    print(Fore.GREEN + f"[!] De-Authing Network\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\nTarget Network SSID ==> {TarNetwork}\n")



def ListenAndCaptureFile(NetWrkInterface):
    print(Fore.GREEN + f"[!] Listening For File to Capture\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\n")




async def FindNetworks(NetWrkInterface):
    print(Fore.GREEN + f"[!] Listening For Nearby Networks\n** 1NF0 **\nNetwork Interface ==> {NetWrkInterface}\n")
    async with airmon(NetWrkInterface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for aps in pdump(mon.monitor_interface):
                print(aps)















