import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget

from gui import Ui_Loggin_Form, Ui_Registration_Form, Ui_Kind_Form, Ui_Adult_Form, Ui_Admin_Form, Ui_Reset_Passwd_Form, Ui_Account_Form
from gui_form_kid import Ui_Form_cartoon_kids, Ui_Form_serials_kids, Ui_Form_new_kids, Ui_Form_comedy_kids, Ui_Form_fantasy_kids, Ui_Form_history_kids
from gui_form import Ui_Form_action, Ui_Form_animation, Ui_Form_comedy, Ui_Form_detective, Ui_Form_dram, Ui_Form_fantasy, Ui_Form_history, Ui_Form_horror,Ui_Form_new, Ui_Form_serial
from gui_form_admin import Ui_Form_action_admin, Ui_Form_animation_admin, Ui_Form_comedy_admin, Ui_Form_detective_admin, Ui_Form_dram_admin, Ui_Form_fantasy_admin, Ui_Form_history_admin, Ui_Form_horror_admin, Ui_Form_new_admin, Ui_Form_serial_admin, Ui_Form_users_database, Ui_Insert_simena_Form, Ui_edit_film_Form
from PyQt5.QtWidgets import QMessageBox
from function import *
from functions_tables_films import *
import time


class Loggin_Form(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Loggin_Form()
        self.ui.setupUi(self)
        self.ui.reg_btn.clicked.connect(self.OpenRegForm)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.login_lk_btn.clicked.connect(self.login_lk)
        self.ui.reset_passwd_btn.clicked.connect(self.OpenResetPasswdForm)

    def OpenResetPasswdForm(self):
        self.reset_passwd_form = ResetPasswd_Form()
        self.reset_passwd_form.show()
    
    def OpenRegForm(self):
        self.reg_form = Registration_Form()
        self.reg_form.show()

    def openAccountForm(self):
        self.account_form = Account_Form()
        self.account_form.setData(get_data(self.ui.username_line_edit.text()))
        self.account_form.show()
    
    def check_data(self):
        if self.ui.username_line_edit.text() and self.ui.password_line_edit.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка ввода данных", "Введены не все данные")
            return False

    def check_passwd(self):
        if get_passwd(self.ui.username_line_edit.text()) == self.ui.password_line_edit.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка входа", "Неверный пароль")
            return False

    def it_is_admin(self):
        self.admin_form = Admin_Form()
        self.admin_form.show()

    def it_is_adult(self):
        self.adult_form = Adult_Form()
        self.adult_form.show()

    def it_is_kid(self):
        self.kid_form = Kid_Form()
        self.kid_form.show()


    def openAdminForm(self):
        QMessageBox.information(self, "Приветствие", f"Здравствуй, {self.ui.username_line_edit.text()}!")
        self.it_is_admin()
        time.sleep(2)
        self.close()

    def openUsersForm(self):
        if (0 < int(get_age(self.ui.username_line_edit.text())) <= 12):
            QMessageBox.information(self, "Приветствие", f"Здравствуй, {self.ui.username_line_edit.text()}!")
            self.it_is_kid()
            time.sleep(2)
            self.close()
            return
        if (12 < int(get_age(self.ui.username_line_edit.text())) < 100):
            QMessageBox.information(self, "Приветствие", f"Здравствуй, {self.ui.username_line_edit.text()}!")
            self.it_is_adult()
            time.sleep(2)
            self.close()
            return

    def login_lk(self):
        print("Заход на проверку введенности")
        if self.check_data():
            if check_loggin(self.ui.username_line_edit.text()):
                QMessageBox.critical(self,"Ошибка", "Данный логин не определен")
                return
            elif self.check_passwd():
                self.openAccountForm()
                return                 
        return

    def login(self):
        if self.check_data():
            if check_loggin(self.ui.username_line_edit.text()):
                QMessageBox.critical(self,"Ошибка", "Данный логин не определен")
                return
            elif self.check_passwd():
                if self.ui.username_line_edit.text() == "admin":
                    self.openAdminForm()
                else:
                    self.openUsersForm()
                return   
        return

class Registration_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Registration_Form()
        self.ui.setupUi(self)
        self.ui.registration_btn.clicked.connect(self.registration)

    def check_data(self):
        if self.ui.name_line_edit.text() and self.ui.age_line_edit.text() and self.ui.emai_line_edit.text() and self.ui.username_reg_line.text() and self.ui.passwd_reg_line.text() and self.ui.checkword_line.text():
            print("проверка введенности данных прошла")
            if 0 < int(self.ui.age_line_edit.text()) < 100:
                print("проверка правильности возраста прошла")
                return True
            else:
                QMessageBox.critical(self, "Ошибка ввода", "Возраст не определен")    
                return False
        else:
            QMessageBox.critical(self,"Ошибка ввода", "Введены не все данные")
            return False

    def check_login(self):
        if self.check_data():
            if check_loggin(self.ui.username_reg_line.text()):
                return True
            else:
                QMessageBox.critical(self, "Ошибка", "Данный логин используется")
                return False
        else:
            return False

    def collect_data(self):
        data = [self.ui.username_reg_line.text(), self.ui.passwd_reg_line.text(), self.ui.name_line_edit.text(), int(self.ui.age_line_edit.text()), self.ui.emai_line_edit.text(), self.ui.checkword_line.text()]
        return data

    def registration(self):
        if self.check_login():
            insert_record_users(self.collect_data())
            QMessageBox.information(self, "Успешно", "Запись добавлена")
            return
        else:
            return

class Account_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Account_Form()
        self.ui.setupUi(self)
        self.ui.delete_btn.clicked.connect(self.delete)
        self.ui.edit_btn.clicked.connect(self.edit)
        
    def setData(self, data):
        self.ui.label.setText(f"Личный кабинет {data[0][3]}")
        self.ui.name_line_account.setText(data[0][0])
        self.ui.age_line_account.setText(data[0][1])
        self.ui.emai_line_account.setText(data[0][2])
        self.ui.username_reg_account.setText(data[0][3])
        self.ui.passwd_reg_account.setText(data[0][4])
        self.ui.checkword_account.setText(data[0][5])
        self.ui.label_2.setText(str(get_id(self.ui.username_reg_account.text())))
        return



    def check_data(self):
        if self.ui.name_line_account.text() and self.ui.age_line_account.text() and self.ui.emai_line_account.text() and self.ui.username_reg_account.text() and self.ui.passwd_reg_account.text() and self.ui.checkword_account.text():
            print("проверка введенности данных прошла")
            if 0 < int(self.ui.age_line_account.text()) < 100:
                print("проверка правильности возраста прошла")
                return True
            else:
                QMessageBox.critical(self, "Ошибка ввода", "Возраст не определен")    
                return False
        else:
            QMessageBox.critical(self,"Ошибка ввода", "Введены не все данные")
            return False

    def check_login(self):
        if self.check_data():
            if self.ui.username_reg_account.text() == get_login(int(self.ui.label_2.text())):
                return True
            elif check_loggin(self.ui.username_reg_account.text()):
                return True      
            else:
                QMessageBox.critical(self, "Ошибка", "Данный логин используется")
                return False
        else:
            return False

    def collect_data(self):
        data = [self.ui.name_line_account.text(), int(self.ui.age_line_account.text()), self.ui.emai_line_account.text(), self.ui.username_reg_account.text(), self.ui.passwd_reg_account.text(), self.ui.checkword_account.text()]
        return data

    def edit(self):
        if self.check_login():
            update_account(int(self.ui.label_2.text()),self.collect_data())
            QMessageBox.information(self, "Успешно", "Запись обновлена")
            return
        else:
            return


    def delete(self):
        if self.check_data():
            delete_account(int(get_id(self.ui.username_reg_account.text())))
            QMessageBox.information(self, "Успешно", "Учетная запись удалена")
            self.close()
            return
        else:
            return


class InsertFilmForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Insert_simena_Form()
        self.ui.setupUi(self)
        self.ui.insert_film_btn.clicked.connect(self.insert_film)

    def set_table_name(self,table_name):
        self.table_name = table_name
        return
    
    def set_genre(self, genre):
        self.genre = genre
        return

    def collect_data(self):
        data = [self.ui.name_film_insert_line_edit.text(), self.ui.country_film_insert_line_edit.text(), int(self.ui.age_lim_flim_insert_line_edit.text()), self.ui.year_film_insert_line.text(),self.ui.director_film_insert_line.text(), self.ui.score_film_insert_line.text(),self.ui.sinosis_film_insert_textEdit.toPlainText()]
        print(self.ui.sinosis_film_insert_textEdit.toPlainText())
        return data

    def check_data(self):
        if self.ui.name_film_insert_line_edit.text() and self.ui.country_film_insert_line_edit.text() and self.ui.age_lim_flim_insert_line_edit.text() and self.ui.year_film_insert_line.text() and self.ui.director_film_insert_line.text() and self.ui.score_film_insert_line.text() and self.ui.sinosis_film_insert_textEdit.toPlainText():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "Введены не все данные")
            return False

    def insert_film(self):
        if self.check_data():
            if self.ui.year_film_insert_line.text() == str(datetime.date.today().year):
                insert_record_film(self.table_name,self.collect_data())
                data = self.collect_data()
                data.append(str(self.genre))
                insert_record_newfilm(data)
                QMessageBox.information(self,"Успешно", f"Запись в таблицы {self.table_name} и newFilm добавлена")
                return
            else:
                insert_record_film(self.table_name,self.collect_data())
                QMessageBox.information(self,"Успешно", f"Запись в таблицу {self.table_name} добавлена")
                return
        else:
            return

class EditFilmForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_edit_film_Form()
        self.ui.setupUi(self)
        self.ui.edit_film_btn.clicked.connect(self.edit_film)

    def set_film_name(self, film_name):
        self.film_name = film_name
        return

    def set_genre(self,genre):
        self.genre = genre
        return

    def data_compl(self):
        self.id = get_id_film(self.genre, self.film_name)
        data = get_data_record_film(self.genre, self.id)
        self.ui.name_film_edit_line_edit.setText(str(data[0][0]))
        self.ui.country_film_edit_line_edit.setText(str(data[0][1]))
        self.ui.age_lim_flim_edit_line_edit.setText(str(data[0][2]))
        self.ui.year_film_edit_line.setText(str(data[0][3]))
        self.ui.director_film_edit_line.setText(str(data[0][4]))
        self.ui.score_film_edit_line.setText(str(data[0][5]))
        self.ui.sinosis_film_edit_textEdit.setText(str(data[0][6]))
        return


    def collect_data(self):
        data = [self.ui.name_film_edit_line_edit.text(), self.ui.country_film_edit_line_edit.text(), int(self.ui.age_lim_flim_edit_line_edit.text()), self.ui.year_film_edit_line.text(), self.ui.director_film_edit_line.text(), self.ui.score_film_edit_line.text(), self.ui.sinosis_film_edit_textEdit.toPlainText()]
        return data

    def check_data(self):
        if self.ui.name_film_edit_line_edit.text() and self.ui.country_film_edit_line_edit.text() and self.ui.age_lim_flim_edit_line_edit.text() and self.ui.year_film_edit_line.text() and self.ui.director_film_edit_line.text() and self.ui.score_film_edit_line.text() and self.ui.sinosis_film_edit_textEdit.toPlainText():
            return True
        else:
            QMessageBox.critical(self,"Ошибка", "Введены не все данные")
            return False

    def edit_film(self):
        if self.check_data():
            update_record_film(self.genre, self.collect_data(), self.id)
            QMessageBox.information(self,"Успешно", f"Запись в таблице {self.genre} обновлена")
        else:
            return

