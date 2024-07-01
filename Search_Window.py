# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Search_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 640)
        Dialog.setMinimumSize(QSize(960, 640))
        Dialog.setMaximumSize(QSize(960, 640))
        Dialog.setStyleSheet(u"background:url(\"icons_new/\u041f\u043e\u0438\u0441\u043a Background.jpg\");")
        self.Photo1 = QLabel(Dialog)
        self.Photo1.setObjectName(u"Photo1")
        self.Photo1.setGeometry(QRect(0, 10, 321, 291))
        self.Photo1.setStyleSheet(u"\n"
"background:none;")
        self.title1 = QLabel(Dialog)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(10, 290, 311, 52))
        self.title1.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:14pt;\n"
"font-family:Comfortaa;\n"
"background:none;\n"
"border:none;")
        self.title1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Photo2 = QLabel(Dialog)
        self.Photo2.setObjectName(u"Photo2")
        self.Photo2.setGeometry(QRect(320, 10, 321, 291))
        self.Photo2.setStyleSheet(u"background:none;")
        self.Photo3 = QLabel(Dialog)
        self.Photo3.setObjectName(u"Photo3")
        self.Photo3.setGeometry(QRect(640, 10, 311, 291))
        self.Photo3.setStyleSheet(u"background:none;")
        self.title2 = QLabel(Dialog)
        self.title2.setObjectName(u"title2")
        self.title2.setGeometry(QRect(320, 290, 321, 52))
        self.title2.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:14pt;\n"
"font-family:Comfortaa;\n"
"background:none;\n"
"border:none;")
        self.title2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title3 = QLabel(Dialog)
        self.title3.setObjectName(u"title3")
        self.title3.setGeometry(QRect(640, 290, 321, 52))
        self.title3.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:14pt;\n"
"font-family:Comfortaa;\n"
"background:none;\n"
"border:none;")
        self.title3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price2 = QLabel(Dialog)
        self.price2.setObjectName(u"price2")
        self.price2.setGeometry(QRect(410, 330, 141, 52))
        self.price2.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:17pt;\n"
"font-family:Acme;\n"
"background:none;\n"
"border:none;")
        self.price2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price1 = QLabel(Dialog)
        self.price1.setObjectName(u"price1")
        self.price1.setGeometry(QRect(90, 330, 141, 52))
        self.price1.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:17pt;\n"
"font-family:Acme;\n"
"background:none;\n"
"border:none;")
        self.price1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price3 = QLabel(Dialog)
        self.price3.setObjectName(u"price3")
        self.price3.setGeometry(QRect(730, 330, 141, 52))
        self.price3.setStyleSheet(u"color:rgba(251,251,252,255);\n"
"font-size:17pt;\n"
"font-family:Acme;\n"
"background:none;\n"
"border:none;")
        self.price3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description1 = QTextBrowser(Dialog)
        self.description1.setObjectName(u"description1")
        self.description1.setGeometry(QRect(60, 391, 201, 211))
        font = QFont()
        font.setFamilies([u"Comfortaa"])
        font.setPointSize(9)
        self.description1.setFont(font)
        self.description1.setStyleSheet(u"color:rgba(151,158,230,255);\n"
"font-size:9pt;\n"
"border:none;\n"
"background:rgba(0,0,0,0);\n"
"")
        self.description1.setFrameShadow(QFrame.Shadow.Raised)
        self.description2 = QTextBrowser(Dialog)
        self.description2.setObjectName(u"description2")
        self.description2.setGeometry(QRect(380, 390, 201, 211))
        self.description2.setFont(font)
        self.description2.setStyleSheet(u"color:rgba(151,158,230,255);\n"
"font-size:9pt;\n"
"border:none;\n"
"background:rgba(0,0,0,0);")
        self.description3 = QTextBrowser(Dialog)
        self.description3.setObjectName(u"description3")
        self.description3.setGeometry(QRect(700, 390, 201, 211))
        self.description3.setFont(font)
        self.description3.setStyleSheet(u"color:rgba(151,158,230,255);\n"
"font-size:9pt;\n"
"border:none;\n"
"background:rgba(0,0,0,0);")
        self.Button1 = QPushButton(Dialog)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setGeometry(QRect(0, 0, 331, 641))
        self.Button1.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"QPushButton::hover{\n"
"background:rgba(62,181,241,40);\n"
"border-radius:40px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background:rgba(62,181,241,60);}")
        self.Button2 = QPushButton(Dialog)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(310, -20, 341, 641))
        self.Button2.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"QPushButton::hover{\n"
"background:rgba(62,181,241,40);\n"
"border-radius:40px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background:rgba(62,181,241,60);}")
        self.Button3 = QPushButton(Dialog)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setGeometry(QRect(630, 0, 331, 641))
        self.Button3.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"QPushButton::hover{\n"
"background:rgba(62,181,241,40);\n"
"border-radius:40px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background:rgba(62,181,241,60);}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Photo1.setText("")
        self.title1.setText("")
        self.Photo2.setText("")
        self.Photo3.setText("")
        self.title2.setText("")
        self.title3.setText("")
        self.price2.setText("")
        self.price1.setText("")
        self.price3.setText("")
        self.description1.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.description2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.description3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Button1.setText("")
        self.Button2.setText("")
        self.Button3.setText("")
    # retranslateUi

