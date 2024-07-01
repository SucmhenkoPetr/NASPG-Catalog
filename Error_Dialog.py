# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import resourses_new

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 420)
        Dialog.setMinimumSize(QSize(320, 420))
        Dialog.setMaximumSize(QSize(320, 420))
        Dialog.setStyleSheet(u"background: url(\"icons_new/\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430.jpg\");")
        self.Error = QLabel(Dialog)
        self.Error.setObjectName(u"Error")
        self.Error.setGeometry(QRect(0, 70, 321, 261))
        self.Error.setStyleSheet(u" font-size:16pt;\n"
"	font-family:Comfortaa;\n"
"background:none;\n"
"border:none;\n"
"color:white;")
        self.Error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Return_to_Sortion = QPushButton(Dialog)
        self.Return_to_Sortion.setObjectName(u"Return_to_Sortion")
        self.Return_to_Sortion.setGeometry(QRect(50, 340, 221, 41))
        self.Return_to_Sortion.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/resourses_new/icons/arrow_back_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Return_to_Sortion.setIcon(icon)
        self.Return_to_Sortion.setIconSize(QSize(25, 25))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Error.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0432\u0430\u0440\u043e\u0432 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e", None))
        self.Return_to_Sortion.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
    # retranslateUi

