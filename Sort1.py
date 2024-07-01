# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sort1.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resourses_new

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 419)
        Dialog.setMaximumSize(QSize(320, 420))
        Dialog.setStyleSheet(u"background: url(\"icons_new/\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430.jpg\");")
        self.Widget = QWidget(Dialog)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(40, 50, 281, 251))
        self.Widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Widget.setStyleSheet(u"background:none;")
        self.verticalLayout = QVBoxLayout(self.Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Checked1 = QCheckBox(self.Widget)
        self.Checked1.setObjectName(u"Checked1")
        self.Checked1.setStyleSheet(u"QCheckBox{ \n"
"    font-size:16pt;\n"
"	font-family:Comfortaa;\n"
"background:none;\n"
"border:none;\n"
"color:white;\n"
"}\n"
"QCheckBox::indicator {\n"
"   height:20px;\n"
"   width:20px;\n"
"   border-radius:5px;\n"
"	background-color:white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   \n"
"    background:url(\"icons_new/checked.jpg\");\n"
"}")
        self.Checked1.setIconSize(QSize(30, 30))
        self.Checked1.setTristate(False)

        self.verticalLayout.addWidget(self.Checked1)

        self.Checked2 = QCheckBox(self.Widget)
        self.Checked2.setObjectName(u"Checked2")
        self.Checked2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:16pt;\n"
"	font-family:Comfortaa;\n"
"background:none;\n"
"border:none;\n"
"color:white;\n"
"}\n"
"QCheckBox::indicator {\n"
"   height:20px;\n"
"   width:20px;\n"
"   border-radius:5px;\n"
"	background-color:white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   \n"
"    background:url(\"icons_new/checked.jpg\");\n"
"}")

        self.verticalLayout.addWidget(self.Checked2)

        self.Checked3 = QCheckBox(self.Widget)
        self.Checked3.setObjectName(u"Checked3")
        self.Checked3.setStyleSheet(u"QCheckBox{ \n"
"    font-size:16pt;\n"
"	font-family:Comfortaa;\n"
"background:none;\n"
"border:none;\n"
"color:white;\n"
"}\n"
"QCheckBox::indicator {\n"
"   height:20px;\n"
"   width:20px;\n"
"   border-radius:5px;\n"
"	background-color:white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   \n"
"    background:url(\"icons_new/checked.jpg\");\n"
"}")

        self.verticalLayout.addWidget(self.Checked3)

        self.Next = QPushButton(Dialog)
        self.Next.setObjectName(u"Next")
        self.Next.setGeometry(QRect(60, 340, 201, 41))
        self.Next.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:3px solid white;\n"
"border-radius:20px;\n"
"color:white;\n"
"font-family:Comfortaa;;\n"
"font-size:16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background:white;\n"
"color:rgba(36,173,243,255);\n"
"}\n"
"QPushButton:pressed{\n"
"border:none;\n"
"background:rgba(255,255,255,160);\n"
"color:rgba(36,173,243,255);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Checked1.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043b\u043e\u0442\u043e\u043d\u0430\u0436\u043d\u044b\u0439", None))
        self.Checked2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0442\u043e\u043d\u0430\u0436\u043d\u044b\u0439", None))
        self.Checked3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u043e\u043a\u043e\u0442\u043e\u043d\u0430\u0436\u043d\u044b\u0439", None))
        self.Next.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

