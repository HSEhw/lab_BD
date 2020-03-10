from DataBase import *
from front_end import *


class DBapp(QtWidgets.QMainWindow, front_end.Ui_MainWindow):

    tables = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_up_Button.connect(self.back_up)
        self.create_Button.connect(self.create)
        self.delete_Button.connect(self.delete)
        self.load_back_up_Button.connect(self.load_back_up)
        self.read_Button.connect(self.read)

        self.add_Button.connect(self.add)
        self.delete_by_id_Button.connect(self.delete_by_id)

        self.pushButton_11.connect(self.find_by_id) #Find by id
        self.pushButton_12.connect(self.edit) #Edit

        self.print_data.connect(self.print_data())

    def create(self):
        db_name = self.data_base_name.text()
        db = DataBase(db_name)
        self.tables[db_name] = db

    def delete(self):
        db_name = self.data_base_name.text()
        self.tables[db_name].__del__()

    def back_up(self):
        db_name = self.data_base_name.text()
        self.tables[db_name].back_up()

    def load_back_up(self):
        db_name = self.data_base_name.text()
        self.tables[db_name].load_backup()

    def read(self):
        db_name = self.data_base_name.text()
        self.tables[db_name].read_csv(db_name)

    def add(self):
        db_name = self.data_base_name.text()
        id = self.id_1.text()
        name = self.name.text()
        surname = self.surname.text()
        phonenum = self.phone_num.text()
        if phonenum == '':
            self.tables[db_name].add_without_phone(id, name, surname)
        else:
            self.tables[db_name].add_with_phone(id, name, surname, phonenum)

    def delete_by_id(self):
        db_name = self.data_base_name.text()
        id = self.id_1.text()
        self.tables[db_name].del_by_id(id)

    def find_by_id(self):
        db_name = self.data_base_name.text()
        id = self.id_2.text()
        print(self.tables[db_name][id])

    def edit(self):
        db_name = self.data_base_name.text()
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
            self.tables[db_name].edit_id(id=id, new_id=id)

    def print_data(self):
        pass