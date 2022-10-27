import main
from main import Data
import next_element as ne


class Iterator:
    """
        класс итератор - чтобы обойти элементы внутри объекта вашего собственного класса
    """

    def __init__(self, limit: int, obj: object, path: str):
        self.limit = limit
        self.obj = obj
        self.counter = 0
        self.this_path = path

    def __iter__(self) -> None:
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return ne.get_path_of_object_class(self.obj, self.this_path)
        else:
            raise StopIteration


if __name__ == "__main__":
    num = int(input("Please input numbers iteration: "))
    path = input("Please input path: ")  # например dataset/rose/0015.jpg
    it = Iterator(num, Data(main.CLASS_DEFAULT[0], "dataset"), path)
    for val in it:
        print(val)
