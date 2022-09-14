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


__REQUEST__GO__ = requests.get(__URL__ + "search?text=" + __INPUT__) # получение веб-страницы, после чего можно получить всю необходимую нам информацию от объекта
__HTML__ = BS(__REQUEST__GO__.content, "html.parser") # html codes
__DATA__ = [] # массив который будет хранить все теги <img>
__FINDER__ = __HTML__.findAll("img") # нахождение всех тегов <img>


def clear_folder(name):  # функция удаления папки
    shutil.rmtree(name)

def get_images_url(): # функция получения картинки
    try: # обработка исключений ( ошибок )
        os.mkdir("images") # папка сохранения спарсиных изображений
    except:
        clear_folder("images") # удаление папки
    for __EVENT__ in __FINDER__: # прогон по FINDER т.е по всем найденным тегам <img>
        __IMAGE__URL__ = __EVENT__.get("src") # получаем ссылку из тега <img id="..." class="..." src="link">
        if(__IMAGE__URL__ != ""): # проверка на пустую ссылку
            save_image(__IMAGE__URL__) # сохранение картинки
    print("Nice save images)") # картинки успешно сохранены
