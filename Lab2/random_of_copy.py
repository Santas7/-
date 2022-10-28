import csv
import random
import os
import shutil

import copy_elements as ce
import main
from main import Data


def create_copy_dataset_with_random_number(obj: type(Data)) -> None:
    """
        данная функция копирует файлы класса и переименовывает их рандомно
    """
    later_dir = obj.dir_name
    ce.make_dir(obj)

    for i in range(1000):
        n = random.randint(0, 10000)
        os.rename(f'{later_dir}/{obj.class_name}/{i + 1:04d}.jpg',
                  f'{later_dir}/{obj.class_name}/{n:05d}.jpg')
        shutil.copy(os.path.join(f'{later_dir}/{obj.class_name}/{n:05d}.jpg'), obj.dir_name)
        os.rename(f'{later_dir}/{obj.class_name}/{n:05d}.jpg',
                  f'{later_dir}/{obj.class_name}/{i + 1:04d}.jpg')
        obj.list_numbers.append(n)

    obj.create_data_for_csv_file(2) # type 2


if __name__ == "__main__":
    for element in range(len(main.CLASS_DEFAULT)):
        create_copy_dataset_with_random_number(Data(main.CLASS_DEFAULT[element], "dataset"))
