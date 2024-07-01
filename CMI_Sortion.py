# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CMI_Sortion.ui'
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
"font-size:32px;\n"
"color:white;\n"
"font-family:Comfortaa;")
        self.temperature = QPushButton(Dialog)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setGeometry(QRect(44, 3, 431, 311))
        self.temperature.setStyleSheet(u"\n"
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
        self.pressure = QPushButton(Dialog)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setGeometry(QRect(490, 0, 441, 321))
        self.pressure.setStyleSheet(u"\n"
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
        self.enviroment = QPushButton(Dialog)
        self.enviroment.setObjectName(u"enviroment")
        self.enviroment.setGeometry(QRect(490, 320, 441, 311))
        self.enviroment.setStyleSheet(u"\n"
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
        self.rele = QPushButton(Dialog)
        self.rele.setObjectName(u"rele")
        self.rele.setGeometry(QRect(40, 320, 441, 311))
        self.rele.setStyleSheet(u"\n"
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
        self.temperature.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0447\u0438\u043a \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b", None))
        self.pressure.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0447\u0438\u043a \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.enviroment.setText(QCoreApplication.translate("Dialog", u"\u041e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0430\u044f \u0441\u0440\u0435\u0434\u0430", None))
        self.rele.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043b\u0435 \u043f\u043e\u0442\u043e\u043a\u0430", None))
    # retranslateUi

