import os, shutil, requests
from bs4 import BeautifulSoup as BS

url = "https://yandex.ru/images/" # ссылка на страничку html



def save_image(image_url, name, i): # функция сохранения картинки
    request_on_download_image = requests.get(f"https:{image_url}") # получение веб-страницы
    saver = open(f"dataset/{name}/{i:04d}.jpg")
    saver.write(request_on_download_image.content) # запись в файл
    saver.close() # закрытие файлового потока

def clear_folder(name):  # функция удаления папки
    shutil.rmtree(name) # рекурсивно удаляет все дерево каталогов


def check_folder():
    try:
        os.mkdir("dataset")
    except:
        clear_folder("dataset")
        os.mkdir("dataset")

def get_images_url(name): # функция получения картинки
    i = 1
    request_go = requests.get(f"{url}search?text={name}", headers={"User-Agent":"Mozilla/5.0"}) # получение веб-страницы, после чего можно получить всю необходимую нам информацию от объекта
    html = BS(request_go.content, "html.parser") # html codes
    data = [] # массив который будет хранить все теги <img>
    finder = html.findAll("img") # нахождение всех тегов <img>
    os.mkdir(f"dataset/{name}")
    for event in finder: # прогон по FINDER т.е по всем найденным тегам <img>
        image_url = event.get("src") # получаем ссылку из тега <img id="..." class="..." src="link">
        data.append([image_url])  # добавление элемента __IMAGE__URL__ в конец списка __DATA__
        if(image_url != ""): # проверка на пустую ссылку
            save_image(image_url, name, i) # сохранение картинки
            i += 1
    print("Nice save images)") # картинки успешно сохранены
    print(data)  # вывод ссылок в консоль для пользователя)


check_folder() # проверка на сущестующую папку
get_images_url("rose") # вызов функции с "rose"
get_images_url("tulip") # вызов функции с "tulip"
