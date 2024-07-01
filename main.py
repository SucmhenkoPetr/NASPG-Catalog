import sys

import PySide6.QtWidgets
from PySide6 import QtWidgets,QtCore,QtSql
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

from  Categories_Dialog import Ui_Dialog as Ui_Categories_Dialog
from Appcatalog import Ui_MainWindow
from Characteristics import Ui_Dialog
from Telephone import Ui_Dialog as UI_Telephone_Dialog
from Search_Window import  Ui_Dialog as UI_Search_Dialog

from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session

from Sort1 import Ui_Dialog as Sort1_Dialog
from Sort2 import Ui_Dialog as Sort2_Dialog
from Sort3 import Ui_Dialog as Sort3_Dialog

from Compressors_Sortion import Ui_Dialog as Ui_Compressors_Sortion_Dialog
from Pumps_Sortion import Ui_Dialog as Ui_Pumps_Sortion_Dialog
from HeatExchangers_Sortion import Ui_Dialog as Ui_HeatExchangers_Sortion_Dialog
from CMI_Sortion import Ui_Dialog as Ui_CMI_Sortion_Dialog
from Error_Dialog import Ui_Dialog as Ui_Error_Dialog

class Sortion(QMainWindow):
    def __init__(self):
        super(Sortion, self).__init__()
        self.user_request = {"size": [None,None,None], "appointment": [None,None,None,None,None], "refrigerant": [None,None,None,None],"type": None}
        self.sort1 = Sort1_Dialog()
        self.sort1.setupUi(self)
        self.sort1.Next.clicked.connect(self.open_sort2)
        self.container1 = False
        self.container2 = False
        self.container3 = False

    def open_sort1(self):
        self.new_window = Sortion()
        self.new_window.show()
    def open_sort2(self):
        self.close()
        if self.container1 == False:
            if self.sort1.Checked1.isChecked() == True:
                self.user_request["size"][0] = "%Малотонажный%"

            if self.sort1.Checked2.isChecked() == True:
                self.user_request["size"][1] = "%Среднетонажный%"

            if self.sort1.Checked3.isChecked() == True:
                self.user_request["size"][2] = "%Высокотонажный%"




        self.container2 = False

        self.user_request["appointment"] = [None,None,None,None,None]
        # print(self.user_sortion)

        self.new_window = QtWidgets.QDialog()
        self.sort2 = Sort2_Dialog()
        self.sort2.setupUi(self.new_window)
        self.new_window.show()
        self.sort2.Next.clicked.connect(self.open_sort3)
        self.sort2.Last.clicked.connect(self.open_sort1)

    def open_sort3(self):
        if self.container2 == False:
            if self.sort2.Checked1_2.isChecked() == True:
                self.user_request["appointment"][0] = "%Производство%"
            if self.sort2.Checked2_2.isChecked() == True:
                self.user_request["appointment"][1] = "%Инфрастр.потребления%"
            if self.sort2.Checked3_2.isChecked() == True:
                self.user_request["appointment"][2] = "%Потребление%"
            if self.sort2.Checked4_2.isChecked() == True:
                self.user_request["appointment"][3] = "%Транспортировка%"
            if self.sort2.Checked5_2.isChecked() == True:
                self.user_request["appointment"][4] = "%Хранение_и_регазификация%"
            self.container2 = True
        self.container3 = False

        self.new_window = QtWidgets.QDialog()
        self.sort3 = Sort3_Dialog()
        self.sort3.setupUi(self.new_window)
        self.new_window.show()

        self.sort3.Last.clicked.connect(self.open_sort2)
        self.sort3.Next.clicked.connect(self.show_me_sortion_categories)


    def Error(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Error_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.Return_to_Sortion.clicked.connect(self.open_sort1)
    def show_me_sortion_categories(self):
        self.close()
        if self.container3 == False:
            if self.sort3.Checked1_3.isChecked() == True:
                self.user_request["refrigerant"][0] = "%Дроссельный%"
            if self.sort3.Checked2_3.isChecked() == True:
                self.user_request["refrigerant"][1] = "%Детандерный%"
            if self.sort3.Checked3_3.isChecked() == True:
                self.user_request["refrigerant"][2] = "%Азотный%"
            if self.sort3.Checked4_3.isChecked() == True:
                self.user_request["refrigerant"][3] = "%Смешанный%"
            self.container3 = True

        global filther
        filther = self.user_request
        if filther["size"] == [None,None,None] or filther["appointment"] == [None,None,None,None,None] or filther["refrigerant"] == [None,None,None,None]:
            self.Error()
        else:
            self.new_window = Categories()
            self.new_window.show()




class Categories(QMainWindow):
    def __init__(self):
        super(Categories, self).__init__()
        self.ui_categories = Ui_Categories_Dialog()
        self.ui_categories.setupUi(self)

        self.ui_categories.Cleaning.clicked.connect(self.Cleaning)
        self.ui_categories.Drying.clicked.connect(self.Drying)
        self.ui_categories.Compressors.clicked.connect(self.Compressors)
        self.ui_categories.Pumps.clicked.connect(self.Pumps)
        self.ui_categories.Tanks.clicked.connect(self.Tanks)
        self.ui_categories.Transportation.clicked.connect(self.Transportation)
        self.ui_categories.CMI.clicked.connect(self.CMI)
        self.ui_categories.Armature.clicked.connect(self.Armature)
        self.ui_categories.HeatExchangers.clicked.connect(self.HeatExchangers)




    def Cleaning(self):
        Categories.close(self)
        global category, names
        category = "Cleaning"
        names = ["Рабочее давление","Температурный диапазон","Температура регенерации","Точка росы","Производительность","Очищаемые газы","Удаляемые примеси","Срок службы"]
        try:
            self.window = Catalog()
            self.window.show()
        except RuntimeError:
            self.Error()
    def Drying(self):
        Categories.close(self)
        global category,names

        category = "Drying"
        names = ["Рабочее давление","Температурный диапазон","Температура точки росы","Производительность","Срок службы"]
        try:
            self.window = Catalog()
            self.window.show()
        except RuntimeError:
            self.Error()
    def Compressors(self):
        Categories.close(self)
        global category,names
        names = ["Тип","Питание","Мощность","Производительность","Срок службы"]
        category = "Compressors"
        try:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_Compressors_Sortion_Dialog()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()
            self.ui_window.spiral.clicked.connect(self.open_catalog)
            self.ui_window.piston.clicked.connect(self.open_catalog)
            self.ui_window.screw.clicked.connect(self.open_catalog)
            self.ui_window.turbine.clicked.connect(self.open_catalog)
        except RuntimeError:
            self.Error(to_sortion=False)



    def Pumps(self):
        Categories.close(self)
        global category,names
        names = ["Питание","Напор","Мощность","Производительность","КПД","Срок службы"]
        category = "Pumps"
        try:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_Pumps_Sortion_Dialog()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()
            self.ui_window.Center.clicked.connect(self.open_catalog)
            self.ui_window.Circle.clicked.connect(self.open_catalog)

        except RuntimeError:
            self.Error(to_sortion=False)
    def Tanks(self):
        Categories.close(self)
        global category,names
        category = "Tanks"
        names = ["Объём","Рабочее давление","Масса груза","Габариты","Тип изоляции","Срок службы","Макс.температура"]
        try:
            self.window = Catalog()
            self.window.show()
        except RuntimeError:
            self.Error()
    def Transportation(self):
        Categories.close(self)
        global category
        category = "Transportation"
        names = [""]
        try:
            self.window = Catalog()
            self.window.show()
        except RuntimeError:
            self.Error()
    def CMI(self):
        Categories.close(self)
        global category,names
        names = ["Диапазон измерений","Погрешноть","Цена деления шкалы","Вес","Размер","Рабочая температура","Дискретность","Частота измерений"]
        category = "CMI"
        try:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_CMI_Sortion_Dialog()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()
            self.ui_window.enviroment.clicked.connect(self.open_catalog)
            self.ui_window.pressure.clicked.connect(self.open_catalog)
            self.ui_window.rele.clicked.connect(self.open_catalog)
            self.ui_window.temperature.clicked.connect(self.open_catalog)

        except RuntimeError:
            self.Error(to_sortion=False)
    def Armature(self):
        Categories.close(self)
        global category,names
        names = ["Диаметр","Сечение","Вес 1 метра","Пластич.до темпер."]
        category = "Armature"
        try:
            self.window = Catalog()
            self.window.show()

        except RuntimeError:
           self.Error(to_sortion=True)
    def HeatExchangers(self):
        Categories.close(self)
        global category,names
        names = ["Рабочее давление","Температура","Тип","Направление потока"]
        category = "HeatExchangers"
        try:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_HeatExchangers_Sortion_Dialog()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()
            self.ui_window.lamellar.clicked.connect(self.open_catalog)
            self.ui_window.piston.clicked.connect(self.open_catalog)
            self.ui_window.shellandtube.clicked.connect(self.open_catalog)
            self.ui_window.turbine.clicked.connect(self.open_catalog)
        except RuntimeError:
            self.Error(to_sortion=False)

    def Error(self,to_sortion = True, selected = None):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Error_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        if to_sortion == True:
            self.ui_window.Return_to_Sortion.clicked.connect(self.return_to_Sortion)
        else:
            if category == "Compressors":
                self.ui_window.Return_to_Sortion.clicked.connect(self.Compressors)
            if category == "Pumps":
                self.ui_window.Return_to_Sortion.clicked.connect(self.Pumps)
            if category == "HeatExchangers":
                self.ui_window.Return_to_Sortion.clicked.connect(self.HeatExchangers)
            if category == "CMI":
                self.ui_window.Return_to_Sortion.clicked.connect(self.CMI)

    def return_to_Sortion(self):
        self.new_window.close()
        print(self.sender().text())
        self.window = Sortion()
        self.window.show()

    def open_catalog(self):#Compressors Pumps HeatExhangers CMI
        sender = self.sender().text() # Название подкатегории
        filther["type"] = sender
        print(filther)
        try:
            self.new_window.close()
            self.window = Catalog()
            self.window.show()
        except RuntimeError:
            self.Error(to_sortion=False)

class Catalog(QMainWindow): # Sumchenko Petr W33052

    def __init__(self):

        self.engine = create_engine("sqlite+pysqlite:///catalog.db", echo=True)
        with Session(self.engine) as s:#Нельзя не выбирать категорию

            query = f""" 
                        SELECT id
                        FROM {category}_Main
                        WHERE (
                            (size LIKE :s_value1 OR size LIKE :s_value2 OR size LIKE :s_value3) 
                            AND (appointment LIKE :app_value1 OR appointment LIKE :app_value2 OR appointment LIKE :app_value3 OR appointment LIKE :app_value4 OR appointment LIKE :app_value5 )
                            AND (refrigerant LIKE :ref_value1 OR refrigerant LIKE :ref_value2 OR refrigerant LIKE :ref_value3 OR refrigerant LIKE :ref_value4)
                            AND (type LIKE :type_value OR type LIKE '-')
                        )

                """

            row = s.execute(text(query),
                {
                    "s_value1": filther["size"][0], "s_value2": filther["size"][1], "s_value3": filther["size"][2],
                    "app_value1":filther["appointment"][0], "app_value2":filther["appointment"][1],"app_value3":filther["appointment"][2],"app_value4":filther["appointment"][3],"app_value5":filther["appointment"][4],
                    "ref_value1":filther["refrigerant"][0],"ref_value2":filther["refrigerant"][1],"ref_value3":filther["refrigerant"][2],"ref_value4":filther["refrigerant"][3],"type_value":filther["type"]
                 }


                        )
            row = row.fetchall()
            self.steps = []
            for r in row:
                self.steps.append(r[0])
            self.maximum = len(self.steps)
            self.i = 0
            if self.steps == []:
                pass
            else:
                super(Catalog, self).__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.Photo.clicked.connect(self.open_new_product_window)
                self.ui.Telephone_Button.clicked.connect(self.open_telephone)
                self.ui.Categories_Button.clicked.connect(self.open_categories)

                self.ui.Right.clicked.connect(self.Right_Step)
                self.ui.Left.clicked.connect(self.Left_Step)

                self.ui.search.clicked.connect(self.search_results)
                query = f"""
                            SELECT *
                            FROM {category}_Main
                            WHERE id = {self.steps[self.i]}
                                                     
                        """
                row = s.execute(text(query))
                pixmapMAIN = QPixmap(f"Photo/{category}/{self.steps[self.i]} 450x438.svg")
                for r in row:
                    self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                    self.ui.Photo.setIconSize(QSize(650,650))
                    self.ui.title.setText(f"{r.title}")
                    self.ui.description1.setText(f"{r.description1}")
                    self.ui.description2.setText(f"{r.description2}")
                    self.ui.description3.setText(f"{r.description3}")
                    self.ui.code.setText(f"{r.code}")
                    self.telephone = r.telephone





        # убрать виндовс
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


    def open_new_product_window(self):

        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)

        with Session(self.engine) as s:
            query = f"""
                   SELECT *
                   FROM {category}
                   WHERE id = {self.steps[self.i]}
                   """


            row = s.execute(text(query))
            pixmap = QPixmap(f"Photo/{category}/{self.steps[self.i]} 319x310.svg")
            for r in row:
                try:
                    self.ui_window.PHOTO.setPixmap(pixmap)
                    self.ui_window.name_par1.setText(names[0])
                    self.ui_window.name_par2.setText(names[1])
                    self.ui_window.name_par3.setText(names[2])
                    self.ui_window.name_par4.setText(names[3])
                    self.ui_window.name_par5.setText(names[4])
                    self.ui_window.name_par6.setText(names[5])
                    self.ui_window.name_par7.setText(names[6])
                    self.ui_window.name_par8.setText(names[7])
                    self.ui_window.name_par9.setText(names[8])
                    self.ui_window.name_par10.setText(names[9])
                except IndexError:
                    pass
                try:
                    self.ui_window.price.setText(f"{r[2]}")
                    self.ui_window.par1.setText(f"{r[3]}")
                    self.ui_window.par2.setText(f"{r[4]}")
                    self.ui_window.par3.setText(f"{r[5]}")
                    self.ui_window.par4.setText(f"{r[6]}")
                    self.ui_window.par5.setText(f"{r[7]}")
                    self.ui_window.par6.setText(f"{r[8]}")
                    self.ui_window.par7.setText(f"{r[9]}")
                    self.ui_window.par8.setText(f"{r[10]}")
                    self.ui_window.par9.setText(f"{r[11]}")
                    self.ui_window.par10.setText(f"{r[12]}")
                except IndexError:
                    pass



        self.new_window.show()
    def open_telephone(self):

        self.new_window = QtWidgets.QDialog()
        self.ui_window = UI_Telephone_Dialog()

        self.ui_window.setupUi(self.new_window)
        with Session(self.engine) as s:

             telephone_query = f"""
                            SELECT telephone
                            FROM {category}_Main
                            WHERE id = {self.steps[self.i]}
                                 """
             row = s.execute(text(telephone_query))
             self.telephone = row.fetchone()[0]


        self.ui_window.telephone.setText(f"{self.telephone}")
        self.new_window.show()
    def open_categories(self):
        Catalog.close(self)
        self.window = Categories()
        self.window.show()

    def Left_Step(self):
        self.i-=1
        if self.i<0:
            self.i = self.maximum - 1
        with Session(self.engine) as s:
            query = f"""
            SELECT *
            FROM {category}_Main
            WHERE id = {self.steps[self.i]}
                           """

            row = s.execute(text(query))
            pixmapMAIN = QPixmap(f"Photo/{category}/{self.steps[self.i]} 450x438.svg")
            for r in row:
                self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                self.ui.Photo.setIconSize(QSize(650,650))
                self.ui.title.setText(f"{r.title}")
                self.ui.description1.setText(f"{r.description1}")
                self.ui.description2.setText(f"{r.description2}")
                self.ui.description3.setText(f"{r.description3}")
                self.ui.code.setText(f"{r.code}")

    def Right_Step(self):
        self.i += 1
        if self.i> self.maximum-1:
            self.i = 0

        with Session(self.engine) as s:
            query = f"""
            SELECT *
            FROM {category}_Main
            WHERE id = {self.steps[self.i]}
                           """

            row = s.execute(text(query))
            pixmapMAIN = QPixmap(f"Photo/{category}/{self.steps[self.i]} 450x438.svg")
            for r in row:
                self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                self.ui.Photo.setIconSize(QSize(650,650))
                self.ui.title.setText(f"{r.title}")
                self.ui.description1.setText(f"{r.description1}")
                self.ui.description2.setText(f"{r.description2}")
                self.ui.description3.setText(f"{r.description3}")
                self.ui.code.setText(f"{r.code}")
        # print(self.step)
    def search_results(self):

        self.request = self.ui.field.toPlainText()

        self.new_window = QtWidgets.QDialog()
        self.ui_window = UI_Search_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.Button1.clicked.connect(self.Button1)
        self.ui_window.Button2.clicked.connect(self.Button2)
        self.ui_window.Button3.clicked.connect(self.Button3)
        self.new_window.show()

        with Session(self.engine) as s:
            query = f"""
                   SELECT *
                   FROM {category}_Main
                   WHERE title LIKE '%{self.request}%'
                   """

            row = s.execute(text(query))
            rows = row.fetchall()
            try:
                global value
                value = []
                value.append(int(rows[0][0]))
                value.append(int(rows[1][0]))
                value.append(int(rows[2][0]))
            except IndexError:
                pass
            for r in rows:
                try:
                    pixmap = QPixmap(f"Photo/{category}/{rows[0][0]} 319x310.svg")
                    self.ui_window.Photo1.setPixmap(pixmap)
                    self.ui_window.price1.setText(f"{rows[0][2]}")
                    self.ui_window.price2.setText(f"{rows[1][2]}")
                    self.ui_window.price3.setText(f"{rows[2][2]}")
                except IndexError:
                    pass
                try:
                    self.ui_window.title1.setText(f"{rows[0][1]}")
                    self.ui_window.title2.setText(f"{rows[1][1]}")
                    self.ui_window.title3.setText(f"{rows[2][1]}")
                except IndexError:
                    pass
                try:
                    self.ui_window.description1.setText(f"{rows[0][3]}")
                    self.ui_window.description2.setText(f"{rows[1][3]}")
                    self.ui_window.description3.setText(f"{rows[2][3]}")
                except IndexError:
                    pass
                try:
                    pixmap1 = QPixmap(f"Photo/{category}/{rows[0][0]} 319x310.svg")
                    self.ui_window.Photo1.setPixmap(pixmap1)
                    pixmap2 = QPixmap(f"Photo/{category}/{rows[1][0]} 319x310.svg")
                    self.ui_window.Photo2.setPixmap(pixmap2)
                    pixmap3 = QPixmap(f"Photo/{category}/{rows[2][0]} 319x310.svg")
                    self.ui_window.Photo3.setPixmap(pixmap3)
                except IndexError:
                    pass

    def Button1(self):
        self.new_window.close()
        self.step = value[0]
        with Session(self.engine) as s:
            query = f"""
            SELECT *
            FROM {category}_Main
            WHERE id = {self.step}
                           """

            row = s.execute(text(query))
            pixmapMAIN = QPixmap(f"Photo/{category}/{self.step} 450x438.svg")
            for r in row:
                self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                self.ui.Photo.setIconSize(QSize(650,650))
                self.ui.title.setText(f"{r.title}")
                self.ui.description1.setText(f"{r.description1}")
                self.ui.description2.setText(f"{r.description2}")
                self.ui.description3.setText(f"{r.description3}")
                self.ui.code.setText(f"{r.code}")

    def Button2(self):
        self.new_window.close()
        self.step = value[1]
        with Session(self.engine) as s:
            query = f"""
            SELECT *
            FROM {category}_Main
            WHERE id = {self.step}
                           """

            row = s.execute(text(query))
            pixmapMAIN = QPixmap(f"Photo/{category}/{self.step} 450x438.svg")
            for r in row:
                self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                self.ui.Photo.setIconSize(QSize(650,650))
                self.ui.title.setText(f"{r.title}")
                self.ui.description1.setText(f"{r.description1}")
                self.ui.description2.setText(f"{r.description2}")
                self.ui.description3.setText(f"{r.description3}")
                self.ui.code.setText(f"{r.code}")

    def Button3(self):
        self.new_window.close()
        self.step = value[2]
        with Session(self.engine) as s:
            query = f"""
            SELECT *
            FROM {category}_Main
            WHERE id = {self.step}
                           """

            row = s.execute(text(query))
            pixmapMAIN = QPixmap(f"Photo/{category}/{self.step} 450x438.svg")
            for r in row:
                self.ui.Photo.setIcon(QPixmap(pixmapMAIN))
                self.ui.Photo.setIconSize(QSize(650,650))
                self.ui.title.setText(f"{r.title}")
                self.ui.description1.setText(f"{r.description1}")
                self.ui.description2.setText(f"{r.description2}")
                self.ui.description3.setText(f"{r.description3}")
                self.ui.code.setText(f"{r.code}")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sortion()
    window.show()
    sys.exit(app.exec())

# from sqlalchemy import text, create_engine
# from sqlalchemy.orm import Session
#
# engine = create_engine("sqlite+pysqlite:///catalog_db.db",echo=True)
# # with Session(engine) as s:
# #     rows = s.execute(text("SELECT * FROM category"))
# #     for r in rows:
# #         print(r)
# with Session(engine) as s:
#     query = """
#     INSERT INTO category (id, title)
#     VALUES(:cid,:t)
#     """
#     s.execute(text(query),{"cid":6,"t":"Agents"})
#     s.commit()







