import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QGridLayout


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
