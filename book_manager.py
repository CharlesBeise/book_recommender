import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
import os
import glob
import json

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
pd.options.mode.chained_assignment = None


def myFunc(a):
    return a['rating']


author_books = pd.read_csv("book_data/updated_books_final.csv")


def make_top_10(a_entry, a_dict):
    author = a_entry['author']
    if a_dict.get(author):
        if len(a_dict[author]) < 10:
            a_dict[author].append(a_entry)
            a_dict[author].sort(reverse=True, key=myFunc)
        elif a_dict[author][9]['rating'] < a_entry['rating']:
            a_dict[author][9] = a_entry
            a_dict[author].sort(reverse=True, key=myFunc)
    else:
        a_dict[author] = [a_entry]


def author_top_10():
    author_dict = {}
    for i in range(author_books.shape[0]):
        book = {'book_id': int(author_books['book_id'][i]),
                'author': author_books['author'][i],
                'title': author_books['title'][i],
                'rating': float(author_books['average_rating'][i]),
                'votes': int(author_books['ratings_count'][i]),
                'primary': author_books['primary_genre'][i],
                'secondary': author_books['secondary_genre'][i],
                'tertiary': author_books['tertiary_genre'][i]}
        make_top_10(book, author_dict)

    with open('book_data/author_ranked.json', 'w') as outfile:
        json.dump(author_dict, outfile)
        outfile.close()


author_top_10()

# Creates a DataFrame object
# books_df = pd.read_csv("book_data/books.csv")
# book_tags_df = pd.read_csv("book_data/book_tags.csv")
# tags_df = pd.read_csv("book_data/tags.csv")
# updated_tags = pd.read_csv("book_data/updated_book_tags.csv")

# joined_files = os.path.join('book_data', 'updated_books_*.csv')
#
# joined_list = glob.glob(joined_files)
#
# print(joined_list)
#
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
#
# df.to_csv("book_data/updated_books_final.csv", index=False)

# the shape method returns a tuple containing the number of rows and columns in the DataFrame
# rows, columns = books_df.shape
#
# tag_dict = {}
# for i in range(updated_tags.shape[0]):
#     tag_dict[updated_tags.values[i][0]] = updated_tags.values[i][1]
#
# for i in range(rows):
#     book_id = books_df['book_id'][i]
#     try:
#         genre = tag_dict[book_id]
#     except KeyError:
#         print(i, book_id, books_df['title'][i])
#     if genre:
#         books_df['genre'][i] = genre

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

def entry(b, genre_dict):
    rank_list = ['primary', 'secondary', 'tertiary']

    for r in range(3):
        genre = b[rank_list[r]]
        if genre_dict.get(genre):
            if len(genre_dict[genre]) < 10:
                genre_dict[genre].append(b)
                genre_dict[genre].sort(reverse=True, key=myFunc)
            elif genre_dict[genre][9]['rating'] < b['rating']:
                genre_dict[genre][9] = b
                genre_dict[genre].sort(reverse=True, key=myFunc)
        else:
            genre_dict[genre] = [b]


def update_genre_dict():
    updated_books = pd.read_csv('book_data/updated_books_final.csv')
    genre_dict = {}
    for i in range(updated_books.shape[0]):
        book = {'book_id': int(updated_books['book_id'][i]),
                'author': updated_books['author'][i],
                'title': updated_books['title'][i],
                'rating': float(updated_books['average_rating'][i]),
                'votes': int(updated_books['ratings_count'][i]),
                'primary': updated_books['primary_genre'][i],
                'secondary': updated_books['secondary_genre'][i],
                'tertiary': updated_books['tertiary_genre'][i]}
        entry(book, genre_dict)

        # Write to json
    with open('book_data/updated_genre_list_ranked.json', 'w') as outfile:
        json.dump(genre_dict, outfile)
        outfile.close()


def update_authors():
    books = pd.read_csv('book_data/updated_books_final.csv')

    for i in range(books.shape[0]):
        authors = books['author'][i]
        author = authors.split(',')[0]
        books['author'][i] = author

    books.to_csv("book_data/updated_books_final_authors.csv", index=False)


# Write to csv
# with open('book_data/updated_genre_list_ranked.csv', 'w', encoding='utf-8', newline='') as ranked_file:
#     ranked_writer = csv.writer(ranked_file)
#     for key, value in genre_dict.items():
#         thing = [key]
#         for val in value:
#             thing.append(val)
#         ranked_writer.writerow(thing)
#     ranked_file.close()



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
