import os, shutil, requests
from bs4 import BeautifulSoup as BS

URL = "https://yandex.ru/images/" # ссылка на страничку html


def save_image(image_url, name, i):
    request_on_download_image = requests.get(f"https:{image_url}")
    saver = open(f"dataset/{name}/{i:04d}.jpg", "wb")
    saver.write(request_on_download_image.content)
    saver.close()

def clear_folder(name):
    shutil.rmtree(name)

def check_folder():
    try:
        os.mkdir("dataset")
    except:
        clear_folder("dataset")
        os.mkdir("dataset")

def get_images_url(name):
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

check_folder()
get_images_url("rose")
get_images_url("tulip")
