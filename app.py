import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from book_main_window import Ui_MainWindow

from author_page import Ui_Dialog as A_Dialog
from book_page import Ui_Dialog as Book_Dialog
from search_author_page import Ui_Dialog as SA_Dialog
from search_author_result import Ui_Dialog as AR_Dialog
from search_similar_page import Ui_Dialog as S_Dialog
from similar_result import Ui_Dialog as SR_Dialog
from top_10 import Ui_Dialog as T_10_Dialog
from top_10_result import Ui_Dialog as T_10_R_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.Top10Btn.clicked.connect(self.top10)
        self.HomeHelpButton.clicked.connect(self.about)
        self.SimilarBtn.clicked.connect(self.search_similar)
        self.AuthorBtn.clicked.connect(self.search_author)

    def search_author(self):
        author_dialog = SearchAuthorDialog(self)
        author_dialog.exec()

    def search_similar(self):
        search_dialog = SearchSimilarDialog(self)
        search_dialog.exec()

    def top10(self):
        top_10_dialog = Top10Dialog(self)
        top_10_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this software",
            "<p>Hello and thank you for using my book recommendation service!</p>"
            "<p>There are three ways you can find book recommendations:</p>"
            "<p>1) View the top 10 books by any given genre.</p>"
            "<p>2) Enter the title of a book to find similar books.</p>"
            "<p>3) Enter the name of an author to find similar authors.</p>"
            "<p>Enjoy!</p>",
        )


class AuthorDialog(QDialog, A_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.AuthorHelpBtn.clicked.connect(self.about)
        self.AuthorBackBtn.clicked.connect(self.reject)
        self.AuthorBookBtn.clicked.connect(self.book_page)

    def book_page(self):
        book_dialog = BookDialog(self)
        book_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here is an author and their most popular books.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


class BookDialog(QDialog, Book_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.BookHelpBtn.clicked.connect(self.about)
        self.BookBackBtn.clicked.connect(self.reject)
        self.BookBuyBtn.clicked.connect(self.purchase)

    def purchase(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>This will call a teammate's microservice</p>",
        )

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here is a book I think you might like!</p>"
            "<p>Click the link in the bottom right corner to go to Amazon and buy the book.</p>",
        )


class SearchAuthorDialog(QDialog, SA_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectAuthorSignals()

    def connectAuthorSignals(self):
        self.SAuthorHelpBtn.clicked.connect(self.about)
        self.SAuthorHomeBtn.clicked.connect(self.reject)
        self.AuthorSearchBtn.clicked.connect(self.authorSearch)

    def authorSearch(self):
        author = self.AuthorSearchBox.text()
        author_result_dialog = SearchAuthorResult(author, self)
        author_result_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Type the name of an author in the box and click the search icon.</p>"
            "<p></p>"
            "<p>Then I will show you authors similar to the author you entered!</p>",
        )


class SearchAuthorResult(QDialog, AR_Dialog):
    """This dialog is called when a user clicks the search button in Search_Author_Dialog"""
    def __init__(self, author, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # The name of the author the user searched is entered into this box
        self.ARUserAuthor.setText(author)
        self.connectSignals()

    def connectSignals(self):
        self.ARBackBtn.clicked.connect(self.reject)
        self.ARHelpBtn.clicked.connect(self.about)
        self.ARAuthorBtn.clicked.connect(self.author)

    def author(self):
        # When the user selects an author, this loads an Author_Dialog with that author's information
        author_dialog = AuthorDialog(self)
        author_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed some authors you may enjoy, based on the author you entered.</p>"
            "<p></p>"
            "<p>Click on an author to get more information about them!</p>",
        )


class SearchSimilarDialog(QDialog, S_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSearchSignals()

    def connectSearchSignals(self):
        self.SearchHomeBtn.clicked.connect(self.reject)
        self.SearchHelpBtn.clicked.connect(self.about)
        self.SearchSearchBtn.clicked.connect(self.searchSearch)

    def searchSearch(self):
        title = self.SearchBox.text()
        search_result_dialog = SimilarResult(title, self)
        search_result_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Type the title of a book in the box and click the search icon.</p>"
            "<p></p>"
            "<p>Then I will show you books similar to the book you entered!</p>",
        )


class SimilarResult(QDialog, SR_Dialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.title = title
        self.connectSignals()
        self.SRUserBook.setText(self.title)

    def connectSignals(self):
        self.SRBackBtn.clicked.connect(self.reject)
        self.SRHelpBtn.clicked.connect(self.about)
        self.SRBookBtn.clicked.connect(self.book_page)

    def book_page(self):
        book_dialog = BookDialog(self)
        book_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed some books you may enjoy, based on the book you entered.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


class Top10Dialog(QDialog, T_10_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.Top10HomeButton.clicked.connect(self.reject)
        self.Top10HelpButton.clicked.connect(self.about)
        self.Top10SearchBtn.clicked.connect(self.top10Search)

    def top10Search(self):
        # genre is set to value currently selected in comboBox
        genre = self.genreBox.currentText()
        t_10_l_dialog = Top10Result(genre, self)
        t_10_l_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Please select a genre from the dropdown box.</p>"
            "<p>The top 10 rated books in that genre will be displayed.</p>",
        )


class Top10Result(QDialog, T_10_R_Dialog):
    def __init__(self, genre, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.genre = genre
        self.connectSignals()
        self.GenreDisplayBox.setText(self.genre)

    def connectSignals(self):
        self.Top10BackBtn.clicked.connect(self.reject)
        self.Top10HelpBtn.clicked.connect(self.about)
        self.Top10BookBtn.clicked.connect(self.book_page)

    def book_page(self):
        book_dialog = BookDialog(self)
        book_dialog.exec()

    def about(self):
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