class ResetPasswd_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Reset_Passwd_Form()
        self.ui.setupUi(self)
        self.ui.reset_passwd_btn.clicked.connect(self.reset_passwd)


    def check_data(self):
        if self.ui.username_resetpasswd_line.text() and self.ui.new_passwd_line.text() and self.ui.checkword_resetpasswd_line.text():
            if self.ui.checkword_resetpasswd_line.text() == get_checkword(self.ui.username_resetpasswd_line.text()):
                return True
            else:
                QMessageBox.critical(self, "Ошибка", "Проверочное слово не совпало")
                return False
        else:
            QMessageBox.critical(self, "Ошибка ввода", "Заполнены не все поля")
            return False

    def reset_passwd(self):
        if self.check_data():
            update_passwd(self.ui.username_resetpasswd_line.text(), self.ui.new_passwd_line.text())
            QMessageBox.information(self, "Успешно", "Пароль изменен")
            return

class UsersDataBaseForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_users_database()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_users_database.clicked.connect(self.search_user)
        self.ui.update_action.triggered.connect(lambda some, data=get_all_table_users(): self.loadingTable(data))
        self.ui.update_action.triggered.connect(lambda some: self.ui.search_line_users_database.setText(""))
    
    def loadingTable(self, data=get_all_table_users()):
        self.ui.table_users_database.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_users_database.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_users_database.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def check_data(self):
        if self.ui.search_line_users_database.text():
            return True
        else:
            QMessageBox.warning(self, "Предупреждение", "Строка поиска не содержит запроса")
            return False

    def search_user(self):
        if self.check_data():
            id = get_id_user(self.ui.search_line_users_database.text())
            if id:
                data = get_all_data(id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self,"Предупреждение", "Данной записи нет")
                return
        


