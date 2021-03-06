# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/top_10_result.ui'
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
        self.Top10BackBtn = QtWidgets.QPushButton(Dialog)
        self.Top10BackBtn.setGeometry(QtCore.QRect(680, 40, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Top10BackBtn.sizePolicy().hasHeightForWidth())
        self.Top10BackBtn.setSizePolicy(sizePolicy)
        self.Top10BackBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Top10BackBtn.setIcon(icon)
        self.Top10BackBtn.setIconSize(QtCore.QSize(48, 48))
        self.Top10BackBtn.setObjectName("Top10BackBtn")
        self.GenreDisplayBox = QtWidgets.QTextBrowser(Dialog)
        self.GenreDisplayBox.setGeometry(QtCore.QRect(275, 120, 250, 60))
        self.GenreDisplayBox.setObjectName("GenreDisplayBox")
        self.Top10Title = QtWidgets.QTextBrowser(Dialog)
        self.Top10Title.setGeometry(QtCore.QRect(350, 50, 100, 40))
        self.Top10Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top10Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Top10Title.setObjectName("Top10Title")
        self.Top10HelpBtn = QtWidgets.QPushButton(Dialog)
        self.Top10HelpBtn.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.Top10HelpBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\images/QuestionMark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Top10HelpBtn.setIcon(icon1)
        self.Top10HelpBtn.setIconSize(QtCore.QSize(48, 48))
        self.Top10HelpBtn.setObjectName("Top10HelpBtn")
        self.Book1 = QtWidgets.QPushButton(Dialog)
        self.Book1.setGeometry(QtCore.QRect(50, 200, 300, 60))
        self.Book1.setText("")
        self.Book1.setObjectName("Book1")
        self.Book2 = QtWidgets.QPushButton(Dialog)
        self.Book2.setGeometry(QtCore.QRect(50, 280, 300, 60))
        self.Book2.setText("")
        self.Book2.setObjectName("Book2")
        self.Book3 = QtWidgets.QPushButton(Dialog)
        self.Book3.setGeometry(QtCore.QRect(50, 360, 300, 60))
        self.Book3.setText("")
        self.Book3.setObjectName("Book3")
        self.Book4 = QtWidgets.QPushButton(Dialog)
        self.Book4.setGeometry(QtCore.QRect(50, 440, 300, 60))
        self.Book4.setText("")
        self.Book4.setObjectName("Book4")
        self.Book5 = QtWidgets.QPushButton(Dialog)
        self.Book5.setGeometry(QtCore.QRect(50, 520, 300, 60))
        self.Book5.setText("")
        self.Book5.setObjectName("Book5")
        self.Book6 = QtWidgets.QPushButton(Dialog)
        self.Book6.setGeometry(QtCore.QRect(450, 200, 300, 60))
        self.Book6.setText("")
        self.Book6.setObjectName("Book6")
        self.Book7 = QtWidgets.QPushButton(Dialog)
        self.Book7.setGeometry(QtCore.QRect(450, 280, 300, 60))
        self.Book7.setText("")
        self.Book7.setObjectName("Book7")
        self.Book8 = QtWidgets.QPushButton(Dialog)
        self.Book8.setGeometry(QtCore.QRect(450, 360, 300, 60))
        self.Book8.setText("")
        self.Book8.setObjectName("Book8")
        self.Book9 = QtWidgets.QPushButton(Dialog)
        self.Book9.setGeometry(QtCore.QRect(450, 440, 300, 60))
        self.Book9.setText("")
        self.Book9.setObjectName("Book9")
        self.Book_10 = QtWidgets.QPushButton(Dialog)
        self.Book_10.setGeometry(QtCore.QRect(450, 520, 300, 60))
        self.Book_10.setText("")
        self.Book_10.setObjectName("Book_10")
        self.Top10BackBtn.raise_()
        self.GenreDisplayBox.raise_()
        self.Top10Title.raise_()
        self.Top10HelpBtn.raise_()
        self.Book2.raise_()
        self.Book3.raise_()
        self.Book4.raise_()
        self.Book5.raise_()
        self.Book6.raise_()
        self.Book7.raise_()
        self.Book8.raise_()
        self.Book9.raise_()
        self.Book_10.raise_()
        self.Book1.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Top10Title.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Top 10</span></p></body></html>"))
