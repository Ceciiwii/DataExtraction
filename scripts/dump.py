# Libraries
from datetime import datetime
from PyQt6.QtCore import pyqtSignal, QThread


class WorkerDump(QThread):
    """Class WorkerDump include de progress bar"""

    update_progress = pyqtSignal(int)
    show_message = pyqtSignal(str)
    task_finished = pyqtSignal(str)
    endOfProcess = pyqtSignal()

    def __init__(self, serial_port, parent=None):
        super().__init__(parent)
        self.serial_port = serial_port
        self.total_data = None
        self.fifty_percent_message_shown = False
        self.hundred_percent_message_shown = False

    def run(self):
        # Collecting is for the write data in .txt
        collecting = False
        # Total_data and collected_data, it is essential for the progress bar to work...
        collected_data = 0
        
        # Send command
        self.serial_port.write(b"1 datalogger_dump\n")
        print("1 datalogger_dump")  # view in text editor
        
        # Gets the date and time... and include in the name of file.txt
        fecha_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        data_extract = f"data_dump_{fecha_datetime}.txt"
        
        with open(data_extract, "w") as file:

            while True:
                line = self.serial_port.readline().decode("utf-8").rstrip()

                # This line indicates data number, for example 4000
                if "dataloger_dump unsended data:" in line:
                    self.total_data = int(line.split(":")[1].strip())
                    file.write(line + "\n")
                    collecting = True
                    # for progress bar
                    self.update_progress.emit(0)

                # Init collecting data
                elif "START" in line:
                    collecting = True
                    print("START")
                    file.write(line + "\n")

                elif collecting:

                    file.write(line + "\n")
                    collected_data += 1
                    progress = int((collected_data / self.total_data) * 100)
                    self.update_progress.emit(progress)

                    # Send additional messages 50% percent ok
                    if progress == 50 and not self.fifty_percent_message_shown:
                        self.show_message.emit("50% of the data received...")
                        self.fifty_percent_message_shown = True

                    if progress == 100 and not self.hundred_percent_message_shown:
                        self.show_message.emit("100% of the data received.")
                        self.hundred_percent_message_shown = True

                        finish_message = (
                            f"Data extraction complete and saved to: {data_extract}"
                        )
                        self.show_message.emit(finish_message)
                        self.show_message.emit("Finally collecting data.")

                        if line == "END":
                            print("END")
                            break
            self.update_progress.emit(100)

