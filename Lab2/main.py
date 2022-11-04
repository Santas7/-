import os
import csv

CLASS_DEFAULT = ["rose", "tulip"]  # базовые названия


class Data:
    def __init__(self, dir_name: str) -> None:
        """
            :number_lines: - кол-во строк в аннотации
            :viewed_files: - кол-во просмотренных файлов
            :dir_name: - название директории ( "dataset" )
        """
        self.number_lines = 0
        self.viewed_files = 1
        self.dir_name = dir_name

    def add(self, path: str, class_name: str, name_image: str) -> None:
        """
            функция добавляет строку в файл аннотация
            :path: - переменная содержащая путь ( например: "D:\Program Files\programmingLabs\Python\python-L-2-var-4\Lab2" )
            :class_name: - имя класса ( под каталога ) например: CLASS_DEFAULT[0]
            :name_image: - переменная которая содержит название картинки
        """
        with open("annotation.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            if self.number_lines == 0: # если кол-во строк = 0, то это заголовки файла аннотация
                writer.writerow([
                    "абсолютный путь",
                    "относительный путь",
                    "класс"
                ])
                self.number_lines += 1
            writer.writerow([os.path.join(path, self.dir_name, class_name, name_image), os.path.join(self.dir_name, class_name, name_image), class_name])
            self.number_lines += 1