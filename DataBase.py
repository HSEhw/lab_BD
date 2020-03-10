import os
import pandas as pd
import shutil as sh


class DataBase:

    data_base_name = ''
    data_base = {}

    def __init__(self, name):
        self.data_base_name = name + '.csv'
        columns = ['ID', 'Surname', 'Name', 'PhoneNum']
        df = pd.DataFrame(columns=columns)
        df.to_csv(self.data_base_name, index=False, header=True)

    def __del__(self):
        os.remove(self.data_base_name)
        if os.path.exists(self.data_base_name[:-4]+'(backup).csv'):
            os.remove(self.data_base_name[:-4]+'(backup).csv')
        self.data_base.clear()

    def read_csv(self, name):
        df = pd.read_csv(name)
        self.data_base = {}
        for index, row in df.iterrows():
            self.data_base[str(row['ID'])] = {'Surname': row['Surname'], 'Name': row['Name'], 'PhoneNum': row['PhoneNum']}

    def save_db(self):
        columns = ['ID', 'Surname', 'Name', 'PhoneNum']
        df = pd.DataFrame(columns=columns)
        i = 0
        for k in self.data_base.keys():
            df.loc[i] = [k] + list(self.data_base[k].values())
            i += 1
        df.to_csv(self.data_base_name, index=False, header=True)

    def print_db(self):
        for k in self.data_base.keys():
            print(k, ':')
            print('\tSurname  : ', self.data_base[k]['Surname'])
            print('\tName     : ', self.data_base[k]['Name'])
            print('\tPhoneNum : ', self.data_base[k]['PhoneNum'])

    def add_without_phone(self, id, surname, name):
        if id not in self.data_base:
            self.data_base[id] = {'Surname': surname, 'Name': name, 'PhoneNum': '¯\_(ツ)_/¯'}

    def add_with_phone(self, id, surname, name, phone_num):
        if id not in self.data_base:
            self.data_base[id] = {'Surname': surname, 'Name': name, 'PhoneNum': phone_num}

    def del_by_id(self, id):
        if id in self.data_base:
            del self.data_base[id]

    def back_up(self):
        sh.copy(self.data_base_name, self.data_base_name[:-4]+'(backup).csv')

    def load_backup(self):
        if os.path.exists(self.data_base_name):
            os.remove(self.data_base_name)
        sh.copy(self.data_base_name[:-4]+'(backup).csv', self.data_base_name)
        self.read_csv(self.data_base_name)

    def edit_id(self, id, new_id):
        if new_id not in self.data_base:
            self.data_base[new_id] = self.data_base[id]
            del self.data_base[id]

    def edit_surname(self, id, surname):
        self.data_base[id]['Surname'] = surname

    def edit_name(self, id, name):
        self.data_base[id]['Name'] = name

    def edit_phone_num(self, id, phone_num):
        self.data_base[id]['PhoneNum'] = phone_num


if __name__ == '__main__':

    db = DataBase('name')

    db.add_with_phone('84530', 'sar', 'art', '88005553535')
    db.add_without_phone('12345', 'a', 'b')
    db.add_without_phone('12345', 'a', 'a')

    db.save_db()

    db.back_up()
    db.del_by_id('12345')
    db.load_backup()
    db.print_db()

    del db
