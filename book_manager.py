import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# Creates a DataFrame object
books_df = pd.read_csv("book_data/books.csv")
book_tags_df = pd.read_csv("book_data/book_tags.csv")
tags_df = pd.read_csv("book_data/tags.csv")
updated_tags = pd.read_csv("book_data/updated_book_tags.csv")

# the shape method returns a tuple containing the number of rows and columns in the DataFrame
rows, columns = books_df.shape

tag_dict = {}
for i in range(updated_tags.shape[0]):
    tag_dict[updated_tags.values[i][0]] = updated_tags.values[i][1]

for i in range(rows):
    book_id = books_df['book_id'][i]
    try:
        genre = tag_dict[book_id]
    except KeyError:
        print(i, book_id, books_df['title'][i])
    if genre:
        books_df['genre'][i] = genre

# books_df.to_csv("book_data/updated_books.csv", index=False)

# with open("book_data/updated_books.csv", 'w', newline='') as updated_books:
#     book_writer = csv.writer(updated_books)
#     for key, value in books_df.items():
#         book_writer.writerow([key, value])
#     updated_books.close()


# This creates a dictionary containing key value pairs where the key is the random number my data file
# tag_dict = {}
#
# for i in range(tags_df.shape[0]):
#     tag_dict[tags_df['tag_id'][i]] = tags_df['tag_name'][i]
#
#
#
# book_tag_dict = {}
#
# x = 0
# last_id = 0
# for i in range(book_tags_df.shape[0]):
#     cur_id = int(book_tags_df['goodreads_book_id'][i])
#     genre = tag_dict.get(book_tags_df['tag_id'][i])
#     if genre:
#         if last_id == cur_id:
#             continue
#             # if x < 3:
#             #     book_tag_dict[cur_id].append(genre)
#             #     x += 1
#         else:
#             book_tag_dict[cur_id] = genre
#             x = 1
#             last_id = cur_id
#
# genre_list = []
#
# for book in book_tag_dict:
#     if book_tag_dict[book] not in genre_list:
#         genre_list.append(book_tag_dict[book])
#
# with open("book_data/updated_book_tags.csv", 'w', newline='') as updated_tag_file:
#     dict_writer = csv.writer(updated_tag_file)
#     for key, value in book_tag_dict.items():
#         dict_writer.writerow([key, value])
#     updated_tag_file.close()
#
# with open("book_data/updated_genre_list.csv", 'w', newline='') as genre_file:
#     genre_writer = csv.writer(genre_file)
#     for genre in genre_list:
#         genre_writer.writerow([genre])
#     genre_file.close()
#
# i = 0
# while i < book_tags_df.shape[0]:
#     temp = tag_dict.get(book_tags_df['tag_id'][i])
#     if temp:
#         book_tags_df['tag_id'][i] = temp
#         i += 1
#     else:
#         book_tags_df.drop(labels=i, axis=0, inplace=True)
#     print(i)
#
# print(book_tags_df.head(99))
#
# book_tags_df.to_csv("book_data/new_book_tags.csv", index=False)
