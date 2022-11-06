import annotation
import copy_elements as ce
import random_of_copy as rc
from annotation import Data
from iterator_class import IteratorOfExemplar
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # параметры окна
        self.setWindowTitle("MyApp")
        self.setFixedSize(QSize(800, 600))
        self.dataset_path = QFileDialog.getExistingDirectory(self, 'Путь к папке базового датасет')
        src = QLabel(f'Базовый датасет:\n{self.dataset_path}', self)
        layout = QGridLayout()
        layout.addWidget(src, 0, 0)

        # стартовые значения
        self.count_r = 1  # счетчик позиции
        self.count_t = 1
        self.s_p_rose = f"dataset\\{annotation.CLASS_DEFAULT[0]}\\0001.jpg"  # начальный для rose
        self.s_p_tulip = f"dataset\\{annotation.CLASS_DEFAULT[1]}\\0001.jpg"  # начальный для tulip

        self.show()

    def add_button(self, name: str, size_x: int, size_y: int, pos_x: int, pos_y: int):
        """
            метод добавления ( создания ) кнопки
            :name: - название кнопки
            :size_x: - размер по x
            :size_y: - размер по y
            :pos_x: - позиция по x
            :pos_y: - позиция по y
        """

    def next_rose(self):
        """
            метод перехода к некст картинки ( rose )
        """

    def next_tulip(self):
        """
            метод перехода к некст картинки ( tulip )
        """

    def back_rose(self):
        """
            метод перехода к предыдущей картинки ( rose )
        """

    def back_tulip(self):
        """
            метод перехода к предыдущей картинки ( tulip )
        """

    def create_annotation(self):
        """
            метод создания файла аннотации
        """
        try:
            ann = Data("dataset")
            for i in range(1, 1000):
                ann.add(self.dataset_path, f"{annotation.CLASS_DEFAULT[0]}", f"{i:04d}.jpg")
            for i in range(1, 1000):
                ann.add(self.dataset_path, f"{annotation.CLASS_DEFAULT[1]}", f"{i:04d}.jpg")
        except OSError:
            print("error")

    def copy_of_dataset(self):
        """
            метод создания копии dataset
        """

    def random_of_dataset(self):
        """
            метод создания рандомизации датасет
        """

    def exit(self):
        """
            метод выхода из программы
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
