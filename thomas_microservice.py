from bs4 import BeautifulSoup
import requests
import time


def check_text_file():
    with open("input.txt", 'r+') as in_file:
        book_name = in_file.readline()
        in_file.close()
    if book_name != '':
        find_amazon_url(book_name)
        with open("input.txt", 'w') as clear_input_file:
            clear_input_file.write('')
            clear_input_file.close()


def find_amazon_url(book_title):
    links = []
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'}

    search_query = book_title.replace(' ', '+')
    base_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&query={0}'.format(search_query)
    default_url = "https://www.goodreads.com"

    page = requests.get(base_url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    for link in soup1.find_all("a", {"class", "bookTitle"}):
        links.append(link.get('href'))

    first_result = default_url + links[0]

    first_result_page = requests.get(first_result, headers=headers)

    soup2 = BeautifulSoup(first_result_page.content, "html.parser")

    li = soup2.find('a', {'class': 'buttonBar'})
    li1 = li.get('data-amazon-url')
    if not li1:
        li1 = li.attrs['href']
        li1 = 'www.goodreads.com' + li1

    file = open("output.txt", "w")
    file.truncate(0)
    file.write(str(li1))
    file.close()


if __name__ == '__main__':
    while True:
        check_text_file()
        time_wait = 5
        print(f'Searching text file in {time_wait} seconds')
        time.sleep(time_wait)