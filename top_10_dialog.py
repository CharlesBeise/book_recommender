# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/top_10_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.Top10HomeButton = QtWidgets.QPushButton(Dialog)
        self.Top10HomeButton.setGeometry(QtCore.QRect(680, 40, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Top10HomeButton.sizePolicy().hasHeightForWidth())
        self.Top10HomeButton.setSizePolicy(sizePolicy)
        self.Top10HomeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Top10HomeButton.setIcon(icon)
        self.Top10HomeButton.setIconSize(QtCore.QSize(64, 64))
        self.Top10HomeButton.setObjectName("Top10HomeButton")
        self.Top10HelpButton = QtWidgets.QPushButton(Dialog)
        self.Top10HelpButton.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.Top10HelpButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\images/QuestionMark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Top10HelpButton.setIcon(icon1)
        self.Top10HelpButton.setIconSize(QtCore.QSize(48, 48))
        self.Top10HelpButton.setObjectName("Top10HelpButton")
        self.PageTitleMsg = QtWidgets.QTextBrowser(Dialog)
        self.PageTitleMsg.setGeometry(QtCore.QRect(290, 155, 200, 40))
        self.PageTitleMsg.setObjectName("PageTitleMsg")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(300, 265, 180, 30))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.genreBox = QtWidgets.QComboBox(Dialog)
        self.genreBox.setGeometry(QtCore.QRect(300, 330, 180, 30))
        self.genreBox.setObjectName("genreBox")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.SearchBtn = QtWidgets.QPushButton(Dialog)
        self.SearchBtn.setGeometry(QtCore.QRect(352, 430, 75, 75))
        self.SearchBtn.setObjectName("SearchBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PageTitleMsg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Top 10 Books</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Please select a genre:</span></p></body></html>"))
        self.genreBox.setItemText(0, _translate("Dialog", "Horror"))
        self.genreBox.setItemText(1, _translate("Dialog", "Fiction"))
        self.genreBox.setItemText(2, _translate("Dialog", "Mystery"))
        self.genreBox.setItemText(3, _translate("Dialog", "Biography"))
        self.genreBox.setItemText(4, _translate("Dialog", "Suspense"))
        self.genreBox.setItemText(5, _translate("Dialog", "Thriller"))
        self.SearchBtn.setText(_translate("Dialog", "Find a Book!"))
