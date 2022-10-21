import csv
import main
from main import Data


def get_path_of_object_class(obj: object, pointer: str) -> str:
    """
        данная функция получает объект и пойнт(точку или метку) и возращает следующий элемент
    """
    with open(f'{obj.dir_name}/annotation.csv', 'r', newline='') as file:
        wr = csv.reader(file, delimiter=' ', quotechar='|')
        count = 0 # счетчик
        res = [] # результирующий список
        tmp = []
        text = "" # временная строка
        for row in wr:
            # tmp.append(row)
            pass
        for i in range(len(tmp)):
            if i != 0:
                # res.append( .. )
                pass
        for path in range(len(res)):
            if res[path] == pointer:
                pass

if __name__ == "__main__":
    pass
