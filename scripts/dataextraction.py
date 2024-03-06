import sys
from PyQt6.QtWidgets import QApplication
from design import Welcome_to_datalogger


if __name__ == "__main__":
    app = QApplication([])
    welcome_window = Welcome_to_datalogger()
    welcome_window.show()
    sys.exit(app.exec())
