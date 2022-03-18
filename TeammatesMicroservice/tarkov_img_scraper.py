from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os
from tqdm import tqdm
import time


def find_image(item):
    item = item.replace(' ', '_')

    item_page = requests.get('https://escapefromtarkov.fandom.com/wiki/' + item)
    soup = BeautifulSoup(item_page.content, 'lxml')
    item_box = soup.find('td', class_='va-infobox-mainimage-image')
    item_image = item_box.find('a').attrs.get('href')
    item_image = urljoin(item, item_image)

    # This raises an error if there are any query parameters after '.png'
    try:
        pos = item_image.index("?")
        item_image = item_image[:pos]
    except ValueError:
        pass

    if not os.path.isdir('item_images'):
        os.makedirs('item_images')
    response = requests.get(item_image, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join('item_images', item_image.split('/')[-3])
    progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))
    return filename


def check_text_file():
    with open("item_name.txt", 'r+') as in_file:
        item_name = in_file.read()
        in_file.close()
        if item_name != '':
            with open('item_path.txt', 'w') as out_file:
                out_file.write(find_image(item_name))
                out_file.close()
            with open('item_name.txt', 'w') as clear_file:
                clear_file.write('')
                clear_file.close()


if __name__ == '__main__':
    while True:
        check_text_file()
        time_wait = 3
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)
