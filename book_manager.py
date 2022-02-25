import pandas as pd
import numpy as np

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# Creates a DataFrame object
books_df = pd.read_csv("book_data/books.csv")
book_tags_df = pd.read_csv("book_data/book_tags.csv")
tags_df = pd.read_csv("book_data/tags.csv")

# the shape method returns a tuple containing the number of rows and columns in the DataFrame
rows, columns = books_df.shape


# This creates a dictionary containing key value pairs where the key is the random number my data file
tag_dict = {}

for i in range(tags_df.shape[0]):
    tag_dict[tags_df['tag_id'][i]] = tags_df['tag_name'][i]


# This c
book_tag_dict = {}

x = 0
last_id = 0
for i in range(book_tags_df.shape[0]):
    cur_id = int(book_tags_df['goodreads_book_id'][i])
    genre = tag_dict.get(book_tags_df['tag_id'][i])
    if genre:
        if last_id == cur_id:
            continue
            # if x < 3:
            #     book_tag_dict[cur_id].append(genre)
            #     x += 1
        else:
            book_tag_dict[cur_id] = genre
            x = 1
            last_id = cur_id

genre_list = []

for book in book_tag_dict:
    if book_tag_dict[book] not in genre_list:
        genre_list.append(book_tag_dict[book])



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

# book_tags_df.to_csv("book_data/new_book_tags.csv", index=False)
