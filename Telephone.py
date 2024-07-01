# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telephone.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 105)
        Dialog.setMinimumSize(QSize(700, 105))
        Dialog.setMaximumSize(QSize(700, 105))
        Dialog.setBaseSize(QSize(0, 2))
        Dialog.setStyleSheet(u"background:url(\"icons_new/telephone.jpg\");\n"
"")
        self.telephone = QLabel(Dialog)
        self.telephone.setObjectName(u"telephone")
        self.telephone.setGeometry(QRect(10, 0, 681, 101))
        self.telephone.setStyleSheet(u"background:none;\n"
"border:none;\n"
"font-size:35pt;\n"
"font-family:Acme;\n"
"color:white;\n"
"")
        self.telephone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.telephone.setText(QCoreApplication.translate("Dialog", u"9084671", None))
    # retranslateUi

