import os, shutil, requests
from bs4 import BeautifulSoup as BS

__URL__ = "https://yandex.ru/images/" # ссылка на страничку html

while(True): # цикл проверки на корректный ввод строки
    __INPUT__ = input("Please enter the text requests: ") # ввод запроса в строку поиска
    if(__INPUT__ != ""):
        print("\nNice!\n") # ввод успешный
        break
    else:
        print("\nBad(\n") # ввод неудачный(


i = 1

def save_image(__IMAGE__URL__, name): # функция сохранения картинки
    global i # показываем функции, что i глобальная переменная, а не локальная в самой функции
    __REQUEST__ON__DOWNLOAD__IMAGE__ = requests.get("https:" + __IMAGE__URL__) # получение веб-страницы
    if(i <= 9):
        __SAVER__ = open("dataset/" + name + "/" + "000" + str(i) + ".jpg", "wb") # открытие потока с типом wb
    elif(i >= 10 and i <= 99):
        __SAVER__ = open("dataset/" + name + "/" + "00" + str(i) + ".jpg", "wb") # открытие потока с типом wb
    elif(i >= 100 and i <= 999):
        __SAVER__ = open("dataset/" + name + "/" + "0" + str(i) + ".jpg", "wb") # открытие файлового потока с типом mode = "wb" - открывает файл в бинарном режиме только для записи.
    i += 1
    __SAVER__.write(__REQUEST__ON__DOWNLOAD__IMAGE__.content) # запись в файл
    __SAVER__.close() # закрытие файлового потока

def clear_folder(name):  # функция удаления папки
    shutil.rmtree(name) # рекурсивно удаляет все дерево каталогов


def check_folder():
    try:
        os.mkdir("dataset")
    except:
        clear_folder("dataset")

def get_images_url(): # функция получения картинки
    __REQUEST__GO__ = requests.get(__URL__ + "search?text=" + name, headers={"User-Agent":"Mozilla/5.0"}) # получение веб-страницы, после чего можно получить всю необходимую нам информацию от объекта
    __HTML__ = BS(__REQUEST__GO__.content, "html.parser") # html codes
    __DATA__ = [] # массив который будет хранить все теги <img>
    __FINDER__ = __HTML__.findAll("img") # нахождение всех тегов <img>
    os.mkdir("dataset/" + name)
    for __EVENT__ in __FINDER__: # прогон по FINDER т.е по всем найденным тегам <img>
        __IMAGE__URL__ = __EVENT__.get("src") # получаем ссылку из тега <img id="..." class="..." src="link">
        __DATA__.append([__IMAGE__URL__])  # добавление элемента __IMAGE__URL__ в конец списка __DATA__
        if(__IMAGE__URL__ != ""): # проверка на пустую ссылку
            save_image(__IMAGE__URL__, name) # сохранение картинки
    print("Nice save images)") # картинки успешно сохранены
    print(__DATA__)  # вывод ссылок в консоль для пользователя)
    global i
    i = 1


check_foler() # проверка на сущестующую папку
os.mkdir("dataset")# папка сохранения спарсиных изображений
get_images_url("rose") # вызов функции с "rose"
get_images_url("tulip") # вызов функции с "tulip"
