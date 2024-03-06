
# Creating Windows Executables and Installer in Linux

This document outlines the steps to configure Wine, install Python and Inno Setup on a Linux environment, and then use these tools to create a Windows executable (.exe) and an installer for a Python application.

## Initial Wine Configuration

Before installing any Windows software on Linux, you need to prepare Wine:

`sudo apt update`

`sudo apt install wine`

`sudo apt-get install wine64` 

`wine --version`

# Configure Wine

`winecfg`

### _Press option Windows 10_

## 1. Installation of Windows Python

Download the Python installer from the official Python website:

https://www.python.org/downloads/windows/

Example for version 3.9.10:

https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe

* Create a new directory for python.exe. Open a terminal in the directory where you downloaded the Python installer and execute it with Wine:

`wine python-3.9.10-amd64.exe` or `wine msiexec /i python-3.9.10-amd64.msi`

Follow the installer's prompts, making sure to select the option to add Python to the PATH.

## Create the .exe Executable

Navigate to the directory of your Python script and execute PyInstaller:

`pyinstaller --onefile --windowed --add-data "resources;resources" --icon=icon.ico dataextraction.py`

Note: The icon can be of your choice in .ico format. You can use this file converter: https://convertio.co/es/png-ico/


## Create a program installer...

### Installation of Inno Setup

Download Inno Setup from the official site:

https://jrsoftware.org/isdl.php

Example for version 6.2.1:

https://files.jrsoftware.org/is/6/innosetup-6.2.1.exe

## Install Inno Setup

Run the downloaded installer with Wine:

`wine innosetup-6.2.1.exe` or `WINEPREFIX=~/wine_inno_setup wine innosetup-6.2.1.exe`


Follow the installer instructions to complete the installation of Inno Setup.

You can now use Inno Setup to create an installer for your Windows executable application.
Tutorial: https://www.youtube.com/watch?v=vj15kfON9E4

* Select some options and answer some blocks of information and continue.
* In some Inno will ask where the executable is located. You must go to the `dist` folder (created previously) and select the .exe file inside.