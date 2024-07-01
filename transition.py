

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle
from Search_Window import  Ui_Dialog

class Search(QMainWindow):
    def __init__(self):
        super(Search, self).__init__()

        self.ui_categories = Ui_Dialog()
        self.ui_categories.setupUi(self)

#
# if __name__ == "__main__":
#     app = QApplication()
#     view = QQuickView()
#     view.setSource("styles.qml")
#     view.show()
#     sys.exit(app.exec())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Search()
    window.show()



    # app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("window",window)

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = "styles.qml"
    engine.load(qml_file)

    engine.quit.connect(app.quit)
    sys.exit(app.exec())

