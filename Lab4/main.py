import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cv2 import *
import cv2
from PIL import Image


def image_forms(df: pd.DataFrame, all_path: pd.Series) -> pd.DataFrame:
    """
        данная функция для каждого изображения в столбце находит ширину, высоту и каналы.
        :df: - переданный dataframe
        :all_path: - переданный список путей
    """
    height_image = []
    width_image = []
    channels_image = []
    numerical = []
    label_n = 0 # числовая метка класса
    counter = 0 # счетчик
    for path_of_image in all_path:
        image = cv2.imread(path_of_image)
        with Image.open(path_of_image) as img:
            width, height = img.size
            height_image.append(height)
            width_image.append(width)
            channels_image.append(3)
            numerical.append(label_n)
        if counter == 998:
            label_n += 1
        counter += 1
    df['numerical'] = numerical
    df['width'] = width_image
    df['height'] = height_image
    df['channel'] = channels_image
    return df


def change_columns_data_frame(df: pd.DataFrame):
    """
        данная функция предназначена для изменения столбцов dataframe, добавления
        столбцов высоты, ширины, глубины изображения и вычисления статистической информации для столбцов.
        ( 3-5 пункты л/р ) ( исп-л относительные пути потому как что то полетело в аннотации ( 2 лабы ) ( смысл работы впринципе
        одинаков, что для относительного что для абсолютного путей )
        в конце функции создает новый файл .csv уже с изменениями.
    """
    df = image_forms(df, df["related_path"])
    df.to_csv('property.csv')


def forming_data_frame(filename: str = 'annotation.csv'):
    """
        данная функция с помощью pandas формирует DataFrame, происходит изменение названия колонок ( 1-2 пункты л/р )
        :df: - созданный dataframe
    """
    df = pd.read_csv(filename)
    df.drop(['абсолютный путь'], axis=1, inplace=True)
    df = df.rename(columns={'относительный путь': 'related_path', 'класс': 'name_class'})
    change_columns_data_frame(df)
    return df


def filter_label_class(df: pd.DataFrame, label_class: str) -> pd.DataFrame:
    """
        данная функция вернет отфильтрованный по метке класса dataframe. ( 6 пункт л/р )
        :df: переданный dataframe
        :label_class: метка класса
    """
    return df[df.name_class == label_class]


def multifunctional_filter(df: pd.DataFrame, width_max: int, height_max: int, label_class: str) -> pd.DataFrame:
    """
        данная функция вернет отфильтрованный по переданной максимальной высоте и ширине + метке класса dataframe.
        ( 7 пункт л/р )
        :df: переданный dataframe
        :width_max: максимально возможная ширина
        :height_max: максимально возможная высота
        :label_class: метка класса
    """
    return df[((df.name_class == label_class) & (df.width <= width_max) & (df.height <= height_max))]


def grouping(df: pd.DataFrame) -> tuple:
    """
        данная функция делает группировку dataframe, вычисляя min и max + cред.знач по пикселям.
        ( 8 пункт л/р )
        Операция groupby включает в себя некоторую комбинацию разбиения объекта, применения функции и объединения
        результатов. Это можно использовать для группировки больших объемов данных и вычисления операций
        над этими группами.
        min() - получение минимального
        max() - получение максимального
        mean() - сред.знач
        :df: переданный dataframe.
    """
    df['pixels'] = df['height'] * df['width'] * df['channel']
    return df.groupby('name_class').min(), df.groupby('name_class').max(), df.groupby('name_class').mean()


def histogram_build(df: pd.DataFrame, label_class: str) -> list:
    """
    данная функция выполняет построение гистограммы. На вход функция принимает dataframe и метку класса,
    на выходе - три массива.
    ( 9 пункт л/р )
    Гистограммы - это собранные подсчеты данных, организованные в набор предопределенных бинов.
    :df: переданный dataframe.
    :label_class: метка класса
    """
    img = cv2.imread(np.random.choice(filter_label_class(df, label_class).related_path.to_numpy()))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return [cv2.calcHist([cv2.cvtColor(img, cv2.COLOR_BGR2RGB)], [0], None, [256], [0, 256]),
            cv2.calcHist([cv2.cvtColor(img, cv2.COLOR_BGR2RGB)], [1], None, [256], [0, 256]),
            cv2.calcHist([cv2.cvtColor(img, cv2.COLOR_BGR2RGB)], [2], None, [256], [0, 256])]


def timeline(df: pd.DataFrame):
    """
        данная функция строит график по данным гистограммы
        ( 10 пункт л/р )
    """
    colors = ['r', 'g', 'b']
    for i in range(len(colors)):
        plt.plot(histogram_build(df, "rose")[i], color=colors[i])
    plt.ylabel('Intensity')
    plt.title('Color scheme')
    plt.xlabel('Color pixel')
    plt.xlim([0, 256])
    plt.show()

if __name__ == "__main__":
    df = forming_data_frame()
    # timeline(df)