from bs4 import BeautifulSoup
import requests
import pandas as pd
import timeit
from sms_service import send_msg

pd.options.mode.chained_assignment = None

start = timeit.default_timer()


def find_genre(name, title):
    default_url = "https://www.goodreads.com/book/show/"
    search_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&query={0}'
    base_url = 'https://www.goodreads.com'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'}

    url = default_url + name

    page = requests.get(url, headers=headers)

    if page.status_code != 200:
        search_query = title.replace(' ', '+')
        url = search_url.format(search_query)
        page = requests.get(url, headers=headers)
        soup1 = BeautifulSoup(page.content, 'lxml')
        link = soup1.find('a', {'class', 'bookTitle'}).get('href')
        first_result = base_url + link
        page = requests.get(first_result, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")
    genre_box = soup.find_all('a', class_='actionLinkLite bookPageGenreLink')

    top_genres = []
    for j in range(3):
        if j < len(genre_box):
            top_genres.append(genre_box[j].contents[0])

    return top_genres


books_df = pd.read_csv("book_data/updated_books_final_3.csv")

rows, columns = books_df.shape

genres = []

for i in range(250, rows):
    checker = books_df['primary_genre'][i]
    if type(checker) == str:
        continue
    book = books_df.values[i]
    book_id = str(book[1])
    book_title = str(book[3]).split('(')[0]

    try:
        genres = find_genre(book_id, book_title)
    except Exception:
        try:
            genres = find_genre(book_id, book_title)
        except Exception:
            print(book_id)

    if len(genres) > 2:
        books_df['primary_genre'][i] = genres[0]
        books_df['secondary_genre'][i] = genres[1]
        books_df['tertiary_genre'][i] = genres[2]

    genres = []

books_df.to_csv("book_data/updated_books_final.csv", index=False)

end = timeit.default_timer()
time = end - start
print("Total time:", time, "seconds, or", time/60, "minutes.")
# send_msg('done')

# Range: 5      Seconds: 18     Minutes: 0.3    Errors: None
# Range: 10     Seconds: 43     Minutes: 0.7    Errors: 11870085
# Range: 10     Seconds: 35     Minutes: 0.6    Errors: 5907
# Range: 10     Seconds: 44     Minutes: 0.7    Errors: 2657, 4671
# Range: 10     Seconds: 42     Minutes: 0.7    Errors: None  !!DEBUGGER-RUN
# Range: 10     Seconds: 36     Minutes: 0.6    Errors: None  !!DEBUGGER-RUN
# Range: 10     Seconds: 40     Minutes: 0.7    Errors: None  !!DEBUGGER-RUN
# Range: 20     Seconds: 114    Minutes: 1.9    Errors: None  !!DEBUGGER-RUN
# Range: 20     Seconds: 139    Minutes: 2.3    Errors: 1885
# Range: 5      Seconds: 34     Minutes: 0.6    Errors: None  !!DEBUGGER-RUN
# Range: 15     Seconds: 98     Minutes: 1.6    Errors: None  !!DEBUGGER-RUN
# Range: 15     Seconds: 95     Minutes: 1.6    Errors: None
# Range: 1000   Seconds: 5606   Minutes: 93.4   Errors: None
# Range: 1000   Seconds: 5137   Minutes: 85.6   Errors: 156534
# Range: 1000   Seconds: 4987   Minutes: 83.1   Errors: 18667945
# Range: 1000   Seconds: 4190   Minutes: 69.8   Errors: 332631, 568454
# Range: 1000   Seconds: 4396   Minutes: 73.2
# Range: 1000   Seconds: 4442   Minutes: 74.0
# Range: 1000   Seconds: 4182   Minutes: 69.7
# Range: 1000   Seconds: 4072   Minutes: 67.9
# Range: 1000   Seconds: 4213   Minutes: 70.2
# Range: 1000   Seconds: 4137   Minutes: 68.9
