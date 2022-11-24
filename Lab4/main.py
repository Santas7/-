import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cv2 import *
import cv2
from PIL import Image


def image_forms(df: pd.DataFrame, all_path: pd.Series) -> pd.DataFrame:
    """
        данная функция для каждого изображения в столбце находит ширину, высоту и каналы.
    """


def change_columns_data_frame(df: pd.DataFrame):
    """
        данная функция предназначена для изменения столбцов dataframe, добавления
        столбцов высоты, ширины, глубины изображения и вычисления статистической информации для столбцов.
        ( 3-5 пункты л/р ) ( исп-л относительные пути потому как что то полетело в аннотации ( 2 лабы ) ( смысл работы впринципе
        одинаков, что для относительного что для абсолютного путей )
        в конце функции создает новый файл .csv уже с изменениями.
    """


def forming_data_frame(filename: str = 'annotation.csv'):
    """
        данная функция с помощью pandas формирует DataFrame, происходит изменение названия колонок ( 1-2 пункты л/р )
        :df: - созданный dataframe
    """


def filter_label_class(df: pd.DataFrame, label_class: str) -> pd.DataFrame:
    """
        данная функция вернет отфильтрованный по метке класса dataframe. ( 6 пункт л/р )
        :df: переданный dataframe
        :label_class: метка класса
    """