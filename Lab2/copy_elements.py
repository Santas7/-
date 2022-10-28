import os
import shutil
import main
from main import Data
from typing import Type


def make_dir(obj: type(Data)) -> None:
    """
        проверка на сущ-ю директорию + создание новой директории
    """
    try:
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"
    except OSError:
        shutil.rmtree("new_dataset")
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"


def teleportdir(obj: type(Data)) -> None:
    """
        данная функция создает новую папку new_dataset и переносит туда каталог class_name со всеми ее под-каталогами
        так что имена новых под-каталогов начинаются с class_name
    """
    later_dir = obj.dir_name
    make_dir(obj)
    for i in range(1000):
        os.rename(f'{later_dir}/{obj.class_name}/{i + 1:04d}.jpg',
                  f'{later_dir}/{obj.class_name}/{obj.class_name}_{i + 1:04d}.jpg')
        shutil.copy(os.path.expanduser(f'{later_dir}/{obj.class_name}/{obj.class_name}_{(i + 1):04d}.jpg'),
                    obj.dir_name)
        os.rename(f'{later_dir}/{obj.class_name}/{obj.class_name}_{i + 1:04d}.jpg',
                  f'{later_dir}/{obj.class_name}/{i + 1:04d}.jpg')
    obj.create_data_for_csv_file(1)  # type 1


if __name__ == "__main__":
    for element in range(len(main.CLASS_DEFAULT)):
        obj = Data(main.CLASS_DEFAULT[element], "dataset")
        teleportdir(obj)
