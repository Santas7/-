import annotation
from annotation import Data
import next_element as ne
import os

class IteratorOfExemplar:
    """
        класс итератор - чтобы обойти элементы внутри объекта вашего собственного класса
    """

    def __init__(self, obj: type(Data), pointer: str):
        self.obj = obj
        self.pointer = pointer
        self.counter = 0

    def __next__(self) -> str:
        """
            возвращает следующий элемент
        """
        self.pointer = ne.next_element(self.obj, self.pointer)
        return self.pointer

if __name__ == "__main__":
    iter = IteratorOfExemplar(Data("dataset"),  "dataset\\rose\\0002.jpg")
    print(iter.__next__())
