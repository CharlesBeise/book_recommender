import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from book_main_window import Ui_MainWindow
from top_10_dialog import Ui_Dialog
from top_10_list_dialog import Ui_Dialog as T_10_L_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.Top10Btn.clicked.connect(self.top10)
        self.HomeHelpButton.clicked.connect(self.about)

    def top10(self):
        dialog = Top10Dialog(self)
        dialog.exec()

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


class Top10Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.Top10HomeButton.clicked.connect(self.reject)
        self.Top10HelpButton.clicked.connect(self.about)
        self.SearchBtn.clicked.connect(self.search)

    def search(self):
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


class Top10List(QDialog, T_10_L_Dialog):
    def __init__(self, genre, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.genre = genre
        self.connectSignals()
        self.GenreDisplayBox.setText(self.genre)

    def connectSignals(self):
        self.Top10GoBack.clicked.connect(self.reject)

    # def go_back(self):
    #     back_dialog = Top10Dialog(self)
    #     back_dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
