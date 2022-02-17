from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os
from tqdm import tqdm


def find_cover(book):
    """This takes the wikipedia URL of a book and finds the cover image"""
    html_text = requests.get(book)
    soup = BeautifulSoup(html_text.content, 'lxml')
    cover = soup.find('table', class_='infobox vcard')
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
    filename = os.path.join('cover_photos', book.split('/')[-2])
    progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))
    return filename


def get_cover(book):
    """Calls the necessary functions to retrieve and save the cover image. Returns the file path to the cover image"""
    return download_cover(find_cover(book))





if __name__ == '__main__':
    TWOK = 'https://en.wikipedia.org/wiki/The_Wise_Man%27s_Fear'
    book_cover = get_cover(TWOK)
    print(book_cover)
