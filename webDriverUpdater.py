import winreg
import os
import zipfile
import wget
from colorama import Fore, Back, init, deinit
import math
import keyboard

#Update Functions
def msedge():
    key_path = r"Software\Microsoft\Edge\BLBeacon"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    edgeVersion = winreg.QueryValueEx(key, "version")[0]
    print(f'{Fore.LIGHTWHITE_EX}MSEdge Driver Version {edgeVersion} being downloaded...')

    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://msedgedriver.azureedge.net/{edgeVersion}/edgedriver_win64.zip'
    wget.download(driverPath, out="driver.zip", bar=bar_custom)
    print(Fore.WHITE + "\nExtracting the archive...\n" + Fore.LIGHTYELLOW_EX)
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("msedgedriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')

def chrome():
    key_path = r"Software\Google\Chrome\BLBeacon"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    chromeVersion = winreg.QueryValueEx(key, "version")[0]
    print(f'{Fore.LIGHTWHITE_EX}Chrome Driver Version {chromeVersion} being downloaded...')

    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chromeVersion}/win64/chrome-win64.zip'
    wget.download(driverPath, out="driver.zip", bar=bar_custom)
    print(Fore.WHITE + "\nExtracting the archive...\n" + Fore.LIGHTYELLOW_EX)
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("chromedriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')
def gecko():
    print(f'{Fore.LIGHTWHITE_EX}GeckoDriver Version 0.33.0 being downloaded...')
    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip'
    wget.download(driverPath, out="driver.zip", bar=bar_custom)
    print(Fore.WHITE + "\nExtracting the archive...\n" + Fore.LIGHTYELLOW_EX)
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("geckodriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')

#UI
def hide_cursor():
    print('\033[?25l', end="")

def bar_custom(current, total, width=100): #lifted directly from wget bar_thermometer
    avail_dots = width
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    return  Back.LIGHTGREEN_EX + chr(32)*shaded_dots + Back.GREEN + chr(32)*(avail_dots-shaded_dots) + Back.BLACK + " %" + str(shaded_dots)
##################

#Main Program
init()
hide_cursor()
selectedIndex = 0

menuTexts = [
    f"MS Edge WebDriver",
    f"Chrome Driver",
    f"Gecko Driver"
]
os.system("cls")
while True: #main loop
    print(f"{Fore.LIGHTCYAN_EX}WEBDRIVER AUTO UPDATER")
    print(f"{Fore.LIGHTYELLOW_EX}------------------------")
    print(f"\n{Fore.LIGHTWHITE_EX}Which webdriver do you want to update? (UP and DOWN to choose, ENTER to update, ESC to exit)\n")
    for i in range(len(menuTexts)):
        if i == selectedIndex:
            print(f"{Fore.LIGHTBLUE_EX}>{menuTexts[i]}")
        else:
            print(f"{Fore.LIGHTWHITE_EX}{menuTexts[i]}")
    if keyboard.read_key() == "up":
        if selectedIndex > 0:
            selectedIndex -= 1
        os.system("cls")
    elif keyboard.read_key() == "down":
        if selectedIndex < 2:
            selectedIndex += 1
        os.system("cls")
    elif keyboard.read_key() == "enter":
        os.system("cls")
        match selectedIndex:
            case 0:
                try:
                    msedge()
                    print(Fore.LIGHTGREEN_EX + "\nDone! Enjoy your automated web surfing :)")
                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"\nAn error occurred during the download or extraction process: {e}")
            case 1:
                try:
                    chrome()
                    print(Fore.LIGHTGREEN_EX + "\nDone! Enjoy your automated web surfing :)")
                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"\nAn error occurred during the download or extraction process: {e}")
            case 2:
                try:
                    gecko()
                    print(Fore.LIGHTGREEN_EX + "\nDone! Enjoy your automated web surfing :)")
                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"\nAn error occurred during the download or extraction process: {e}")
        os.system("cls")
    elif keyboard.read_key() == "esc":
        deinit()
        os.system("cls")
        break