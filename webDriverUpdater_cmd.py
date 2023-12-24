import winreg
import os
import zipfile
import wget
import sys

whichDriver = None

def msedge():
    key_path = r"Software\Microsoft\Edge\BLBeacon"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    edgeVersion = winreg.QueryValueEx(key, "version")[0]
    print(f'MSEdge Driver Version {edgeVersion} being downloaded...')

    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://msedgedriver.azureedge.net/{edgeVersion}/edgedriver_win64.zip'
    wget.download(driverPath, out="driver.zip")
    print("\nExtracting the archive...\n")
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("msedgedriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')

def chrome():
    key_path = r"Software\Google\Chrome\BLBeacon"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    chromeVersion = winreg.QueryValueEx(key, "version")[0]
    print(f'Chrome Driver Version {chromeVersion} being downloaded...')

    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chromeVersion}/win64/chrome-win64.zip'
    wget.download(driverPath, out="driver.zip")
    print("\nExtracting the archive...\n")
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("chromedriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')
def gecko():
    print(f'{Fore.LIGHTWHITE_EX}GeckoDriver Version 0.33.0 being downloaded...')
    scriptPath = os.path.dirname(__file__)
    driverPath = f'https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip'
    wget.download(driverPath, out="driver.zip")
    print("\nExtracting the archive...\n")
    with zipfile.ZipFile('driver.zip', 'r') as archive:
        archive.extract("geckodriver.exe", scriptPath + "\drivers")
    os.remove('driver.zip')

def help():
    print("Usage: python3 webDriverUpdater.py [driver]")
    print("Drivers: --edge, --chrome, (--firefox or --gecko)")

if(len(sys.argv) == 2):
    whichDriver = sys.argv[1]
    match(whichDriver):
        case "--edge":
            msedge()
        case "--chrome":
            chrome()
        case "--firefox" | "--gecho":
            gecko()
        case "--help":
            help()
        case _:
            help()