from DataBase import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *
import front_end
import sys

class DBapp(QtWidgets.QMainWindow, front_end.Ui_MainWindow):

    tables = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_up_Button.clicked.connect(self.back_up)
        self.create_Button.clicked.connect(self.create)
        self.delete_Button.clicked.connect(self.delete)
        self.load_back_up_Button.clicked.connect(self.load_back_up)
        self.read_Button.clicked.connect(self.read)
        self.save_Button.clicked.connect(self.save_table)

        self.add_Button.clicked.connect(self.add)
        self.delete_by_id_Button.clicked.connect(self.delete_by_id)

        self.pushButton_11.clicked.connect(self.find_by_id) #Find by id
        self.pushButton_12.clicked.connect(self.edit) #Edit

        self.print_data.clicked.connect(self.go_print_data)

    def save_table(self):
        db_name = self.database_name.text()
        self.tables[db_name].save_db()
        print("data base was saved")

    def create(self):
        db_name = self.database_name.text()
        db = DataBase(db_name)
        self.tables[db_name] = db
        print("data base was created")

    def delete(self):
        db_name = self.database_name.text()
        self.tables[db_name].delete()
        print("data base was deleded")

    def back_up(self):
        db_name = self.database_name.text()
        self.tables[db_name].back_up()
        print("back_up was created")

    def load_back_up(self):
        db_name = self.database_name.text()
        self.tables[db_name].load_backup()
        print("back_up was loaded")

    def read(self):
        db_name = self.database_name.text().split()[0]  + ".csv"
        db_sourse = self.database_name.text().split()[1] + ".csv"
        self.tables[db_name].read_csv(db_sourse)

    def add(self):
        db_name = self.database_name.text()
        id = self.id_1.text()
        name = self.name.text()
        surname = self.surname.text()
        phonenum = self.phone_num.text()
        if phonenum == '':
            self.tables[db_name].add_without_phone(id, name, surname)
        else:
            self.tables[db_name].add_with_phone(id, name, surname, phonenum)
        print("record was added")

    def delete_by_id(self):
        db_name = self.database_name.text()
        id = self.id_1.text()
        self.tables[db_name].del_by_id(id)
        print("record was deleted")

    def find_by_id(self):
        db_name = self.database_name.text()
        id = self.id_2.text()
        #print(self.tables[db_name].data_base[id])
        self.settingdata = True
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Phone num"])
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(id)))
        for j, kk in enumerate(self.tables[db_name].data_base[id].keys()):
            print(kk)
            self.tableWidget.setItem(0, j+1, QTableWidgetItem(str(self.tables[db_name].data_base[id][kk])))
        self.settingdata = False
        self.saved = False

    def edit(self):
        db_name = self.database_name.text()
        id = self.id_2.text()
        new_id = self.new_id.text()
        new_name = self.new_name.text()
        new_surname = self.new_surname.text()
        new_phonenum = self.new_phone_num.text()
        if new_name != '':
            self.tables[db_name].edit_name(id=id, name=new_name)
        if new_surname != '':
            self.tables[db_name].edit_surname(id=id, surname=new_surname)
        if new_phonenum != '':
            self.tables[db_name].edit_phone_num(id=id, phone_num=new_phonenum)
        if new_id != '':
            self.tables[db_name].edit_id(id=id, new_id=new_id)
        print("record was edited")

    def go_print_data(self):
        print(self.tables)
        db_name = self.database_name.text()
        self.settingdata = True
        self.tableWidget.setRowCount(len(self.tables[db_name].data_base.keys()))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Phone num"])
        for i, k in enumerate(self.tables[db_name].data_base.keys()):
            print(type(str(k)))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(k)))
            for j, kk in enumerate(self.tables[db_name].data_base[k].keys()):
                print(kk)
                self.tableWidget.setItem(i, j+1, QTableWidgetItem(str(self.tables[db_name].data_base[k][kk])))
        self.settingdata = False
        self.saved = False
        self.tables[db_name].print_db()

app = QtWidgets.QApplication(sys.argv)
window = DBapp()
window.show()
app.exec_()
