import sys
import webbrowser
import json

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QCompleter
from PyQt5 import QtGui

from gui_py_files.book_main_window import Ui_MainWindow
from gui_py_files.book_page import Ui_Dialog as Book_Dialog
from gui_py_files.search_author_page import Ui_Dialog as SA_Dialog
from gui_py_files.author_result import Ui_Dialog as AR_Dialog
from gui_py_files.search_similar_page import Ui_Dialog as S_Dialog
from gui_py_files.similar_result import Ui_Dialog as SR_Dialog
from gui_py_files.top_10 import Ui_Dialog as T_10_Dialog
from gui_py_files.top_10_result import Ui_Dialog as T_10_R_Dialog


from utility_files import goodreads_scraper


class MainWindow(QMainWindow, Ui_MainWindow):
    """This is the main window of the program. From here you can navigate to multiple methods for
    searching for a book"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """Here are the clickable buttons on the page"""
        self.HomeHelpButton.clicked.connect(self.about)
        self.Top10Btn.clicked.connect(self.top10)
        self.SimilarBtn.clicked.connect(self.searchSimilar)
        self.AuthorBtn.clicked.connect(self.searchAuthor)

    def searchAuthor(self):
        """If a user wishes to search by author, this will load a SearchAuthorDialog"""
        author_dialog = SearchAuthorDialog(self)
        author_dialog.exec()

    def searchSimilar(self):
        """If a user wishes to search by similar books, this will load a SearchSimilarDialog"""
        search_dialog = SearchSimilarDialog(self)
        search_dialog.exec()

    def top10(self):
        """If a user wishes to view the top 10 books in a given genre, this will loas a Top10Dialog"""
        top_10_dialog = Top10Dialog(self)
        top_10_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this software",
            "<p>Hello and thank you for using my book recommendation service!</p>"
            "<p>There are three ways you can find book recommendations:</p>"
            "<p>1) View the top 10 books by any given genre.</p>"
            "<p>2) Enter the title of a book to find similar books.</p>"
            "<p>3) View the top 10 books by any given author.</p>"
            "<p>Enjoy!</p>",
        )


class BookDialog(QDialog, Book_Dialog):
    """This page displays a book. It shows the title of the book and name of the author at the top, an image of the
    cover on the right side of the screen, and a description of the book on the left side of the screen. There is also
    a button in the bottom right corner of the screen that will eventually bring the user to the book's Amazon page
    where they can buy the book. Currently this page does not take any parameters, but that will change in future
    versions."""
    def __init__(self, book, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.book = book
        self.loadpage()
        self.connectSignals()

    def loadpage(self):
        """This loads the page elements"""
        cover, description = goodreads_scraper.find_book(str(self.book['book_id']))
        title = "<b><center><p style='font-size: 15px'>" + self.book['title'].split('(')[0] + "</p></center></b>"
        author = "<b><center><p style='font-size: 15px'>By " + self.book['author'] + "</p></center></b>"
        self.BookTitleMsg.setText(title)
        self.BookAuthorMsg.setText(author)
        self.BookSummary.setText(description)
        self.setCoverImage(cover)

    def setCoverImage(self, image):
        """This loads the cover image of the book into the image box"""
        self.BookCoverImg.setPixmap(QtGui.QPixmap(image))
        self.BookCoverImg.setScaledContents(True)
        self.BookCoverImg.setObjectName("BookCoverImg")

    def connectSignals(self):
        """Here are the clickable buttons on the page"""
        self.BookHelpBtn.clicked.connect(self.about)
        self.BookBackBtn.clicked.connect(self.reject)
        self.BookBuyBtn.clicked.connect(self.purchase)

    def purchase(self):
        """When the user clicks the button to purchase the book, this takes them to the Amazon page of the book."""
        with open('input.txt', 'w') as out_file:
            out_file.write(self.book['title'])
            out_file.close()
        book_url = ''
        while book_url == '':
            with open('output.txt', 'r') as title_file:
                book_url = title_file.read()
        webbrowser.open(book_url)
        with open('output.txt', 'w') as clear_file:
            clear_file.write('')
            clear_file.close()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here is a book I think you might like!</p>"
            "<p>Click the link in the bottom right corner to go to Amazon and buy the book.</p>",
        )


class SearchAuthorDialog(QDialog, SA_Dialog):
    """This page allows a user to enter the name of an author in a text box. Then if the user clicks the search button
    it will load a SearchAuthorResult dialog populated with a list of authors similar to the author they entered in the
    text box."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        file = open('book_data/author_ranked.json')
        books = json.load(file)
        authors = books.keys()
        completer = QCompleter(authors)
        completer.setCaseSensitivity(False)
        self.AuthorSearchBox.setCompleter(completer)
        self.connectAuthorSignals()

    def connectAuthorSignals(self):
        """Here are the clickable buttons on the page"""
        self.SAuthorHelpBtn.clicked.connect(self.about)
        self.SAuthorHomeBtn.clicked.connect(self.reject)
        self.AuthorSearchBtn.clicked.connect(self.authorSearch)

    def authorSearch(self):
        """When the user clicks the search button this checks if the user entered an author in the search box. If the
        user did not enter an author in the search box, this prompts them to do so. If they did enter an author in the
        search box this will load a SearchAuthorResult dialog and pass along the name of the author the user entered."""
        author = self.AuthorSearchBox.text()
        if author == "":
            QMessageBox.about(
                self,
                "Error",
                "<p>Please enter an author in the search box.</p>"
            )
        else:
            author_result_dialog = SearchAuthorResult(author, self)
            author_result_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Type the name of an author in the box and click the search icon.</p>"
            "<p></p>"
            "<p>Then I will show you the best books by that author!</p>",
        )


