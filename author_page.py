# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/author_page.ui'
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
        self.AuthorHelpBtn = QtWidgets.QPushButton(Dialog)
        self.AuthorHelpBtn.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.AuthorHelpBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/QuestionMark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorHelpBtn.setIcon(icon)
        self.AuthorHelpBtn.setIconSize(QtCore.QSize(48, 48))
        self.AuthorHelpBtn.setObjectName("AuthorHelpBtn")
        self.AuthorHomeBtn = QtWidgets.QPushButton(Dialog)
        self.AuthorHomeBtn.setGeometry(QtCore.QRect(680, 40, 75, 75))
        self.AuthorHomeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorHomeBtn.setIcon(icon1)
        self.AuthorHomeBtn.setIconSize(QtCore.QSize(48, 48))
        self.AuthorHomeBtn.setObjectName("AuthorHomeBtn")
        self.AuthorTitleMsg = QtWidgets.QTextBrowser(Dialog)
        self.AuthorTitleMsg.setGeometry(QtCore.QRect(250, 155, 300, 60))
        self.AuthorTitleMsg.setObjectName("AuthorTitleMsg")
        self.AuthorSearchBox = QtWidgets.QLineEdit(Dialog)
        self.AuthorSearchBox.setGeometry(QtCore.QRect(250, 260, 300, 70))
        self.AuthorSearchBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthorSearchBox.setClearButtonEnabled(True)
        self.AuthorSearchBox.setObjectName("AuthorSearchBox")
        self.AuthorSearchBtn = QtWidgets.QPushButton(Dialog)
        self.AuthorSearchBtn.setGeometry(QtCore.QRect(352, 430, 75, 75))
        self.AuthorSearchBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AuthorSearchBtn.setIcon(icon2)
        self.AuthorSearchBtn.setIconSize(QtCore.QSize(48, 48))
        self.AuthorSearchBtn.setObjectName("AuthorSearchBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AuthorTitleMsg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Enter an author you like</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">and discover similar authors</span></p></body></html>"))
        self.AuthorSearchBox.setPlaceholderText(_translate("Dialog", "Enter author here"))