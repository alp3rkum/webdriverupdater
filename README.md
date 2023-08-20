# msedgeupdater

MSEdgeUpdater is a small and handy Python script that allows you to auto-update your MS Edge Driver for your projects that involves Selenium WebDriver. This little script is basically downloading the appropriate version of MS Edge Driver according to your browser's version to ensure maximum compatibility, and extracts the .exe file into the "driver" folder right next to it, so you can use your MS Edge Driver right in your application's directory.

## How Does It Work?

msedgeupdater makes use of these important packages:

- winreg
- wget
- zipfile

These packages allow the program to get your current version of MS Edge by looking up to computer's registry records. Then, according to this version, it downloads the appropriate version of MS Edge Driver from its official website (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) into the directory the script is in. As the driver (msedgedriver.exe) comes in an archive, the script proceeds to extract the driver executable to "drivers" folder (with assumption of your Selenium program's possibility of using multiple browser drivers, eg. ChromeDriver or GeckoDriver) and deletes the archive once the file is extracted.

This program should work the way it does as long as Microsoft doesn't heavily alter the layout of MS Edge Driver's website. In other words, you can possibly use msedgeupdater for a lifetime :)

### How To Use?

All you need to do is to double-click or call it via another console/GUI interface. It doesn't take any arguments.

## Requirements

msedgeupdater requires the following to work optimally:

- Internet connection (to download msedgedriver archive)
- Python 3.11 (to ensure compatibility with pip and required packages' versions)
- Windows 10 operating system (because of Windows-specific packages, preferably 64-bit)

Once you satisfy these needs and its necessary packages, msedgeupdater should be a very featherweight but an important aspect of your Selenium-based projects, since ensuring driver's up-to-date status is important for the project in the long term.
