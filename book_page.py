# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/book_page.ui'
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
        self.BookHelpBtn = QtWidgets.QPushButton(Dialog)
        self.BookHelpBtn.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.BookHelpBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/QuestionMark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BookHelpBtn.setIcon(icon)
        self.BookHelpBtn.setIconSize(QtCore.QSize(48, 48))
        self.BookHelpBtn.setObjectName("BookHelpBtn")
        self.BookBackBtn = QtWidgets.QPushButton(Dialog)
        self.BookBackBtn.setGeometry(QtCore.QRect(680, 40, 75, 75))
        self.BookBackBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BookBackBtn.setIcon(icon1)
        self.BookBackBtn.setIconSize(QtCore.QSize(48, 48))
        self.BookBackBtn.setObjectName("BookBackBtn")
        self.BookTitleMsg = QtWidgets.QTextBrowser(Dialog)
        self.BookTitleMsg.setGeometry(QtCore.QRect(275, 40, 250, 40))
        self.BookTitleMsg.setObjectName("BookTitleMsg")
        self.BookAuthorMsg = QtWidgets.QTextBrowser(Dialog)
        self.BookAuthorMsg.setGeometry(QtCore.QRect(275, 90, 250, 40))
        self.BookAuthorMsg.setObjectName("BookAuthorMsg")
        self.BookCoverImg = QtWidgets.QLabel(Dialog)
        self.BookCoverImg.setGeometry(QtCore.QRect(560, 160, 200, 300))
        self.BookCoverImg.setText("")
        self.BookCoverImg.setPixmap(QtGui.QPixmap("ui\\images/TheWayofKings.jpg"))
        self.BookCoverImg.setScaledContents(True)
        self.BookCoverImg.setObjectName("BookCoverImg")
        self.BookSummary = QtWidgets.QTextBrowser(Dialog)
        self.BookSummary.setGeometry(QtCore.QRect(20, 160, 480, 410))
        self.BookSummary.setObjectName("BookSummary")
        self.BookBuyBtn = QtWidgets.QPushButton(Dialog)
        self.BookBuyBtn.setGeometry(QtCore.QRect(560, 520, 200, 50))
        self.BookBuyBtn.setObjectName("BookBuyBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.BookTitleMsg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">The Way of Kings</span></p></body></html>"))
        self.BookAuthorMsg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">by Brandon Sanderson</span></p></body></html>"))
        self.BookSummary.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"freeText2603228299155217856\"></a><span style=\" font-family:\'Merriweather,Georgia,serif\'; font-size:11pt; color:#181818; background-color:#ffffff;\">R</span><span style=\" font-family:\'Merriweather,Georgia,serif\'; font-size:11pt; color:#181818; background-color:#ffffff;\">oshar is a world of stone and storms. Uncanny tempests of incredible power sweep across the rocky terrain so frequently that they have shaped ecology and civilization alike. Animals hide in shells, trees pull in branches, and grass retracts into the soilless ground. Cities are built only where the topography offers shelter.<br /><br />It has been centuries since the fall of the ten consecrated orders known as the Knights Radiant, but their Shardblades and Shardplate remain: mystical swords and suits of armor that transform ordinary men into near-invincible warriors. Men trade kingdoms for Shardblades. Wars were fought for them, and won by them.<br /><br />One such war rages on a ruined landscape called the Shattered Plains. There, Kaladin, who traded his medical apprenticeship for a spear to protect his little brother, has been reduced to slavery. In a war that makes no sense, where ten armies fight separately against a single foe, he struggles to save his men and to fathom the leaders who consider them expendable.<br /><br />The result of over ten years of planning, writing, and world-building, The Way of Kings is but the opening movement of the Stormlight Archive, a bold masterpiece in the making.</span></p></body></html>"))
        self.BookBuyBtn.setText(_translate("Dialog", "Click here to buy the book on Amazon!"))
