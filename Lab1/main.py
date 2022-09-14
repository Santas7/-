import os, requests

__URL__ = "https://yandex.ru/images/" # ссылка на страничку html

while(True): # цикл проверки на корректный ввод строки
    __INPUT__ = input("Please enter the text requests: ") # ввод запроса в строку поиска
    if(__INPUT__ != ""):
        print("\nNice!\n") # ввод успешный
        break
    else:
        print("\nBad(\n") # ввод неудачный(
