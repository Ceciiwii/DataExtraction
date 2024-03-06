import serial.tools.list_ports
import serial
import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QProgressBar,
    QComboBox,
    QMessageBox,
    QMainWindow,
    QListWidget,
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt6.QtGui import QFont
from datetime import datetime
from style import button_style, button_sleep, progressBarStyleFuturistic
from driver import FTDI_install
from dump import WorkerDump
from okwake import InitWake


class Welcome_to_datalogger(QMainWindow):
    """This class is design interface, is the main window for the datalogger application"""

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.serial_port = None
        self.ser = None

    def setupUI(self):
        self.setWindowTitle("Welcome to datalogger")
        self.setGeometry(505, 270, 400, 550)
        self.setStyleSheet("background-color: light grey")

        self.label = QLabel("Welcome to datalogger", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Arial", 18, QFont.Weight.Bold)
        self.label.setFont(font)

        self.Port_Box = QComboBox(self)
        self.Port_Box.setStyleSheet("QComboBox { text-align: center; }")
        self.list_serial_ports()

        self.ok_Button = QPushButton("Ok", self)
        self.ok_Button.setMinimumWidth(100)
        self.ok_Button.setStyleSheet(button_style)

        self.status_Button = QPushButton("Check status", self)
        self.status_Button.setMinimumWidth(100)
        self.status_Button.setStyleSheet(button_style)

        self.text = QListWidget(self)
        self.text.setStyleSheet("QLineEdit { text-align: center; }")
        self.text.setStyleSheet("background-color: beige ")

        self.dump_Button = QPushButton("Data extraction", self)
        self.dump_Button.setMinimumWidth(100)
        self.dump_Button.setStyleSheet(button_style)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet(progressBarStyleFuturistic)

        self.sleep_Button = QPushButton("Sleep", self)
        self.sleep_Button.setMinimumWidth(100)
        self.sleep_Button.setStyleSheet(button_sleep)

        # Layaout define order of buttons, title, etc
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.Port_Box)
        layout.addWidget(self.ok_Button)
        layout.addWidget(self.text)
        layout.addWidget(self.status_Button)
        layout.addWidget(self.dump_Button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.sleep_Button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)  # Center objects
        self.ok_Button.clicked.connect(self.ok_device)
        self.dump_Button.clicked.connect(self.start_data_dump)
        self.status_Button.clicked.connect(self.send_status_command)
        self.sleep_Button.clicked.connect(self.send_sleep_command)

        # Create the menu bar
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu("&File")
        options_menu = self.menu_bar.addMenu("&Options")
        driver_menu = self.menu_bar.addMenu("&Driver")
        help_menu = self.menu_bar.addMenu("&Help")

        # Driver
        driver_action = driver_menu.addAction("Option 1: DELL")
        driver_action.triggered.connect(self.install_driver)
        driver2_action = driver_menu.addAction("Option 2: FTDI CHIP")
        driver2_action.triggered.connect(self.ftdi_chip)
        # Options
        reboot_action = options_menu.addAction("Reboot")
        reboot_action.triggered.connect(self.send_reboot_command)
        # file
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

    """
    Function to automatically find the port
    """

    def list_serial_ports(self):
        self.Port_Box.clear()  # Limpiar los elementos existentes
        ports = serial.tools.list_ports.comports()
        connected_ports = [
            port.device
            for port in ports
            if "USB" in port.hwid or "COM" in port.description
        ]
        self.Port_Box.addItems(
            connected_ports
        )  # Añadir todos los dispositivos conectados al QComboBox

    """
    List serial ports that have a connect device and add to QComboBox
    """

    def find_serial_port(self):
        return next(
            (
                port.device
                for port in serial.tools.list_ports.comports()
                if "USB" in port.device or "COM" in port.device
            ),
            None,
        )

    """
    Function call the class "FTDI_install"
    """

    def install_driver(self):
        installer = FTDI_install(self)
        installer.install_driver()

    """
    Function call the class "FTDI_install"
    """

    def ftdi_chip(self):
        installer = FTDI_install(self)
        installer.install_chip()

    """
    Function init "Wake" 
    """

    def ok_device(self):
        self.text.addItem("Starting Wake...")
        self.text.addItem("Wait a moment...")
        if self.serial_port is not None and self.serial_port.isOpen():
            QMessageBox.warning(self, "Warning", "Connected device.")
            return

        port = self.find_serial_port()

        if port is None:
            QMessageBox.warning(self, "Warning", "No device is connected.")
            return

        self.serial_port = serial.Serial(port, 115200, timeout=1)
        QMessageBox.information(
            self, "Information", f"Connected device in port: {port}. Wake!"
        )
        self.initWakeThread = InitWake(self.serial_port)
        self.initWakeThread.finished.connect(self.onWakeFinished)
        self.initWakeThread.start()

    def onWakeFinished(self, message):
        self.text.addItem(message)

    """
    Function send command "1 sleep"
    """

    def send_sleep_command(self):
        if self.serial_port is None or not self.serial_port.isOpen():
            QMessageBox.warning(self, "Warning", "No device is connected.")
            return

        self.serial_port.write(b"1 sleep\n")
        print("1 sleep")
        response = self.serial_port.readline().decode("utf-8").rstrip()
        print(response)
        self.text.addItem(response)

    """
    Function send command "1 reboot"
    """

    def send_reboot_command(self):
        if self.serial_port is None or not self.serial_port.isOpen():
            QMessageBox.warning(self, "Warning", "No device is connected.")
            return

        self.serial_port.write(b"1 reboot\n")
        print("1 reboot")
        response = self.serial_port.readline().decode("utf-8").rstrip()
        print(response)
        self.text.addItem("Reboot oxycontroller...")
        if "Send: 1 Rebooting..." in response:
            self.text.addItem("Oxycontroller restarted")

    """ 
    Function send command "1 status"
    """

    def send_status_command(self):
        if self.serial_port is None or not self.serial_port.isOpen():
            QMessageBox.warning(self, "Warning", "No device is connected.")
            return

        line = self.serial_port.readline().decode("utf-8").rstrip()
        # Send command "1 status"
        self.serial_port.write(b"1 status\n")
        print("1 status")
        self.text.addItem(line)

        # Name for file. Create and save file with exactly hour and date
        fecha_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        data_status = f"status_{fecha_datetime}.txt"

        # Open file writing
        with open(data_status, "w") as file:
            collecting = True

            # Function for stop collecting
            def stop_collecting():
                nonlocal collecting
                collecting = False

            timeout_timer = QTimer()
            timeout_timer.setSingleShot(True)
            timeout_timer.timeout.connect(stop_collecting)
            timeout_timer.start(5000)  # Wait 5 seconds

            # Read data serial port and save
            while collecting:
                line = self.serial_port.readline().decode("utf-8").rstrip()
                print(f"{line}")
                if line:
                    file.write(line + "\n")
                    self.text.addItem(line)
                else:
                    self.text.addItem(f"Status complete and saved to: {data_status}")
                    break

    """
    Function init progress bar
    """

    def update_progress_bar(self, progress):
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(progress)

    """ 
    Data extraction thread. This function call Class "WorkerDump".
    Create and save file with exactly hour and date
    """

    def start_data_dump(self):
        if self.serial_port is None or not self.serial_port.isOpen():
            QMessageBox.warning(self, "Warning", "No device is connected.")
            return

        # Obtain data

        self.text.addItem("Send command...")
        self.text.addItem("1 datalogger_dump")
        self.text.addItem("Receiving...")
        self.text.addItem("Wait a moment...")

        # Init thread work "WorkerDump
        self.worker_dump = WorkerDump(self.serial_port)
        self.worker_dump.show_message.connect(self.showMessage)
        # self.worker_dump.endOfProcess.connect(self.showMessage)
        self.worker_dump.update_progress.connect(self.update_progress_bar)
        self.worker_dump.start()

    def showMessage(self, message):
        self.text.addItem(message)
