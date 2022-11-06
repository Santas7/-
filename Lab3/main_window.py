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

        # кнопки
        self.btn_create_of_annotation = self.add_button("Создать аннотацию", 150, 50, 630, 50)
        self.btn_copy_of_dataset = self.add_button("Копирование датасет", 150, 50, 630, 100)
        self.btn_random_of_dataset = self.add_button("Рандомайз датасет", 150, 50, 630, 150)
        self.btn_next_rose = self.add_button("Следующая роза-->", 150, 50, 630, 250)
        self.btn_back_rose = self.add_button("<--Предыдущая роза", 150, 50, 630, 300)
        self.btn_next_tulip = self.add_button("Следующий тюльпан-->", 150, 50, 630, 350)
        self.btn_back_tulip = self.add_button("<--Предыдущий тюльпан", 150, 50, 630, 400)
        self.go_to_exit = self.add_button("Выйти из программы", 150, 50, 630, 500)

        # картинка
        self.pic = QtWidgets.QLabel(self)
        self.pic.setPixmap(QtGui.QPixmap(self.s_p_rose))
        self.pic.resize(600, 500)  # <--
        self.pic.move(10, 50)

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
        button = QPushButton(name, self)
        button.setFixedSize(QSize(size_x, size_y))
        button.move(pos_x, pos_y)
        return button

    def next_rose(self):
        """
            метод перехода к некст картинки ( rose )
        """
        try:
            if self.count_r >= 1000 or self.count_r < 1:
                self.s_p_rose = f"dataset\\{annotation.CLASS_DEFAULT[0]}\\0001.jpg"
            else:
                next = IteratorOfExemplar(Data("dataset"), self.s_p_rose).__next__()
                next.replace("", '"')
                self.s_p_rose = next.replace("/", "\\")
                self.count_r += 1
            self.pic.setPixmap(QtGui.QPixmap(self.s_p_rose.replace('"', "")))
        except OSError:
            print("error")

    def next_tulip(self):
        """
            метод перехода к некст картинки ( tulip )
        """
        try:
            if self.count_t >= 1000 or self.count_t < 1:
                self.s_p_tulip = f"dataset\\{annotation.CLASS_DEFAULT[1]}\\0001.jpg"
            else:
                next = IteratorOfExemplar(Data("dataset"), self.s_p_tulip).__next__()
                next.replace("", '"')
                self.s_p_tulip = next.replace("/", "\\")
                self.count_t += 1
            self.pic.setPixmap(QtGui.QPixmap(self.s_p_tulip.replace('"', "")))
        except OSError:
            print("error")

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
        try:
            ce.teleport_dir(Data("dataset"), self.dataset_path, annotation.CLASS_DEFAULT[0])
        except OSError:
            print("error")

    def random_of_dataset(self):
        """
            метод создания рандомизации датасет
        """
        try:
            rc.create_copy_dataset_with_random_number(Data("dataset"), self.dataset_path, annotation.CLASS_DEFAULT[0])
        except OSError:
            print("error")

    def exit(self):
        """
            метод выхода из программы
        """
        print("пока... надеюсь скоро увидимся!)")
        self.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