class SearchAuthorResult(QDialog, AR_Dialog):
    """This dialog is called when a user clicks the search button in Search_Author_Dialog. It takes the name of an
    author as a parameter."""
    def __init__(self, author, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.author = author
        # The name of the author the user searched is entered into this box
        name = "<b><center><p style='font-size: 20px'>" + self.author + "</p></center></b>"
        self.ARUserAuthor.setText(name)
        file = open('book_data/author_ranked.json')
        book_dict = json.load(file)
        self.selection = book_dict[self.author]
        self.populateBoxes()
        self.connectSignals()

    def connectSignals(self):
        """Here are the clickable buttons on the page"""
        self.ARBackBtn.clicked.connect(self.reject)
        self.ARHelpBtn.clicked.connect(self.about)
        self.Book1.clicked.connect(lambda: self.loadBookPage(0))
        self.Book2.clicked.connect(lambda: self.loadBookPage(1))
        self.Book3.clicked.connect(lambda: self.loadBookPage(2))
        self.Book4.clicked.connect(lambda: self.loadBookPage(3))
        self.Book5.clicked.connect(lambda: self.loadBookPage(4))
        self.Book6.clicked.connect(lambda: self.loadBookPage(5))
        self.Book7.clicked.connect(lambda: self.loadBookPage(6))
        self.Book8.clicked.connect(lambda: self.loadBookPage(7))
        self.Book9.clicked.connect(lambda: self.loadBookPage(8))
        self.Book_10.clicked.connect(lambda: self.loadBookPage(9))

    def populateBoxes(self):
        """This fills the 10 buttons with information for the top 10 books in the entered genre"""
        book_list = []
        for book in self.selection:
            title = book['title']
            if len(title) > 50:
                title = title.split('(')[0]
            book_list.append(title)
        while len(book_list) < 10:
            book_list.append(f"Sorry, I couldn't find 10 books by {self.author}")
        self.Book1.setText(f'1. {book_list[0]}')
        self.Book2.setText(f'2. {book_list[1]}')
        self.Book3.setText(f'3. {book_list[2]}')
        self.Book4.setText(f'4. {book_list[3]}')
        self.Book5.setText(f'5. {book_list[4]}')
        self.Book6.setText(f'6. {book_list[5]}')
        self.Book7.setText(f'7. {book_list[6]}')
        self.Book8.setText(f'8. {book_list[7]}')
        self.Book9.setText(f'9. {book_list[8]}')
        self.Book_10.setText(f'10. {book_list[9]}')

    def loadBookPage(self, pick):
        """When the user selects a book, this loads a Book dialog with that book's information. Currently does not pass
        any parameters, but this will change in future versions."""
        if pick >= len(self.selection):
            QMessageBox.about(
                self,
                "Oops!",
                "<p>Please select a valid book.</p>"
            )
        else:
            book = self.selection[pick]
            book_dialog = BookDialog(book)
            book_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here is an author and their most popular books.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


class SearchSimilarDialog(QDialog, S_Dialog):
    """This page allows a user to enter the title of a book in a text box. Then if the user clicks the search button
    it will load a SimilarResult dialog populated with a list of books similar to the book they entered in the
    text box."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        file = open('book_data/books_and_genres.json')
        books = json.load(file)
        titles = books.keys()
        completer = QCompleter(titles)
        completer.setCaseSensitivity(False)
        self.SearchBox.setCompleter(completer)
        self.connectSearchSignals()

    def connectSearchSignals(self):
        """Here are the clickable buttons on the page"""
        self.SearchHomeBtn.clicked.connect(self.reject)
        self.SearchHelpBtn.clicked.connect(self.about)
        self.SearchSearchBtn.clicked.connect(self.titleSearch)

    def titleSearch(self):
        """When the user clicks the search button this checks if the user entered a book in the search box. If the
        user did not enter a book in the search box, this prompts them to do so. If they did enter a book in the
        search box this will load a SimilarResult dialog and pass along the title of the book the user entered."""
        title = self.SearchBox.text()
        if title == "":
            QMessageBox.about(
                self,
                "Error",
                "<p>Please enter an book in the search box.</p>"
            )
        else:
            search_result_dialog = SimilarResult(title, self)
            search_result_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Type the title of a book in the box and click the search icon.</p>"
            "<p></p>"
            "<p>Then I will show you books similar to the book you entered!</p>",
        )


class SimilarResult(QDialog, SR_Dialog):
    """This dialog is called when a user clicks the search button in a SearchSimilar dialog. It takes the title of a
    book as a parameter."""
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.title = title
        # The title of the book the user searched is entered into the ARUserAuthor box
        book_name = "<b><center><p style='font-size: 20px'>" + self.title + "</p></center></b>"
        file = open('book_data/books_and_genres.json')
        self.book_dict = json.load(file)
        file2 = open('book_data/books_by_title.json')
        self.master_books = json.load(file2)
        self.target_genres = self.book_dict[title]['genres']
        self.similar_list = []
        self.findSimilar()
        self.populateBoxes()
        self.connectSignals()
        self.SRUserBook.setText(book_name)

    def myFunc(self, a):
        return self.book_dict[a]['rating']

    def findSimilar(self):
        for book in self.book_dict:
            if self.book_dict[book]['genres'] == self.target_genres:
                if book != self.title:
                    self.similar_list.append(book)
        self.similar_list.sort(reverse=True, key=self.myFunc)


    def connectSignals(self):
        """Here are the clickable buttons on the page"""
        self.SRBackBtn.clicked.connect(self.reject)
        self.SRHelpBtn.clicked.connect(self.about)
        self.Book1.clicked.connect(lambda: self.loadBookPage(0))
        self.Book2.clicked.connect(lambda: self.loadBookPage(1))
        self.Book3.clicked.connect(lambda: self.loadBookPage(2))
        self.Book4.clicked.connect(lambda: self.loadBookPage(3))
        self.Book5.clicked.connect(lambda: self.loadBookPage(4))
        self.Book6.clicked.connect(lambda: self.loadBookPage(5))
        self.Book7.clicked.connect(lambda: self.loadBookPage(6))
        self.Book8.clicked.connect(lambda: self.loadBookPage(7))
        self.Book9.clicked.connect(lambda: self.loadBookPage(8))
        self.Book_10.clicked.connect(lambda: self.loadBookPage(9))

    def populateBoxes(self):
        pairs = []
        for book in self.similar_list:
            title = book
            if len(title) > 50:
                title = title.split('(')[0]
            pairs.append([title, f"by {self.master_books[book]['author']}"])
        while len(pairs) < 10:
            pairs.append([f"Sorry, I couldn't find 10 books", ""])
        self.Book1.setText(f'1. {pairs[0][0]} \n {pairs[0][1]}')
        self.Book2.setText(f'2. {pairs[1][0]} \n {pairs[1][1]}')
        self.Book3.setText(f'3. {pairs[2][0]} \n {pairs[2][1]}')
        self.Book4.setText(f'4. {pairs[3][0]} \n {pairs[3][1]}')
        self.Book5.setText(f'5. {pairs[4][0]} \n {pairs[4][1]}')
        self.Book6.setText(f'6. {pairs[5][0]} \n {pairs[5][1]}')
        self.Book7.setText(f'7. {pairs[6][0]} \n {pairs[6][1]}')
        self.Book8.setText(f'8. {pairs[7][0]} \n {pairs[7][1]}')
        self.Book9.setText(f'9. {pairs[8][0]} \n {pairs[8][1]}')
        self.Book_10.setText(f'10. {pairs[9][0]} \n {pairs[9][1]}')

    def loadBookPage(self, pick):
        """When the user selects a book, this loads a Book dialog with that book's information. Currently does not pass
        any parameters, but this will change in future versions."""
        book = self.master_books[self.similar_list[pick]]
        book_dialog = BookDialog(book)
        book_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed some books you may enjoy, based on the book you entered.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


class Top10Dialog(QDialog, T_10_Dialog):
    """This page allows a user to select a book genre. Then when they click the search button it will load a
    Top10Result dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()
        file = open('book_data/updated_genre_list_ranked.json')
        books = json.load(file)
        genres = books.keys()
        completer = QCompleter(genres)
        completer.setCaseSensitivity(False)
        self.genreBox.setCompleter(completer)

    def connectSignals(self):
        """Here are the clickable buttons on the page"""
        self.Top10HomeButton.clicked.connect(self.reject)
        self.Top10HelpButton.clicked.connect(self.about)
        self.Top10SearchBtn.clicked.connect(self.top10Search)

    def top10Search(self):
        """When the user clicks the search button this loads a Top10Result dialog and passes the genre the user
        selected as a parameter."""
        genre = self.genreBox.text()
        t_10_l_dialog = Top10Result(genre, self)
        t_10_l_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Please select a genre from the dropdown box.</p>"
            "<p>The top 10 rated books in that genre will be displayed.</p>",
        )


