import os, shutil, requests
from bs4 import BeautifulSoup as BS

url = "https://yandex.ru/images/" # ссылка на страничку html

i = 1

def save_image(image_url, name): # функция сохранения картинки
    global i # показываем функции, что i глобальная переменная, а не локальная в самой функции
    request_on_download_image = requests.get("https:" + image_url) # получение веб-страницы
    if(i <= 9):
        saver = open("dataset/" + name + "/" + "000" + str(i) + ".jpg", "wb") # открытие потока с типом wb
    elif(i >= 10 and i <= 99):
        saver = open("dataset/" + name + "/" + "00" + str(i) + ".jpg", "wb") # открытие потока с типом wb
    elif(i >= 100 and i <= 999):
        saver = open("dataset/" + name + "/" + "0" + str(i) + ".jpg", "wb") # открытие файлового потока с типом mode = "wb" - открывает файл в бинарном режиме только для записи.
    i += 1
    saver.write(request_on_download_image.content) # запись в файл
    saver.close() # закрытие файлового потока

def clear_folder(name):  # функция удаления папки
    shutil.rmtree(name) # рекурсивно удаляет все дерево каталогов


def check_folder():
    try:
        os.mkdir("dataset")
    except:
        clear_folder("dataset")

def get_images_url(name): # функция получения картинки
    request_go = requests.get(url + "search?text=" + name, headers={"User-Agent":"Mozilla/5.0"}) # получение веб-страницы, после чего можно получить всю необходимую нам информацию от объекта
    html = BS(request_go.content, "html.parser") # html codes
    data = [] # массив который будет хранить все теги <img>
    finder = html.findAll("img") # нахождение всех тегов <img>
    os.mkdir("dataset/" + name)
    for event in finder: # прогон по FINDER т.е по всем найденным тегам <img>
        image_url = event.get("src") # получаем ссылку из тега <img id="..." class="..." src="link">
        data.append([image_url])  # добавление элемента __IMAGE__URL__ в конец списка __DATA__
        if(image_url != ""): # проверка на пустую ссылку
            save_image(image_url, name) # сохранение картинки
    print("Nice save images)") # картинки успешно сохранены
    print(data)  # вывод ссылок в консоль для пользователя)
    global i
    i = 1


check_folder() # проверка на сущестующую папку
get_images_url("rose") # вызов функции с "rose"
get_images_url("tulip") # вызов функции с "tulip"
