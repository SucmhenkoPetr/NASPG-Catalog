# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pumps_Sortion.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 640)
        Dialog.setMinimumSize(QSize(960, 640))
        Dialog.setMaximumSize(QSize(960, 640))
        Dialog.setStyleSheet(u"background:url(\"icons_new/\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438.jpg\");\n"
"font-size:48px;\n"
"color:white;\n"
"font-family:Comfortaa;")
        self.Circle = QPushButton(Dialog)
        self.Circle.setObjectName(u"Circle")
        self.Circle.setGeometry(QRect(10, 0, 471, 631))
        self.Circle.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"border-radius:50px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(252,252,252,60);\n"
"}")
        self.Center = QPushButton(Dialog)
        self.Center.setObjectName(u"Center")
        self.Center.setGeometry(QRect(484, 0, 471, 631))
        self.Center.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"border-radius:50px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(252,252,252,60);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Circle.setText(QCoreApplication.translate("Dialog", u"\u0426\u0438\u0440\u043a\u0443\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.Center.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0442\u0440\u043e\u0431\u0435\u0436\u043d\u044b\u0439", None))
    # retranslateUi