class Top10Result(QDialog, T_10_R_Dialog):
    """This page displays the top 10 books in a given genre. It takes a genre as a parameter."""
    def __init__(self, genre, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.genre = "<b><center><p style='font-size: 30px'>" + genre + "</p></center></b>"
        file = open('book_data/updated_genre_list_ranked.json')
        book_dict = json.load(file)
        self.selection = book_dict[genre]
        self.GenreDisplayBox.setText(self.genre)
        self.populateBoxes()
        self.connectSignals()

    def connectSignals(self):
        """Here are the clickable buttons on the page"""
        self.Top10BackBtn.clicked.connect(self.reject)
        self.Top10HelpBtn.clicked.connect(self.about)
        self.Book1.clicked.connect(lambda: self.loadBookPage(0))
        self.Book2.clicked.connect(lambda: self.loadBookPage(1))
        self.Book3.clicked.connect(lambda: self.loadBookPage(2))
        self.Book4.clicked.connect(lambda: self.loadBookPage(3))
        self.Book5.clicked.connect(lambda: self.loadBookPage(4))
        self.Book6.clicked.connect(lambda: self.loadBookPage(5))
        self.Book7.clicked.connect(lambda: self.loadBookPage(6))
        self.Book8.clicked.connect(lambda: self.loadBookPage(7))
        self.Book9.clicked.connect(lambda: self.loadBookPage(8))
        self.Book_10.clicked.connect(lambda: self.loadBookPage(9))


    def populateBoxes(self):
        """This fills the 10 buttons with information for the top 10 books in the entered genre"""
        pairs = []
        for book in self.selection:
            title = book['title']
            if len(title) > 50:
                title = title.split('(')[0]
            pairs.append([title, f"by {book['author']}"])
        while len(pairs) < 10:
            pairs.append([f"Sorry, I couldn't find 10 books in this genre", ""])
        self.Book1.setText(f'1. {pairs[0][0]} \n {pairs[0][1]}')
        self.Book2.setText(f'2. {pairs[1][0]} \n {pairs[1][1]}')
        self.Book3.setText(f'3. {pairs[2][0]} \n {pairs[2][1]}')
        self.Book4.setText(f'4. {pairs[3][0]} \n {pairs[3][1]}')
        self.Book5.setText(f'5. {pairs[4][0]} \n {pairs[4][1]}')
        self.Book6.setText(f'6. {pairs[5][0]} \n {pairs[5][1]}')
        self.Book7.setText(f'7. {pairs[6][0]} \n {pairs[6][1]}')
        self.Book8.setText(f'8. {pairs[7][0]} \n {pairs[7][1]}')
        self.Book9.setText(f'9. {pairs[8][0]} \n {pairs[8][1]}')
        self.Book_10.setText(f'10. {pairs[9][0]} \n {pairs[9][1]}')

    def loadBookPage(self, pick):
        """When the user selects a book, this loads a Book dialog with that book's information. Currently does not pass
        any parameters, but this will change in future versions."""
        book = self.selection[pick]
        book_dialog = BookDialog(book)
        book_dialog.exec()

    def about(self):
        """This displays an information alert when the user clicks the About button"""
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed the 10 highest rated books in the genre you selected.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
