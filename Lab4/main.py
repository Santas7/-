import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image


class DataAnalysis:
    def __init__(self) -> None:
        self.df = None
        self.forming_data_frame()

    def image_forms(self, all_path: pd.Series) -> None:
        """
            данная функция для каждого изображения в столбце находит ширину, высоту и каналы.
            :df: - переданный dataframe
            :all_path: - переданный список путей
        """
        height_image = []
        width_image = []
        channels_image = []
        numerical = []
        label_n = 0  # числовая метка класса
        counter = 0  # счетчик
        for path_of_image in all_path:
            with Image.open(path_of_image) as img:
                width, height = img.size
                height_image.append(height)
                width_image.append(width)
                channels_image.append(3)
                numerical.append(label_n)
            if counter == 998:
                label_n += 1
            counter += 1
        self.df['numerical'] = numerical
        self.df['width'] = width_image
        self.df['height'] = height_image
        self.df['channel'] = channels_image

    def change_columns_data_frame(self) -> pd.DataFrame:
        """
            данная функция предназначена для изменения столбцов dataframe, добавления
            столбцов высоты, ширины, глубины изображения и вычисления статистической информации для столбцов.
            ( 3-5 пункты л/р ) ( исп-л относительные пути потому как что то полетело в аннотации ( 2 лабы ) ( смысл работы впринципе
            одинаков, что для относительного что для абсолютного путей )
        """
        self.image_forms(self.df["related_path"])
        self.saving_in_csv_file("property.csv")

    def forming_data_frame(self, filename: str = 'annotation.csv'):
        """
            данная функция с помощью pandas формирует DataFrame, происходит изменение названия колонок ( 1-2 пункты л/р )
            :df: - созданный dataframe
        """
        self.df = pd.read_csv(filename)
        self.df.drop(['абсолютный путь'], axis=1, inplace=True)
        self.df = self.df.rename(columns={'относительный путь': 'related_path', 'класс': 'name_class'})
        self.change_columns_data_frame()

    def filter_label_class(self, label_class: str) -> pd.DataFrame:
        """
            данная функция вернет отфильтрованный по метке класса dataframe. ( 6 пункт л/р )
            :label_class: метка класса
        """
        return self.df[self.df.name_class == label_class]

    def multifunctional_filter(self, width_max: int, height_max: int,
                               label_class: str) -> pd.DataFrame:
        """
            данная функция вернет отфильтрованный по переданной максимальной высоте и ширине + метке класса dataframe.
            ( 7 пункт л/р )
            :width_max: максимально возможная ширина
            :height_max: максимально возможная высота
            :label_class: метка класса
        """
        return self.df[((self.df.name_class == label_class) & (self.df.width <= width_max) & (self.df.height <= height_max))]

    def grouping(self) -> tuple:
        """
            данная функция делает группировку dataframe, вычисляя min и max + cред.знач по пикселям.
            ( 8 пункт л/р )
            Операция groupby включает в себя некоторую комбинацию разбиения объекта, применения функции и объединения
            результатов. Это можно использовать для группировки больших объемов данных и вычисления операций
            над этими группами.
            min() - получение минимального
            max() - получение максимального
            mean() - сред.знач
        """
        self.df['pixels'] = self.df['height'] * self.df['width'] * self.df['channel']
        return self.df.groupby('name_class').min(), self.df.groupby('name_class').max(), self.df.groupby('name_class').mean()

    def histogram_build(self, label_class: str) -> list:
        """
        данная функция выполняет построение гистограммы. На вход функция принимает dataframe и метку класса,
        на выходе - три массива.
        ( 9 пункт л/р )
        Гистограммы - это собранные подсчеты данных, организованные в набор предопределенных бинов.
        :label_class: метка класса
        """
        img = cv2.imread(np.random.choice(self.filter_label_class(label_class).related_path.to_numpy()))
        height, width, channel = img.shape
        return [cv2.calcHist([img], [0], None, [256], [0, 256]) / (height * width),
                cv2.calcHist([img], [1], None, [256], [0, 256]) / (height * width),
                cv2.calcHist([img], [2], None, [256], [0, 256]) / (height * width)]

    def plots_the_histogram_data(self):
        """
            данная функция строит график по данным гистограммы
            ( 10 пункт л/р )
        """
        colors = ['b', 'g', 'r']
        for i in range(len(colors)):
            plt.plot(self.histogram_build("rose")[i], color=colors[i])
        plt.ylabel('# of Pixels')
        plt.title('Image Histogram GFG')
        plt.xlabel('Pixel values')
        plt.xlim([0, 256])
        plt.show()

    def saving_in_csv_file(self, filename: str):
        self.df.to_csv(filename)

if __name__ == "__main__":
    da = DataAnalysis()
    da.plots_the_histogram_data()