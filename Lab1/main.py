import os, shutil, requests
from bs4 import BeautifulSoup as BS

URL = "https://yandex.ru/images/" # ссылка на страничку html


def save_image(image_url, name, i):
    """сохранение спарсенной картинки в определенную папку"""
    request_on_download_image = requests.get(f"https:{image_url}")
    saver = open(f"dataset/{name}/{i:04d}.jpg", "wb")
    saver.write(request_on_download_image.content)
    saver.close()


def check_folder():
    """проверка на существование папки"""
    try:
        os.mkdir("dataset")
    except:
        shutil.rmtree("dataset")
        os.mkdir("dataset")

def get_images_url(name):
    """
    VARIABLES: создаем необходимые переменные для работы
    FOR: Цикл for нужен для пробежки по finder ( по спарсеному html-коду ).
    IMAGE_URL: Далее в переменную image_url записываем ссылку которая содержится в теге img, в параметре src="...".
    DATA: Затем в массив data с помощью метода append добавляем в конец значение переменной image_url.
    После проверяем через условный оператор if строку на пустоту.... если не пустая, то сохраняем картинку в
    соответствующую папку dataset/name/....jpg/. После цикла выводим сообщение в консоль для пользователя.
    На этом работа функции закончена.
    """
    i = 1
    page = 0
    request_go = requests.get(f"{URL}search?p={page}&text={name}&lr=51&rpt=image", headers={"User-Agent":"Mozilla/5.0"})
    html = BS(request_go.content, "html.parser")
    data = []
    finder = html.findAll("img")
    os.mkdir(f"dataset/{name}")
    while (True):
        for event in finder:
            image_url = event.get("src")
            data.append([image_url])
            if (i > 999):
                page = 0
                break
            if (image_url != ""):
                save_image(image_url, name, i)
                i += 1
        if (i > 999): break
        page += 1
    print("Nice save images)")
    print(data)





if __name__ == "__main__":
    check_folder()
    get_images_url("rose")
    get_images_url("tulip")

help(get_images_url.__doc__)
help(save_image.__doc__)
help(check_folder.__doc__)