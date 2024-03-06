import serial
from PyQt6.QtCore import QThread, pyqtSignal


class InitWake(QThread):
    finished = pyqtSignal(str)  # Emitir con un mensaje cuando finalice

    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port

    def run(self):
        try:
            while True:
                line = self.serial_port.readline().decode("utf-8").rstrip()
                print(line)
                if "Wake?" in line:
                    self.serial_port.write(b"1 ok\n")
                    print("1 ok")
                    print(line)
                    self.finished.emit("Connection with Wake! list.")
                    break
        except Exception as e:
            self.finished.emit(f"Error: {str(e)}")
