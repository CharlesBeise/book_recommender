import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from book_main_window import Ui_MainWindow
from top_10 import Ui_Dialog as T_10_Dialog
from top_10_result import Ui_Dialog as T_10_R_Dialog
from search_page import Ui_Dialog as S_Dialog
from search_result import Ui_Dialog as SR_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.Top10Btn.clicked.connect(self.top10)
        self.HomeHelpButton.clicked.connect(self.about)
        self.SimilarBtn.clicked.connect(self.search_similar)

    def search_similar(self):
        search_dialog = SearchDialog(self)
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
            "<p>2) Enter a book you have enjoyed to find similar books.</p>"
            "<p>3) Enter an author you have enjoyed to find similar authors.</p>"
            "<p>Enjoy!</p>",
        )


class Top10Dialog(QDialog, T_10_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.Top10HomeButton.clicked.connect(self.reject)
        self.Top10HelpButton.clicked.connect(self.about)
        self.Top10SearchBtn.clicked.connect(self.top10search)

    def top10search(self):
        # genre is set to value currently selected in comboBox
        genre = self.genreBox.currentText()
        t_10_l_dialog = Top10List(genre, self)
        t_10_l_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Please select a genre from the dropdown box.</p>"
            "<p>The top 10 rated books in that genre will be displayed.</p>",
        )


class Top10List(QDialog, T_10_R_Dialog):
    def __init__(self, genre, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.genre = genre
        self.connectSignals()
        self.GenreDisplayBox.setText(self.genre)

    def connectSignals(self):
        self.Top10BackBtn.clicked.connect(self.reject)
        self.Top10HelpBtn.clicked.connect(self.about)

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed the 10 highest rated books in the genre you selected.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


class SearchDialog(QDialog, S_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSearchSignals()

    def connectSearchSignals(self):
        self.SearchHomeBtn.clicked.connect(self.reject)
        self.SearchHelpBtn.clicked.connect(self.about)
        self.SearchSearchBtn.clicked.connect(self.searchsearch)

    def searchsearch(self):
        title = self.SearchBox.text()
        search_result_dialog = SearchResult(title, self)
        search_result_dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Type the title of a book in the box and click the search icon.</p>"
            "<p></p>"
            "<p>Then I will show you books similar to the book you entered!</p>",
        )


class SearchResult(QDialog, SR_Dialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.title = title
        self.connectSignals()
        self.SRUserBook.setText(self.title)

    def connectSignals(self):
        self.SRBackBtn.clicked.connect(self.reject)
        self.SRHelpBtn.clicked.connect(self.about)

    def about(self):
        QMessageBox.about(
            self,
            "About this page",
            "<p>Here we have listed some books you may enjoy, based on the book you entered.</p>"
            "<p></p>"
            "<p>Click on a book to get more information about it!</p>",
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
