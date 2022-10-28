import os
import csv
import logging
import pandas as pd

CLASS_DEFAULT = ["rose", "tulip"]  # базовые названия


class Data:
    def __init__(self, class_name: str, dir_name: str):
        """
            конструктор с параметром class_name и dir_name ( название папки напр. dataset )
        """
        self.class_name = class_name
        self.dir_name = dir_name
        self.list_numbers = []

    # 1 пункт л/р
    def absolute_or_related(self, enum: int, i: int) -> str:
        """
            данная функция предназначена для получения абсолютного или относительного пути
        """
        try:
            path = ""
            if enum == 0:
                path = os.path.abspath(f'{self.dir_name}/{self.class_name}/{i:04d}.jpg')
            elif enum == 1:
                path = os.path.expanduser(f'{self.dir_name}/{self.class_name}/{i:04d}.jpg')
            elif enum == 2:
                path = os.path.abspath(f'{self.dir_name}/{self.class_name}_{i:04d}.jpg')
            elif enum == 3:
                path = os.path.expanduser(f'{self.dir_name}/{self.class_name}_{i:04d}.jpg')
            elif enum == 4:
                path = os.path.abspath(f'{self.dir_name}/{i:05d}.jpg')
            elif enum == 5:
                path = os.path.expanduser(f'{self.dir_name}/{i:05d}.jpg')
            return path
        except OSError:
            logging.warning("I'm sorry, but I couldn't find the path(")

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
        except OSError:
            logging.warning("error when writing the annotation file")

    def get_data_path(self, data, enum) -> list:
        """
            данная функция нужна для формирования словаря data с путями
        """
        try:
            if enum == 0:
                for i in range(1000):
                    data["absolute path"].append(self.absolute_or_related(0, i + 1))
                    data["related path"].append(self.absolute_or_related(1, i + 1))
            elif enum == 1:
                for i in range(1000):
                    data["absolute path"].append(self.absolute_or_related(2, i + 1))
                    data["related path"].append(self.absolute_or_related(3, i + 1))
            elif enum == 2:
                for i in range(len(self.list_numbers)):
                    data["absolute path"].append(self.absolute_or_related(4, self.list_numbers[i]))
                    data["related path"].append(self.absolute_or_related(5, self.list_numbers[i]))
            data["name"] = self.dir_name
            return data
        except OSError:
            logging.warning("error when generating a data dictionary with paths")

    def create_data_for_csv_file(self, enum) -> None:
        """
            данная функция предназначенна для создания словаря data
        """
        try:
            data = {
                "absolute path": [],
                "related path": [],
                "name": ""
            }
            if enum == 0:
                data = self.get_data_path(data, 0)
            elif enum == 1:
                data = self.get_data_path(data, 1)
            elif enum == 2:
                data = self.get_data_path(data, 2)
            else:
                print("error invalid id!")
            df = pd.DataFrame(data)
            print(df)
            self.write_in_file_csv(df)
        except OSError:
            logging.warning("error when creating a data dictionary")


if __name__ == "__main__":
    for element in range(len(CLASS_DEFAULT)):
        obj = Data(CLASS_DEFAULT[element], "dataset")
        obj.create_data_for_csv_file(0)
