import os
import csv


class Data:
    class_name: str
    dir_name: str  # название директории напр. dataset
    n_data: str  #

    def __init__(self, class_name: str, dir_name: str):
        """
            конструктор с параметром class_name и dir_name ( название папки напр. dataset )
        """
        self.class_name = class_name
        self.dir_name = dir_name
        self.n_data = []

    def set_class_name(self, new_class_name: str) -> None:
        """
            изменение class_name
        """
        self.class_name = new_class_name

    def get_class_name(self) -> str:
        """
            получение значения class_name
        """
        return self.class_name

    def set_dir_name(self, new_dir_name: str) -> None:
        """
            изменение dir_name
        """
        self.dir_name = new_dir_name

    def get_dir_name(self) -> str:
        """
            получение значения dir_name
        """
        return self.dir_name

    # 1 пункт л/р
    def absolute_or_related(self, event, i) -> str:
        """
            данная функция предназначена для получения абсолютного или относительного пути
        """

    def write_in_file_csv(self, data) -> None:
        """
            данная функция нужна для сохранения data ( с получ-ми  путями ) в файл .csv
        """

    def get_data_path(self, data) -> list:
        """
            данная функция нужна для формирования списка data с путями
        """


if __name__ == "__main__":
    pass
