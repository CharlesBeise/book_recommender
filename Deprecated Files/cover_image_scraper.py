from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os
from tqdm import tqdm
import wikipedia
import time


def find_cover(book):
    """This takes the wikipedia URL of a book and finds the cover image"""
    html_text = requests.get(book)
    soup = BeautifulSoup(html_text.content, 'lxml')
    # 'infobox vcard' is the class name of the display box on wikipedia pages, so this ensures it pulls the image from
    # this box, instead of a random image located elsewhere on the page
    cover = soup.find('table', class_='infobox vcard')
    if not cover:
        cover = soup.find('table', class_='infobox')
    cover_image = cover.find('img').attrs.get('src')
    cover_image = urljoin(book, cover_image)

    # This raises an error if there are any query parameters after '.png'
    try:
        pos = cover_image.index("?")
        cover_image = cover_image[:pos]
    except ValueError:
        pass

    return cover_image


def download_cover(book):
    """This downloads the .png of the book"""
    # Create a folder to download cover images to
    if not os.path.isdir('cover_photos'):
        os.makedirs('cover_photos')
    response = requests.get(book, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join('cover_photos', book.split('/')[-1])
    progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))
    return filename


def get_cover(book):
    """Calls the necessary functions to retrieve and save the cover image. Returns the file path to the cover image"""
    try:
        page = wikipedia.page(book + ' book')
    except wikipedia.exceptions.PageError:
        page = wikipedia.page(book + ' novel')
    print(page.url)
    return download_cover(find_cover(page.url))


def check_text_file():
    with open("book_title.txt", 'r+') as in_file:
        title = in_file.read()
        in_file.close()
        if title != '':
            with open('cover_image_path.txt', 'w') as out_file:
                out_file.write(get_cover(title))
                out_file.close()
            with open('book_title.txt', 'w') as clear_file:
                clear_file.write('')
                clear_file.close()



if __name__ == '__main__':
    while True:
        check_text_file()
        time_wait = 3
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)
