import os
import csv
import logging
import pandas as pd

class_default = ["rose", "tulip"]  # базовые названия


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
        try:
            if event == 0:
                path = os.path.abspath(f'{self.dir_name}/{self.class_name}/{i:04d}.jpg')
                return path
            if event == 1:
                path = os.path.expanduser(f'{self.dir_name}/{self.class_name}/{i:04d}.jpg')
                return path
            if event == 2:
                path = os.path.abspath(f'{self.dir_name}/{self.class_name}_{i:04d}.jpg')
                return path
            if event == 3:
                path = os.path.expanduser(f'{self.dir_name}/{self.class_name}_{i:04d}.jpg')
                return path
            if event == 4:
                path = os.path.abspath(f'{self.dir_name}/{i:05d}.jpg')
                return path
            if event == 5:
                path = os.path.expanduser(f'{self.dir_name}/{i:05d}.jpg')
                return path
        except OSError:
            logging.warning("Error! I can not get path! 0x(((")

    def write_in_file_csv(self, data) -> None:
        """
            данная функция нужна для сохранения data ( с получ-ми  путями ) в файл .csv
        """
        try:
            with open(f'{self.dir_name}/annotation.csv', 'a', newline='') as file:
                wr = csv.writer(file)
                wr.writerow(["absolute path", "relative path", "name"])

                for i in range(999):
                    wr.writerow([
                        data["absolute path"][i],
                        data["related path"][i],
                        data["name"][i]
                    ])
                file.close()
                pass
        except OSError:
            logging.warning("Error! Write in this file is failed! 0x(((")

    def get_data_path(self, data) -> list:
        """
            данная функция нужна для формирования словаря data с путями
        """
        try:
            for i in range(999):
                data["absolute path"].append(self.absolute_or_related(0, i + 1))
                data["related path"].append(self.absolute_or_related(1, i + 1))
            data["name"] = self.class_name
            return data
        except OSError:
            logging.warning("Error! I can not get the path of data! 0x(((")

    def get_data_path_w(self, data) -> list:
        """
            данная функция нужна для формирования словаря data с путями
        """

    def get_data_path_w2(self, data) -> list:
        """
            данная функция нужна для формирования списка data с путями
        """

    def create_data_for_csv_file(self) -> None:
        """
            данная функция предназначенна для создания словаря data
        """
        try:
            data = {
                "absolute path": [],
                "related path": [],
                "name": ""
            }
            if id == 0:
                data = self.get_data_path(data)
            if id == 1:
                data = self.get_data_path_w(data)
            if id == 2:
                data = self.get_data_path_w2(data)
            else:
                print("error invalid id!")
            df = pd.DataFrame(data)
            print(df)
            self.write_in_file_csv(df)
        except OSError:
            logging.warning("Error forming of csv file! 0x(((")


if __name__ == "__main__":
    for element in range(len(class_default)):
        obj = Data(class_default[element], "dataset")
        obj.create_data_for_csv_file()
