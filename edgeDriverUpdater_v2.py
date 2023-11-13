import winreg
import os
import zipfile
import wget
from colorama import Fore, Back, init
import math

def hide_cursor():
    print('\033[?25l', end="")

def bar_custom(current, total, width=100): #lifted directly from wget bar_thermometer
    avail_dots = width
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    return  Back.LIGHTGREEN_EX + chr(32)*shaded_dots + Back.GREEN + chr(32)*(avail_dots-shaded_dots) + Back.BLACK + "%" + str(shaded_dots)

init()
hide_cursor()
print(Fore.BLUE + "MS EDGE DRIVER UPDATER V2\n")
print(Fore.WHITE)
key_path = r"Software\Microsoft\Edge\BLBeacon"
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
edgeVersion = winreg.QueryValueEx(key, "version")[0]
print(f'MSEdge Driver Version {edgeVersion} being downloaded...')

scriptPath = os.path.dirname(__file__)
driverPath = f'https://msedgedriver.azureedge.net/{edgeVersion}/edgedriver_win64.zip'

try:
    wget.download(driverPath, out="driver.zip", bar=bar_custom)
    print(Fore.WHITE + "\nExtracting the archive...\n" + Fore.LIGHTYELLOW_EX)
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("msedgedriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')
    print(Fore.LIGHTGREEN_EX + "\nDone! Enjoy your automated web surfing :)")
except Exception as e:
    print(Fore.LIGHTRED_EX + f"\nAn error occurred during the download or extraction process: {e}")
finally:
    input("Press any key to continue...")