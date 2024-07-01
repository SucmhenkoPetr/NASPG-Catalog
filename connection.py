import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow
from main import Categories
# from Sort1 import Ui_Dialog as Sort1_Dialog
# from Sort2 import Ui_Dialog as Sort2_Dialog
# from Sort3 import Ui_Dialog as Sort3_Dialog
#
# class Sortion(QMainWindow):
#     def __init__(self):
#         super(Sortion, self).__init__()
#         self.user_sortion = {"size":"","appointment":"","type":""}
#         self.sort1 = Sort1_Dialog()
#         self.sort1.setupUi(self)
#         self.sort1.Next.clicked.connect(self.open_sort2)
#         self.container1 = False
#         self.container2 = False
#         self.container3 = False
#
#
#
#
#
#
#
#     # def open_sort1(self):
#     #
#     #     self.new_window = QtWidgets.QDialog()
#     #     self.ui_window = Sort1_Dialog()
#     #     self.ui_window.setupUi(self.new_window)
#     #     self.new_window.show()
#     #     self.ui_window.Next.clicked.connect(self.open_sort2)
#
#
#     def open_sort1(self):
#         self.new_window = Sortion()
#         self.new_window.show()
#     def open_sort2(self):
#         self.close()
#         if self.sort1.Checked1.isChecked() == True and self.container1 == False:
#             self.user_sortion["size"] += "Малотонажный"
#         if self.sort1.Checked2.isChecked() == True and self.container1 == False:
#             self.user_sortion["size"] += " " + "Среднетонажный"
#         if self.sort1.Checked3.isChecked() == True and self.container1 == False:
#             self.user_sortion["size"] += " " + "Высокотонажный"
#
#         self.container1 = True
#         self.container2 = False
#
#         self.user_sortion["appointment"] = ""
#         # print(self.user_sortion)
#
#         self.new_window = QtWidgets.QDialog()
#         self.sort2 = Sort2_Dialog()
#         self.sort2.setupUi(self.new_window)
#         self.new_window.show()
#         self.sort2.Next.clicked.connect(self.open_sort3)
#         self.sort2.Last.clicked.connect(self.open_sort1)
#
#     def open_sort3(self):
#         if self.container2 == False:
#             if self.sort2.Checked1_2.isChecked() == True:
#                 self.user_sortion["appointment"] += "Производство"
#             if self.sort2.Checked2_2.isChecked() == True:
#                 self.user_sortion["appointment"] += " "+"Инфрастр.потребления"
#             if self.sort2.Checked3_2.isChecked() == True:
#                 self.user_sortion["appointment"] += " " + "Потребление"
#             if self.sort2.Checked4_2.isChecked() == True:
#                 self.user_sortion["appointment"] += " " + "Транспортировка"
#             if self.sort2.Checked5_2.isChecked() == True:
#                 self.user_sortion["appointment"] += " " + "Хранение и Регазификация"
#             self.container2 = True
#         self.container3 = False
#         # print(self.user_sortion)
#         self.new_window = QtWidgets.QDialog()
#         self.sort3 = Sort3_Dialog()
#         self.sort3.setupUi(self.new_window)
#         self.new_window.show()
#         # self.ui_window.Next.clicked.connect(self.open_sort3)
#         self.sort3.Last.clicked.connect(self.open_sort2)
#         self.sort3.Next.clicked.connect(self.show_me_sortion_categories)
#     def show_me_sortion_categories(self):
#         self.new_window.close()
#         if self.container3 == False:
#             if self.sort3.Checked1_3.isChecked() == True:
#                 self.user_sortion["type"] += "Дроссельный"
#             if self.sort3.Checked2_3.isChecked() == True:
#                 self.user_sortion["type"] += " " + "Детандерный"
#             if self.sort3.Checked3_3.isChecked() == True:
#                 self.user_sortion["type"] += " " + "Азотный"
#             if self.sort3.Checked4_3.isChecked() == True:
#                 self.user_sortion["type"] += " " + "Смешанный"
#             self.container3 = True
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Sortion()
#     window.show()
#     sys.exit(app.exec())
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Sortion()
#     window.show()
#     sys.exit(app.exec())
#
# from sqlalchemy import text, create_engine,Column,String
# from sqlalchemy.orm import Session
#
# engine = create_engine("sqlite+pysqlite:///catalog.db", echo=True)


# with Session(engine) as s:
#     query = f"""
#             SELECT id
#             FROM Armature_Main
#             WHERE size = "{filther["size"]}" AND appointment = "{filther["appointment"]}" AND type = "{filther["type"]}"
#                            """
#
#     row = s.execute(text(query))
#     row = row.fetchall()
#
#     steps = []
#     for r in row:
#         steps.append(r[0])
#     print(steps)


# maximum_query = f"""
# SELECT COUNT(*) from {category}_Main
# """
# count = s.execute(text(maximum_query))
# # print(f"Подсчёт строк: {count.fetchone()[0]}")
# self.maximum = count.fetchone()[0]

from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///catalog.db", echo=True)
with Session(engine) as s:
    query = """
            SELECT id 
            FROM Armature_Main
            WHERE (size LIKE :x OR size LIKE :y)
    
    """
    value = None
    value2 = "%Среднетонажный%"
    value3 = None
    row = s.execute(text(query),{"x":value,"y":value2,"z":value3})
    row = row.fetchall()
    print(row)