class Kid_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Kind_Form()
        self.ui.setupUi(self)
        self.ui.cartoons_btn_kid.clicked.connect(self.openCartoonForm)
        self.ui.comedy_btn_kid.clicked.connect(self.openComedyForm)
        self.ui.fantasy_btn_kid.clicked.connect(self.openFantasyForm)
        self.ui.history_btn_kid.clicked.connect(self.openHistoryForm)
        self.ui.new_btn_kid.clicked.connect(self.openNewForm)
        self.ui.serials_btn_kid.clicked.connect(self.openSerialForm)

    def openCartoonForm(self):
        self.cartoonForm = CartoonKidForm()
        self.cartoonForm.show()

    def openComedyForm(self):
        self.comedyForm = ComedyKidForm()
        self.comedyForm.show()

    def openFantasyForm(self):
        self.fantasyForm = FantasyKidForm()
        self.fantasyForm.show()

    def openHistoryForm(self):
        self.historyForm = HistoryKidForm()
        self.historyForm.show()

    def openSerialForm(self):
        self.serialForm = SerialKidForm()
        self.serialForm.show()

    def openNewForm(self):
        self.newForm = NewKidForm()
        self.newForm.show()

class CartoonKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_cartoon_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_cartoon_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film_kid("cartoons"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_cartoon_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_cartoon_kid.setText(""))
        self.ui.table_cartoon_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("cartoons", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_cartoon_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_cartoon_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("cartoons", item.text())
        return id

    def loadingTable(self, data=get_data_film_kid("cartoons")):
        self.ui.table_cartoon_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_cartoon_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_cartoon_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_cartoon_kid.text()

    def get_id(self,film_name):
        id = get_id_film("cartoons",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_cartoon_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_kid("cartoons", id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class ComedyKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_comedy_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_comedy_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film_kid("comedy"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_comedy_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_comedy_kid.setText(""))
        self.ui.table_comedy_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("comedy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_comedy_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_comedy_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("comedy", item.text())
        return id


    def loadingTable(self, data=get_data_film_kid("comedy")):
        self.ui.table_comedy_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_comedy_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_comedy_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_comedy_kid.text()

    def get_id(self,film_name):
        id = get_id_film("comedy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_comedy_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_kid("comedy", id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return


class FantasyKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_fantasy_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_fantasy_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film_kid("fantasy"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_fantasy_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_fantasy_kid.setText(""))
        self.ui.table_fantasy_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("fantasy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_fantasy_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_fantasy_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("fantasy", item.text())
        return id

    def loadingTable(self, data=get_data_film_kid("fantasy")):
        self.ui.table_fantasy_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_fantasy_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_fantasy_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_fantasy_kid.text()

    def get_id(self,film_name):
        id = get_id_film("fantasy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_fantasy_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_kid("fantasy",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return


class SerialKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_serials_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_serials_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film_kid("serial"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_serials_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_serials_kid.setText(""))
        self.ui.table_serials_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("serial", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_serials_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_serials_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("serial", item.text())
        return id

    def loadingTable(self, data=get_data_film_kid("serial")):
        self.ui.table_serials_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_serials_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_serials_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_serials_kid.text()

    def get_id(self,film_name):
        id = get_id_film("serial",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_serials_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_kid("serial",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return


class HistoryKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_history_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_history_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film_kid("history"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_history_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_history_kid.setText(""))
        self.ui.table_history_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("history", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_history_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_history_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("history", item.text())
        return id

    def loadingTable(self, data=get_data_film_kid("history")):
        self.ui.table_history_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_history_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_history_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_history_kid.text()

    def get_id(self,film_name):
        id = get_id_film("history",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_history_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_kid("history",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return


class NewKidForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_new_kids()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_new_kid.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_newfilm_kid(): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_new_kid.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.label_info_new_kid.setText(""))
        self.ui.table_new_kid.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("newFilm", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.label_info_new_kid.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_new_kid.item(self.coord[0], self.coord[1])
        id = get_id_film("newFilm", item.text())
        return id

    def loadingTable(self, data=get_data_newfilm_kid()):
        self.ui.table_new_kid.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_new_kid.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_new_kid.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_new_kid.text()

    def get_id(self,film_name):
        id = get_id_film("newFilm",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_new_kid.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_newfilm_kid(id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class Admin_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Admin_Form()
        self.ui.setupUi(self)
        self.ui.action_btn_admin.clicked.connect(self.openActionAdminForm)
        self.ui.horror_btn_admin.clicked.connect(self.openHorrorAdminForm)
        self.ui.animation_btn_admin.clicked.connect(self.openAnimationAdminForm)
        self.ui.comedy_btn_admin.clicked.connect(self.openComedyAdminForm)
        self.ui.detective_btn_admin.clicked.connect(self.openDetectiveAdminForm)
        self.ui.dram_btn_admin.clicked.connect(self.openDramAdminForm)
        self.ui.fantasy_btn_admin.clicked.connect(self.openFantasyAdminForm)
        self.ui.serials_btn_admin.clicked.connect(self.openSerialAdminForm)
        self.ui.new_btn_admin.clicked.connect(self.openNewAdminForm)
        self.ui.history_btn_admin.clicked.connect(self.openHistoryAdminForm)
        
    def openSerialAdminForm(self):
        self.serialadminForm = SerialAdminForm()
        self.serialadminForm.show()


    def openActionAdminForm(self):
        self.actionadminForm = ActionAdminForm()
        self.actionadminForm.show()

    def openDetectiveAdminForm(self):
        self.detectiveadminForm = DetectiveAdminForm()
        self.detectiveadminForm.show()

    def openComedyAdminForm(self):
        self.comedyadminForm = ComedyAdminForm()
        self.comedyadminForm.show()

    def openNewAdminForm(self):
        self.newadminForm = NewAdminForm()
        self.newadminForm.show()

    def openFantasyAdminForm(self):
        self.fantasyadminForm = FantasyAdminForm()
        self.fantasyadminForm.show()

    def openHorrorAdminForm(self):
        self.horroradminForm = HorrorAdminForm()
        self.horroradminForm.show()

    def openAnimationAdminForm(self):
        self.animationadminForm = AnimationAdminForm()
        self.animationadminForm.show()

    def openDramAdminForm(self):
        self.dramadminForm = DramAdminForm()
        self.dramadminForm.show()

    def openHistoryAdminForm(self):
        self.historyadminForm = HistoryAdminForm()
        self.historyadminForm.show()

class AnimationAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_animation_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_animation_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_animation_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("cartoons"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_animation_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_animation_admin.setText(""))
        self.ui.table_animation_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("cartoons", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_animation_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_animation_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("cartoons", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("cartoons", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('cartoons')
        self.insertfilmform.set_genre('Анимационный фильм')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("cartoons")
        self.editfilmform.set_film_name(self.ui.table_animation_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("cartoons")):
        self.ui.table_animation_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_animation_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_animation_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_animation_admin.text()

    def get_id(self,film_name):
        id = get_id_film("cartoons",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_animation_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("cartoons",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

    

class ActionAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_action_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_action_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_action_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("action"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_action_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_action_admin.setText(""))
        self.ui.table_action_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("action", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_action_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_action_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("action", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("action", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('action')
        self.insertfilmform.set_genre('Боевик')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("action")
        self.editfilmform.set_film_name(self.ui.table_action_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("action")):
        self.ui.table_action_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_action_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_action_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_action_admin.text()

    def get_id(self,film_name):
        id = get_id_film("action",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_action_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("action",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class DetectiveAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_detective_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_detective_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_detective_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("detective"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_detective_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_detective_admin.setText(""))
        self.ui.table_detective_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("detective", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_detective_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_detective_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("detective", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("detective", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('detective')
        self.insertfilmform.set_genre('Детектив')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("detective")
        self.editfilmform.set_film_name(self.ui.table_detective_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("detective")):
        self.ui.table_detective_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_detective_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_detective_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_detective_admin.text()

    def get_id(self,film_name):
        id = get_id_film("detective",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_detective_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("detective",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class ComedyAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_comedy_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_comedy_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_comedy_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("comedy"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_comedy_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_comedy_admin.setText(""))
        self.ui.table_comedy_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("comedy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_comedy_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_comedy_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("comedy", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("comedy", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('comedy')
        self.insertfilmform.set_genre('Комедия')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("comedy")
        self.editfilmform.set_film_name(self.ui.table_comedy_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("comedy")):
        self.ui.table_comedy_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_comedy_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_comedy_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_comedy_admin.text()

    def get_id(self,film_name):
        id = get_id_film("comedy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_comedy_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("comedy",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

    

class SerialAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_serial_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_serial_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_serial_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("serial"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_serial_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_serial_admin.setText(""))
        self.ui.table_serial_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("serial", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_serial_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_serial_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("serial", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("serial", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('serial')
        self.insertfilmform.set_genre('Сериал')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("serial")
        self.editfilmform.set_film_name(self.ui.table_serial_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("serial")):
        self.ui.table_serial_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_serial_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_serial_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_serial_admin.text()

    def get_id(self,film_name):
        id = get_id_film("serial",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_serial_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("serial",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class HorrorAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_horror_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_horror_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_horror_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("horror"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_horror_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_horror_admin.setText(""))
        self.ui.table_horror_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("horror", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_horror_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_horror_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("horror", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("horror", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('horror')
        self.insertfilmform.set_genre('Фильм ужасов')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("horror")
        self.editfilmform.set_film_name(self.ui.table_horror_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("horror")):
        self.ui.table_horror_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_horror_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_horror_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_horror_admin.text()

    def get_id(self,film_name):
        id = get_id_film("horror",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_horror_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("horror",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class FantasyAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_fantasy_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_fantasy_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_fantasy_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("fantasy"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_fantasy_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_fantasy_admin.setText(""))
        self.ui.table_fantasy_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("fantasy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_fantasy_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_fantasy_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("fantasy", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("fantasy", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return


    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('fantasy')
        self.insertfilmform.set_genre('Фантастический фильм')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("fantasy")
        self.editfilmform.set_film_name(self.ui.table_fantasy_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("fantasy")):
        self.ui.table_fantasy_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_fantasy_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_fantasy_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_fantasy_admin.text()

    def get_id(self,film_name):
        id = get_id_film("fantasy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_fantasy_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("fantasy",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class HistoryAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_history_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_history_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_history_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("history"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_history_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_history_admin.setText(""))
        self.ui.table_history_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("history", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_history_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_history_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("history", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("history", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()
    
    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('history')
        self.insertfilmform.set_genre('Исторический фильм')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("history")
        self.editfilmform.set_film_name(self.ui.table_history_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("history")):
        self.ui.table_history_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_history_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_history_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_history_admin.text()

    def get_id(self,film_name):
        id = get_id_film("history",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_history_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("history",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class DramAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_dram_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.ui.insert_drama_btn.clicked.connect(self.openInsertFilmForm)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.loadingTable()
        self.ui.search_btn_drama_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_film("dram"): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_drama_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_drama_admin.setText(""))
        self.ui.table_drama_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.info_detective_action.triggered.connect(self.info_film)


    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("dram", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_drama_admin.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_drama_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("dram", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("dram", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def openInsertFilmForm(self):
        self.insertfilmform = InsertFilmForm()
        self.insertfilmform.set_table_name('dram')
        self.insertfilmform.set_genre('Драма')
        self.insertfilmform.show()

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("dram")
        self.editfilmform.set_film_name(self.ui.table_drama_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def loadingTable(self, data=get_data_film("dram")):
        self.ui.table_drama_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_drama_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_drama_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_drama_admin.text()

    def get_id(self,film_name):
        id = get_id_film("dram",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_drama_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("dram",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class NewAdminForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_new_admin()
        self.ui.setupUi(self)
        self.ui.db_users_btn.clicked.connect(self.openUsersDataBaseForm)
        self.loadingTable()
        self.ui.search_btn_new_admin.clicked.connect(self.search_film)
        self.ui.update_detective_action.triggered.connect(lambda some, data=get_data_newfilm(): self.loadingTable(data))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.search_line_new_admin.setText(""))
        self.ui.update_detective_action.triggered.connect(lambda some: self.ui.lable_info_new_admin.setText(""))
        self.ui.table_new_admin.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.delete_detective_action.triggered.connect(self.delete_film)
        self.ui.edit_detective_action.triggered.connect(self.openEditFilmForm)
        self.ui.info_detective_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("newFilm", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_new_admin.setText(str)
        return



    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return
    
    def get_id_record(self):
        item = self.ui.table_new_admin.item(self.coord[0], self.coord[1])
        id = get_id_film("newFilm", item.text())
        return id

    def delete_film(self):
        id = self.get_id_record()
        delete_record_film("newFilm", id)
        QMessageBox.information(self, "Успешно", "Запись удалена")
        return 

    def openEditFilmForm(self):
        self.editfilmform = EditFilmForm()
        self.editfilmform.set_genre("newFilm")
        self.editfilmform.set_film_name(self.ui.table_new_admin.item(self.coord[0],self.coord[1]).text())
        self.editfilmform.data_compl()
        self.editfilmform.show()

    def openUsersDataBaseForm(self):
        self.usersdatabaseform = UsersDataBaseForm()
        self.usersdatabaseform.show()

    def loadingTable(self, data=get_data_newfilm()):
        self.ui.table_new_admin.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_new_admin.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_new_admin.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_new_admin.text()

    def get_id(self,film_name):
        id = get_id_film("newFilm",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_new_admin.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_newfilm(id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class Adult_Form(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Adult_Form()
        self.ui.setupUi(self)
        self.ui.action_btn_adult.clicked.connect(self.openActionForm)
        self.ui.comedy_btn_adult.clicked.connect(self.openComedyForm)
        self.ui.detective_btn_adult.clicked.connect(self.openDetectiveForm)
        self.ui.animation_btn_adult.clicked.connect(self.openAnimationForm)
        self.ui.dram_btn_adult.clicked.connect(self.openDramForm)
        self.ui.horror_btn_adult.clicked.connect(self.openHorrorForm)
        self.ui.history_btn_adult.clicked.connect(self.openHistoryForm)
        self.ui.fantasy_btn_adult.clicked.connect(self.openFantasyForm)
        self.ui.serials_btn_adult.clicked.connect(self.openSerialForm)
        self.ui.new_btn_adult.clicked.connect(self.openNewForm)
        
    def openNewForm(self):
        self.newForm = NewForm()
        self.newForm.show()

    def openAnimationForm(self):
        self.animationForm = AnimationForm()
        self.animationForm.show()

    def openDetectiveForm(self):
        self.detectiveForm = DetectiveForm()
        self.detectiveForm.show()

    def openActionForm(self):
        self.actionForm = ActionForm()
        self.actionForm.show()

    def openDramForm(self):
        self.dramForm = DramForm()
        self.dramForm.show()

    def openHistoryForm(self):
        self.historyForm = HistoryForm()
        self.historyForm.show()

    def openHorrorForm(self):
        self.horrorForm = HorrorForm()
        self.horrorForm.show()

    def openComedyForm(self):
        self.comedyForm = ComedyForm()
        self.comedyForm.show()

    def openFantasyForm(self):
        self.fantasyForm = FantasyForm()
        self.fantasyForm.show()

    def openSerialForm(self):
        self.serialForm = SerialForm()
        self.serialForm.show()

class AnimationForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_animation()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_animation.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("cartoons"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_animation.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_animation.setText(""))
        self.ui.table_animation.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("cartoons", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_animation.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_animation.item(self.coord[0], self.coord[1])
        id = get_id_film("cartoons", item.text())
        return id


    def loadingTable(self, data=get_data_film("cartoons")):
        self.ui.table_animation.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_animation.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_animation.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_animation.text()

    def get_id(self,film_name):
        id = get_id_film("cartoons",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_animation.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("cartoons",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class DetectiveForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_detective()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_detective.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("detective"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_detective.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_detective.setText(""))
        self.ui.table_detective.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("detective", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_detective.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_detective.item(self.coord[0], self.coord[1])
        id = get_id_film("detective", item.text())
        return id

    def loadingTable(self, data=get_data_film("detective")):
        self.ui.table_detective.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_detective.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_detective.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return
    
    def get_search_line(self):
        return self.ui.search_line_detective.text()

    def get_id(self,film_name):
        id = get_id_film("detective",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_detective.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("detective",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class DramForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_dram()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_dram.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("dram"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_dram.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_dram.setText(""))
        self.ui.table_dram.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("dram", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_dram.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_dram.item(self.coord[0], self.coord[1])
        id = get_id_film("dram", item.text())
        return id

    def loadingTable(self, data=get_data_film("dram")):
        self.ui.table_dram.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_dram.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_dram.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return
    
    def get_search_line(self):
        return self.ui.search_line_dram.text()

    def get_id(self,film_name):
        id = get_id_film("dram",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_dram.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("dram",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class FantasyForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_fantasy()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_fantasy.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("fantasy"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_fantasy.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_fantasy.setText(""))
        self.ui.table_fantasy.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("fantasy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_fantasy.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_fantasy.item(self.coord[0], self.coord[1])
        id = get_id_film("fantasy", item.text())
        return id


    def loadingTable(self, data=get_data_film("fantasy")):
        self.ui.table_fantasy.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_fantasy.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_fantasy.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_fantasy.text()

    def get_id(self,film_name):
        id = get_id_film("fantasy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_fantasy.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("fantasy",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class SerialForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_serial()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_serial.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("serial"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_serial.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_serial.setText(""))
        self.ui.table_serial.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("serial", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_serial.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_serial.item(self.coord[0], self.coord[1])
        id = get_id_film("serial", item.text())
        return id

    def loadingTable(self, data=get_data_film("serial")):
        self.ui.table_serial.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_serial.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_serial.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_serial.text()

    def get_id(self,film_name):
        id = get_id_film("serial",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_serial.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("serial",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return
    
class ComedyForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_comedy()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_comedy.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("comedy"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_comedy.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_comedy.setText(""))
        self.ui.table_comedy.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("comedy", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_comedy.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_comedy.item(self.coord[0], self.coord[1])
        id = get_id_film("comedy", item.text())
        return id

    def loadingTable(self, data=get_data_film("comedy")):
        self.ui.table_comedy.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_comedy.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_comedy.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_comedy.text()

    def get_id(self,film_name):
        id = get_id_film("comedy",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_comedy.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("comedy",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return
    

class HorrorForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_horror()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_horror.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("horror"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_horror.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_horror.setText(""))
        self.ui.table_horror.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("horror", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_horror.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_horror.item(self.coord[0], self.coord[1])
        id = get_id_film("horror", item.text())
        return id


    def loadingTable(self, data=get_data_film("horror")):
        self.ui.table_horror.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_horror.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_horror.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_horror.text()

    def get_id(self,film_name):
        id = get_id_film("horror",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_horror.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("horror",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class HistoryForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_history()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_history.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("history"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_history.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_history.setText(""))
        self.ui.table_history.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("history", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_history.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_history.item(self.coord[0], self.coord[1])
        id = get_id_film("history", item.text())
        return id

    def loadingTable(self, data=get_data_film("history")):
        self.ui.table_history.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_history.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_history.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_history.text()

    def get_id(self,film_name):
        id = get_id_film("history",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_history.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("history",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class NewForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_new()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_new.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_newfilm(): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_new.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_new.setText(""))
        self.ui.table_new.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("newFilm", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_new.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_new.item(self.coord[0], self.coord[1])
        id = get_id_film("newFilm", item.text())
        return id

    def loadingTable(self, data=get_data_newfilm()):
        self.ui.table_new.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_new.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_new.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_new.text()

    def get_id(self,film_name):
        id = get_id_film("newFilm",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_new.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search_newfilm(id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return

class ActionForm(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_action()
        self.ui.setupUi(self)
        self.loadingTable()
        self.ui.search_btn_action.clicked.connect(self.search_film)
        self.ui.actionupgrade_action.triggered.connect(lambda some, data=get_data_film("action"): self.loadingTable(data))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.search_line_action.setText(""))
        self.ui.actionupgrade_action.triggered.connect(lambda some: self.ui.lable_info_action.setText(""))
        self.ui.table_action.selectionModel().selectionChanged.connect(self.create_coord)
        self.ui.actioninfo_action.triggered.connect(self.info_film)

    def info_film(self):
        id = self.get_id_record()
        data = get_info_film("action", id)
        str = f"""
        Название фильма: <<{data[0][0]}>>
        Режиссер: {data[0][1]}
        Синопсис: <{data[0][2]}>
        """
        self.ui.lable_info_action.setText(str)
        return

    def create_coord(self, selected):
        for x in selected.indexes():
            if x.column() == 0:
                # item = self.ui.table_new.item(x.row(), x.column())
                # print(item.text())
                # print(get_id_film("newFilm",item.text()))
                self.coord = [x.row(), x.column()]
                return
            else:
                return

    def get_id_record(self):
        item = self.ui.table_action.item(self.coord[0], self.coord[1])
        id = get_id_film("action", item.text())
        return id

    def loadingTable(self, data=get_data_film("action")):
        self.ui.table_action.setRowCount(0)
        for row_numb, row_data in enumerate(data):
            self.ui.table_action.insertRow(row_numb)
            for column_numb,data in enumerate(row_data):
                self.ui.table_action.setItem(row_numb,column_numb,QtWidgets.QTableWidgetItem(str(data)))
        return

    def get_search_line(self):
        return self.ui.search_line_action.text()

    def get_id(self,film_name):
        id = get_id_film("action",film_name)
        print(id)
        return id

    def check_request(self):
        if self.ui.search_line_action.text():
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "В поле нет запроса")
            return False

    def search_film(self):
        if self.check_request():
            id = self.get_id(self.get_search_line())
            if id:
                data = get_data_search("action",id)
                self.loadingTable(data)
                return
            else:
                QMessageBox.warning(self, "Предупреждение", "Данной записи нет")
                return
        else:
            return


def main():
    app = QtWidgets.QApplication(sys.argv)
    log_form = Loggin_Form()
    log_form.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

