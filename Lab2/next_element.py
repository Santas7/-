import csv
import main
from main import Data


def get_path_of_object_class(obj: type(Data), pointer: str) -> str:
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
            tmp.append(row[1])
        for i in range(len(tmp)):
            if i != 0:
                for l in range(len(tmp[i])): # пробежка по-символьно
                    if tmp[i][l] == ",":  # запятая
                        count = l
                        while count + 1 < len(tmp[i]):
                            count += 1
                            if tmp[i][count] == ",": # если встретили запятую то выхожим из цикла
                                break
                            else:
                                text += tmp[i][count]
                        res.append(text)
                        text = ""
                        count = 0
        for path in range(len(res)): # пробежка по результируещему списку
            if res[path] == pointer: # если данный маркер (pointer) совпадает с res[path] выводим нект элемент
                return "the next-->" + str(res[path + 2])

if __name__ == "__main__":
    obj = Data("rose", "dataset")
    s1 = get_path_of_object_class(obj, "dataset/rose/0015.jpg")  # dataset/rose/0016.jpg
    print(s1)

    obj = Data("tulip", "dataset")
    s2 = get_path_of_object_class(obj, "dataset/tulip/0443.jpg")  # dataset/tulip/0444.jpg
    print(s2)

