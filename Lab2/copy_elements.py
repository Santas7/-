import os
import shutil


def make_dir(obj: object) -> None:
    """
        проверка на сущ-ю директорию + создание новой директории
    """
    try:
        os.mkdir("new_dataset")
        obj.set_dir_name("new_dataset")
    except OSError:
        shutil.rmtree("new_dataset")
        os.mkdir("new_dataset")
        obj.set_dir_name("new_dataset")


def teleportdir(obj: object) -> None:
    """
        данная функция создает новую папку new_dataset и переносит туда каталог class_name со всеми ее под-каталогами
        так что имена новых под-каталогов начинаются с class_name
    """


if __name__ == "__main__":
    pass
