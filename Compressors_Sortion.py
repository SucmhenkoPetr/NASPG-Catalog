# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compressors_Sortion.ui'
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
        self.spiral = QPushButton(Dialog)
        self.spiral.setObjectName(u"spiral")
        self.spiral.setGeometry(QRect(50, 10, 441, 281))
        self.spiral.setStyleSheet(u"\n"
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
        self.piston = QPushButton(Dialog)
        self.piston.setObjectName(u"piston")
        self.piston.setGeometry(QRect(480, 10, 431, 281))
        self.piston.setStyleSheet(u"\n"
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
        self.screw = QPushButton(Dialog)
        self.screw.setObjectName(u"screw")
        self.screw.setGeometry(QRect(50, 330, 441, 301))
        self.screw.setStyleSheet(u"\n"
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
        self.turbine.setGeometry(QRect(480, 330, 431, 301))
        self.turbine.setStyleSheet(u"\n"
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
        self.spiral.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.piston.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u043d\u0442\u043e\u0432\u043e\u0439", None))
        self.screw.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u0448\u043d\u0435\u0432\u043e\u0439", None))
        self.turbine.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u0431\u0438\u043d\u043d\u044b\u0439", None))
    # retranslateUi

