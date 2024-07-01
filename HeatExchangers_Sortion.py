# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HeatExchangers_Sortion.ui'
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
"font-size:42px;\n"
"color:white;\n"
"font-family:Comfortaa;")
        self.shellandtube = QPushButton(Dialog)
        self.shellandtube.setObjectName(u"shellandtube")
        self.shellandtube.setGeometry(QRect(40, 13, 441, 301))
        self.shellandtube.setStyleSheet(u"\n"
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
        self.lamellar = QPushButton(Dialog)
        self.lamellar.setObjectName(u"lamellar")
        self.lamellar.setGeometry(QRect(484, 13, 431, 301))
        self.lamellar.setStyleSheet(u"\n"
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
        self.turbine = QPushButton(Dialog)
        self.turbine.setObjectName(u"turbine")
        self.turbine.setGeometry(QRect(40, 333, 441, 301))
        self.turbine.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"border-radius:50px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(252,252,252,60);\n"
"}")
        self.piston = QPushButton(Dialog)
        self.piston.setObjectName(u"piston")
        self.piston.setGeometry(QRect(484, 333, 431, 301))
        self.piston.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"border-radius:50px;\n"
"font-size:42px;\n"
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
        self.shellandtube.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0436\u0443\u0445\u043e\u0442\u0440\u0443\u0431\u043d\u044b\u0439", None))
        self.lamellar.setText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u0430\u0441\u0442\u0438\u043d\u0447\u0430\u0442\u044b\u0439", None))
        self.turbine.setText(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0443\u0431\u0430 \u0432 \u0442\u0440\u0443\u0431\u0435", None))
        self.piston.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043a\u0440\u043e\u043a\u0430\u043d\u0430\u043b\u044c\u043d\u044b\u0439", None))
    # retranslateUi

