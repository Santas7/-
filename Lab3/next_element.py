import csv
from annotation import Data


def back_element(obj: type(Data), pointer: str) -> str:
    """
        данная функция получает объект и пойнт(точку или метку) и возращает предыдущий элемент
    """
    with open('annotation.csv', 'r', newline='') as file:
        wr = csv.reader(file, delimiter=' ', quotechar='|')
        i = 0  # счетчик
        saver = 0
        num_list = []
        num = ''
        for char in pointer:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
        if num != '':
            num_list.append(int(num))
        for row in wr:
            if i != 0:
                exist = pointer in row[1]
                if exist:
                    res = row[1].split(",")[1].replace("\\", "/")
                    return res.replace(str(num_list[0]), str(num_list[0]-1))
            i += 1
    return None

def next_element(obj: type(Data), pointer: str) -> str:
    """
        данная функция получает объект и пойнт(точку или метку) и возращает следующий элемент
    """
    with open('annotation.csv', 'r', newline='') as file:
        wr = csv.reader(file, delimiter=' ', quotechar='|')
        i = 0  # счетчик
        status = False
        for row in wr:
            if i != 0:
                exist = pointer in row[1]
                if status:
                    return row[1].split(",")[1].replace("\\", "/")
                if exist:
                    status = True
            i += 1
    return None

if __name__ == "__main__":
    obj = Data("dataset")
    next = next_element(obj, "dataset\\rose\\0304.jpg")
    back = back_element(obj, "dataset\\rose\\0304.jpg") # dataset\rose\0752.jpg
    print(next, back)
