import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import Request,urlopen
import os
from tqdm import tqdm
import re


def get_page(book_id):
    default_url = "https://www.goodreads.com/book/show/"

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'}

    url = default_url + book_id

    page = Request(url, headers=headers)
    webpage = urlopen(page).read()
    soup = BeautifulSoup(webpage, 'lxml')

    return soup


def download_cover(book_page, book_id):
    """This downloads the .png of the book"""
    # Create a folder to download cover images to
    if not os.path.isdir('cover_photos'):
        os.makedirs('cover_photos')

    # Find the cover image on the page
    link = book_page.find('div', {'class', 'bookCoverPrimary'})
    cover_image = link.find('img').attrs.get('src')
    cover_image = urljoin(book_id, cover_image)

    response = requests.get(cover_image, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join('cover_photos', cover_image.split('/')[-1])
    progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))

    return filename


def get_description(book):
    des = book.findAll(id=re.compile(r'(?<=freeText)\d+'))
    description = des[0].contents
    whole_description = "<p style='font-size: 15px'>"
    for item in description:
        if type(item) is bs4.element.NavigableString:
            whole_description = whole_description + item + "</p><p style='font-size: 15px'>"
        elif type(item) is bs4.element.Tag:
            whole_description = whole_description + item.text + "</p><p style='font-size: 15px'>"
    whole_description = whole_description + "</p>"
    return whole_description


def find_book(book):
    book_page = get_page(book)
    cover_image = download_cover(book_page, book)
    description = get_description(book_page)

    return cover_image, description


if __name__ == '__main__':
    cur_book = '17332218'
    print(find_book(cur_book))
