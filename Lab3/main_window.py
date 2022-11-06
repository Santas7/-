import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QGridLayout


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
