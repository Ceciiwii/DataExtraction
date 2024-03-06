# Script
    
* All scripts are executable from any code editor.
* To run them, the oxycontroller must be connected to one of the computer's USB ports
* Remember that for Windows, ONE of the applications from the "drivers" folder must be installed.

## LINUX
### Requeriments:
* Python 3.8 o superior
* PyQt6
* pyserial
* FTDI drivers, incluir carpeta "recursos" (para driver.py)

### Python install
* `apt-get install python3`
* `python3 --version`

#### Libraries
* `pip3 install PyQt6`
* `pip3 install pyserial`

## Running the Scripts

### Downloading drivers
For Ubuntu Linux, it is not necessary to install the driver. However, it is important to still have the files so that the code and application can function without any problems.
* "FTDI_driver_installer.exe" = https://dl.dell.com/FOLDER07738532M/4/FTDI-USB-Serial-Port-Driver_KJ2DR_WIN64_2.14.1.2_A00_02.EXE
* "FTDI_Chip" = https://ftdichip.com/wp-content/uploads/2021/08/CDM212364_Setup.zip (Descomprimir la carpeta)


### File descriptions:
* `auto_extract.py`
The base script for data extraction. Automatically inputs commands and saves them in a .txt file

* `dataextraction.py`
This script can be run from the code editor to view the interface design and extract data from the oxycontroller. This file is the main script.

* `style.py`
Provides various styles for buttons, progress bars, etc.
            
* "`recursos`" is a folder with drivers FTDI

#### To design an interface in designer execute:

You can go to the folder where your virtual environment is located

`pyqt6-tools designer`
* Once the design is ready, save it
* Navigate to the directory where you saved the file:
`pyside6-uic nombre_del_archivo.ui > nombre_del_archivo.py`
With this command, the file will be a .py using the PyQt6 library

