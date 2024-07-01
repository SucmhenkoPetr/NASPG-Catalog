# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Appcatalog.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resourses_new

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(962, 640)
        MainWindow.setMinimumSize(QSize(962, 640))
        MainWindow.setMaximumSize(QSize(962, 640))
        MainWindow.setStyleSheet(u"background-image:url(\"icons_new/back.jpg\");\n"
"font-family:Comfortaa;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:(0,0,0,0);")
        self.Photo = QPushButton(self.centralwidget)
        self.Photo.setObjectName(u"Photo")
        self.Photo.setGeometry(QRect(480, 40, 441, 441))
        self.Photo.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border-radius:220px;\n"
"border: 3px solid rgba(0,0,0,0);\n"
"background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid rgba(0,0,0,60);\n"
"background-color:rgba(0,0,0,60);\n"
"\n"
"background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(0,0,0,100);\n"
"background-repeat: no-repeat;\n"
"border:3px solid rgba(0,0,0,100);\n"
"}\n"
"\n"
"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 100, 391, 231))
        self.widget.setStyleSheet(u"border:none;\n"
"background:rgba(0,0,0,0)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"font-family:Comfortaa;\n"
"color:rgba(184,188,228,255);\n"
"font-size:24.5pt;\n"
"background:none;")

        self.verticalLayout.addWidget(self.title)

        self.description1 = QTextEdit(self.widget)
        self.description1.setObjectName(u"description1")
        self.description1.setStyleSheet(u"font-size:8pt;\n"
"color:rgba(131,211,244,255);\n"
"border:none;\n"
"background-color:rgba(0,0,0,0);\n"
"padding-bottom:7px;\n"
"")

        self.verticalLayout.addWidget(self.description1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.description2 = QTextEdit(self.widget)
        self.description2.setObjectName(u"description2")
        self.description2.setStyleSheet(u"font-size:8pt;\n"
"color:rgba(185,218,242,255);\n"
"border:none;")

        self.horizontalLayout.addWidget(self.description2)

        self.description3 = QTextEdit(self.widget)
        self.description3.setObjectName(u"description3")
        self.description3.setStyleSheet(u"font-size:8pt;\n"
"color:rgba(185,218,242,255);\n"
"background:(0,0,0,0);\n"
"border:none;\n"
"padding-right:15px;")

        self.horizontalLayout.addWidget(self.description3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Right = QPushButton(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(910, 230, 41, 121))
        self.Right.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:10px;\n"
"background-color:rgba(0,0,0,40);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgba(0,0,0,60);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resourses_new/icons_new/arrow_forward_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Right.setIcon(icon)
        self.Right.setIconSize(QSize(43, 43))
        self.Left = QPushButton(self.centralwidget)
        self.Left.setObjectName(u"Left")
        self.Left.setGeometry(QRect(10, 230, 41, 121))
        self.Left.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:10px;\n"
"background-color:rgba(0,0,0,40);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgba(0,0,0,60);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/resourses_new/icons_new/arrow_back_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Left.setIcon(icon1)
        self.Left.setIconSize(QSize(43, 43))
        self.Widget = QFrame(self.centralwidget)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(590, 460, 251, 61))
        self.Widget.setStyleSheet(u"background:none;\n"
"border:none;")
        self.horizontalLayout_3 = QHBoxLayout(self.Widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border:none;\n"
"background:rgba(0,0,0,0);\n"
"color:rgba(184,188,228,245);\n"
"font-size:15pt;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.code = QLabel(self.Widget)
        self.code.setObjectName(u"code")
        self.code.setStyleSheet(u"border:none;\n"
"background:rgba(0,0,0,0);\n"
"color:rgba(35,223,232,255);\n"
"font-size:15pt;")

        self.horizontalLayout_3.addWidget(self.code)

        self.Telephone_Button = QPushButton(self.centralwidget)
        self.Telephone_Button.setObjectName(u"Telephone_Button")
        self.Telephone_Button.setGeometry(QRect(80, 370, 91, 91))
        self.Telephone_Button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background:none;\n"
"border-radius:45px;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid rgba(0,0,0,60);\n"
"background:rgba(0,0,0,60);\n"
"}\n"
"QPushButton:pressed{\n"
"border:3px solid rgba(0,0,0,100);\n"
"background:rgba(0,0,0,90);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/resourses_new/icons_new/call_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Telephone_Button.setIcon(icon2)
        self.Telephone_Button.setIconSize(QSize(43, 43))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 370, 91, 91))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background:none;\n"
"border-radius:45px;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid rgba(0,0,0,60);\n"
"background:rgba(0,0,0,60);\n"
"}\n"
"QPushButton:pressed{\n"
"border:3px solid rgba(0,0,0,100);\n"
"background:rgba(0,0,0,90);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/resourses_new/icons_new/shopping_cart_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(43, 43))
        self.Categories_Button = QPushButton(self.centralwidget)
        self.Categories_Button.setObjectName(u"Categories_Button")
        self.Categories_Button.setGeometry(QRect(-10, 520, 111, 161))
        self.Categories_Button.setStyleSheet(u"QPushButton{\n"
"background:rgba(0,0,0,0)\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"color:black;\n"
"}\n"
";")
        icon4 = QIcon()
        icon4.addFile(u":/resourses_new/icons_new/\u041a\u043d\u043e\u043f\u043a\u0430 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Categories_Button.setIcon(icon4)
        self.Categories_Button.setIconSize(QSize(90, 90))
        self.Categories_Button.setAutoExclusive(False)
        self.Categories_Button.setAutoRepeatDelay(500)
        self.Categories_Button.setAutoDefault(False)
        self.Categories_Button.setFlat(False)
        self.field = QTextEdit(self.centralwidget)
        self.field.setObjectName(u"field")
        self.field.setGeometry(QRect(80, 40, 261, 31))
        self.field.setStyleSheet(u"border:none;\n"
"background:#b9bce4;\n"
"border-radius:15px;\n"
"padding-top:5px;\n"
"color:white;")
        self.search = QPushButton(self.centralwidget)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(90, 40, 31, 31))
        self.search.setStyleSheet(u"\n"
"QPushButton{\n"
"border:none;\n"
"background:none;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"background:rgba(212,214,241,60);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/resourses_new/icons/search_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon5)
        self.search.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Photo, self.description1)
        QWidget.setTabOrder(self.description1, self.description2)
        QWidget.setTabOrder(self.description2, self.description3)
        QWidget.setTabOrder(self.description3, self.Right)

        self.retranslateUi(MainWindow)

        self.Categories_Button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AppCatalog", None))
        self.Photo.setText("")
        self.title.setText("")
        self.description1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.description2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.description3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Right.setText("")
        self.Left.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u0434 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.code.setText("")
        self.Telephone_Button.setText("")
        self.pushButton_4.setText("")
        self.Categories_Button.setText("")
        self.field.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comfortaa'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.search.setText("")
    # retranslateUi

