# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sort2.ui'
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
        Dialog.resize(320, 420)
        Dialog.setMaximumSize(QSize(320, 420))
        Dialog.setStyleSheet(u"background: url(\"icons_new/\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430.jpg\");")
        self.Widget = QWidget(Dialog)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(30, 50, 291, 281))
        self.Widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Widget.setStyleSheet(u"background:none;")
        self.verticalLayout = QVBoxLayout(self.Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Checked1_2 = QCheckBox(self.Widget)
        self.Checked1_2.setObjectName(u"Checked1_2")
        self.Checked1_2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:12pt;\n"
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
        self.Checked1_2.setIconSize(QSize(30, 30))
        self.Checked1_2.setTristate(False)

        self.verticalLayout.addWidget(self.Checked1_2)

        self.Checked2_2 = QCheckBox(self.Widget)
        self.Checked2_2.setObjectName(u"Checked2_2")
        self.Checked2_2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:12pt;\n"
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

        self.verticalLayout.addWidget(self.Checked2_2)

        self.Checked3_2 = QCheckBox(self.Widget)
        self.Checked3_2.setObjectName(u"Checked3_2")
        self.Checked3_2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:12pt;\n"
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

        self.verticalLayout.addWidget(self.Checked3_2)

        self.Checked4_2 = QCheckBox(self.Widget)
        self.Checked4_2.setObjectName(u"Checked4_2")
        self.Checked4_2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:12pt;\n"
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

        self.verticalLayout.addWidget(self.Checked4_2)

        self.Checked5_2 = QCheckBox(self.Widget)
        self.Checked5_2.setObjectName(u"Checked5_2")
        self.Checked5_2.setStyleSheet(u"QCheckBox{ \n"
"    font-size:12pt;\n"
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

        self.verticalLayout.addWidget(self.Checked5_2)

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
        self.Last = QPushButton(Dialog)
        self.Last.setObjectName(u"Last")
        self.Last.setGeometry(QRect(0, 380, 51, 41))
        self.Last.setStyleSheet(u"\n"
"QPushButton{\n"
"background:none;\n"
"border:none;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(255,255,255,20);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background:rgba(255,255,255,30);\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/resourses_new/icons/arrow_back_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Last.setIcon(icon)
        self.Last.setIconSize(QSize(24, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Checked1_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.Checked2_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u0440\u0430\u0441\u0442\u0440. \u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u044f", None))
        self.Checked3_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u0435", None))
        self.Checked4_2.setText(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.Checked5_2.setText(QCoreApplication.translate("Dialog", u"\u0425\u0440\u0430\u043d\u0438\u043d\u0438\u0435 \u0438 \u0420\u0435\u0433\u0430\u0437\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.Next.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.Last.setText("")
    # retranslateUi

