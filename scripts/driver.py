import os
import subprocess
import importlib.resources
from PyQt6.QtWidgets import QMessageBox

''' Class driver install"'''


class FTDI_install:
    def __init__(self, parent=None):
        self.parent = parent

    def install_driver(self):
        # Import driver, from "recuros" file.
        driver_content = importlib.resources.read_binary(
            "recursos", "FTDI_driver_installer.exe"
        )
        driver_path = os.path.join(os.getcwd(), "FTDI_driver_installer.exe")
        with open(driver_path, "wb") as f:
            f.write(driver_content)

        # Init silence installer with the parameter: /S.
        subprocess.run([driver_path, "/S"], shell=True)

        # Remove file temporaly of drive
        os.remove(driver_path)

        QMessageBox.information(
            self.parent,
            "Instalación completada",
            "El controlador FTDI se ha instalado correctamente.",
        )

    def install_chip(self):
        # Import driver, from "recuros" file.
        driver_content = importlib.resources.read_binary("recursos", "FTDI_Chip.exe")
        driver_path = os.path.join(os.getcwd(), "FTDI_Chip.exe")
        with open(driver_path, "wb") as f:
            f.write(driver_content)

        # Init silence installer with the parameter: /S.
        subprocess.run([driver_path, "/S"], shell=True)

        # Elimina el archivo temporal del controlador
        os.remove(driver_path)

        QMessageBox.information(
            self.parent,
            "Instalación completada",
            "El controlador FTDI se ha instalado correctamente.",
        )
