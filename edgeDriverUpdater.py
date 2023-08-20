import subprocess
import winreg
import re

import os
import time

import zipfile
import wget

keyPath = r"Software\Microsoft\Edge\BLBeacon"
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,keyPath, 0, winreg.KEY_READ)
edgeVersion = winreg.QueryValueEx(key,"version")[0]
print(f'MSEdge Driver Version {edgeVersion} being downloaded...')

scriptPath = os.path.dirname(__file__)
driverPath = f'https://msedgedriver.azureedge.net/{edgeVersion}/edgedriver_win64.zip'
wget.download(driverPath)
time.sleep(1)
with zipfile.ZipFile('edgedriver_win64.zip','r') as archive:
    archive.extract("msedgedriver.exe",scriptPath + "\drivers")
os.remove('edgedriver_win64.zip')
print("\nDone! Enjoy your automated web surfing :)")
os.system("pause")