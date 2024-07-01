# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Categories_Dialog.ui'
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
        Dialog.resize(960, 660)
        Dialog.setMinimumSize(QSize(960, 660))
        Dialog.setMaximumSize(QSize(960, 660))
        Dialog.setStyleSheet(u"background:url(\"icons_new/Categories.jpg\");")
        self.Cleaning = QPushButton(Dialog)
        self.Cleaning.setObjectName(u"Cleaning")
        self.Cleaning.setGeometry(QRect(0, 0, 321, 211))
        self.Cleaning.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Drying = QPushButton(Dialog)
        self.Drying.setObjectName(u"Drying")
        self.Drying.setGeometry(QRect(320, 0, 321, 211))
        self.Drying.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Compressors = QPushButton(Dialog)
        self.Compressors.setObjectName(u"Compressors")
        self.Compressors.setGeometry(QRect(640, 0, 321, 211))
        self.Compressors.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Pumps = QPushButton(Dialog)
        self.Pumps.setObjectName(u"Pumps")
        self.Pumps.setGeometry(QRect(0, 210, 321, 211))
        self.Pumps.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Tanks = QPushButton(Dialog)
        self.Tanks.setObjectName(u"Tanks")
        self.Tanks.setGeometry(QRect(320, 210, 321, 211))
        self.Tanks.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Transportation = QPushButton(Dialog)
        self.Transportation.setObjectName(u"Transportation")
        self.Transportation.setGeometry(QRect(640, 210, 321, 211))
        self.Transportation.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.CMI = QPushButton(Dialog)
        self.CMI.setObjectName(u"CMI")
        self.CMI.setGeometry(QRect(0, 430, 321, 211))
        self.CMI.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.Armature = QPushButton(Dialog)
        self.Armature.setObjectName(u"Armature")
        self.Armature.setGeometry(QRect(320, 430, 321, 211))
        self.Armature.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")
        self.HeatExchangers = QPushButton(Dialog)
        self.HeatExchangers.setObjectName(u"HeatExchangers")
        self.HeatExchangers.setGeometry(QRect(640, 430, 321, 211))
        self.HeatExchangers.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(13,13,13,55);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(13,13,13,85);\n"
"\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Cleaning.setText("")
        self.Drying.setText("")
        self.Compressors.setText("")
        self.Pumps.setText("")
        self.Tanks.setText("")
        self.Transportation.setText("")
        self.CMI.setText("")
        self.Armature.setText("")
        self.HeatExchangers.setText("")
    # retranslateUi

