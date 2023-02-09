
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loggin_Form(object):
    def setupUi(self, Loggin_Form):
        Loggin_Form.setObjectName("Loggin_Form")
        Loggin_Form.resize(529, 674)
        Loggin_Form.setStyleSheet("background-color: rgb(129, 61, 156);\n"
"")
        self.label = QtWidgets.QLabel(Loggin_Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 451, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: rgb(246, 245, 244);\n"
"")
        self.label.setObjectName("label")
        self.username_line_edit = QtWidgets.QLineEdit(Loggin_Form)
        self.username_line_edit.setGeometry(QtCore.QRect(60, 160, 411, 61))
        self.username_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30;\n"
"padding-left:20")
        self.username_line_edit.setObjectName("username_line_edit")
        self.password_line_edit = QtWidgets.QLineEdit(Loggin_Form)
        self.password_line_edit.setGeometry(QtCore.QRect(60, 250, 411, 61))
        self.password_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30;\n"
"padding-left:20")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.login_btn = QtWidgets.QPushButton(Loggin_Form)
        self.login_btn.setGeometry(QtCore.QRect(160, 370, 241, 51))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.reg_btn = QtWidgets.QPushButton(Loggin_Form)
        self.reg_btn.setGeometry(QtCore.QRect(160, 500, 241, 51))
        self.reg_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.reg_btn.setObjectName("reg_btn")
        self.reset_passwd_btn = QtWidgets.QPushButton(Loggin_Form)
        self.reset_passwd_btn.setGeometry(QtCore.QRect(340, 600, 161, 41))
        self.reset_passwd_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.reset_passwd_btn.setObjectName("reset_passwd_btn")
        self.login_lk_btn = QtWidgets.QPushButton(Loggin_Form)
        self.login_lk_btn.setGeometry(QtCore.QRect(160, 430, 241, 61))
        self.login_lk_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.login_lk_btn.setObjectName("login_lk_btn")

        self.retranslateUi(Loggin_Form)
        QtCore.QMetaObject.connectSlotsByName(Loggin_Form)

    def retranslateUi(self, Loggin_Form):
        _translate = QtCore.QCoreApplication.translate
        Loggin_Form.setWindowTitle(_translate("Loggin_Form", "Окно авторизации"))
        self.label.setText(_translate("Loggin_Form", "Авторизация пользователей"))
        self.username_line_edit.setPlaceholderText(_translate("Loggin_Form", "Введите логин"))
        self.password_line_edit.setPlaceholderText(_translate("Loggin_Form", "Введите пароль"))
        self.login_btn.setText(_translate("Loggin_Form", "Войти в систему"))
        self.reg_btn.setText(_translate("Loggin_Form", "Регистрация"))
        self.reset_passwd_btn.setText(_translate("Loggin_Form", "Сброс пароля"))
        self.login_lk_btn.setText(_translate("Loggin_Form", "Войти в личный кабинет"))


class Ui_Account_Form(object):
    def setupUi(self, Account_Form):
        Account_Form.setObjectName("Account_Form")
        Account_Form.resize(615, 841)
        Account_Form.setStyleSheet("background-color: rgb(129, 61, 156);")
        self.label = QtWidgets.QLabel(Account_Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 371, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label.setText("")
        self.label.setObjectName("label")
        self.name_line_account = QtWidgets.QLineEdit(Account_Form)
        self.name_line_account.setGeometry(QtCore.QRect(60, 150, 491, 61))
        self.name_line_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.name_line_account.setObjectName("name_line_account")
        self.age_line_account = QtWidgets.QLineEdit(Account_Form)
        self.age_line_account.setGeometry(QtCore.QRect(60, 230, 491, 61))
        self.age_line_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.age_line_account.setObjectName("age_line_account")
        self.emai_line_account = QtWidgets.QLineEdit(Account_Form)
        self.emai_line_account.setGeometry(QtCore.QRect(60, 310, 491, 61))
        self.emai_line_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.emai_line_account.setObjectName("emai_line_account")
        self.username_reg_account = QtWidgets.QLineEdit(Account_Form)
        self.username_reg_account.setGeometry(QtCore.QRect(60, 390, 491, 61))
        self.username_reg_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.username_reg_account.setObjectName("username_reg_account")
        self.passwd_reg_account = QtWidgets.QLineEdit(Account_Form)
        self.passwd_reg_account.setGeometry(QtCore.QRect(60, 470, 491, 61))
        self.passwd_reg_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.passwd_reg_account.setMaxLength(10)
        self.passwd_reg_account.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_reg_account.setObjectName("passwd_reg_account")
        self.checkword_account = QtWidgets.QLineEdit(Account_Form)
        self.checkword_account.setGeometry(QtCore.QRect(60, 550, 491, 61))
        self.checkword_account.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.checkword_account.setObjectName("checkword_account")
        self.edit_btn = QtWidgets.QPushButton(Account_Form)
        self.edit_btn.setGeometry(QtCore.QRect(140, 650, 341, 61))
        self.edit_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"   font: 63 16pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.edit_btn.setObjectName("edit_btn")
        self.delete_btn = QtWidgets.QPushButton(Account_Form)
        self.delete_btn.setGeometry(QtCore.QRect(140, 730, 341, 61))
        self.delete_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"   font: 63 16pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.delete_btn.setObjectName("delete_btn")
        self.label_2 = QtWidgets.QLabel(Account_Form)
        self.label_2.setGeometry(QtCore.QRect(440, 40, 141, 61))
        self.label_2.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Account_Form)
        QtCore.QMetaObject.connectSlotsByName(Account_Form)

    def retranslateUi(self, Account_Form):
        _translate = QtCore.QCoreApplication.translate
        Account_Form.setWindowTitle(_translate("Account_Form", "Личный кабинет пользователя"))
        self.name_line_account.setPlaceholderText(_translate("Account_Form", "Введите имя"))
        self.age_line_account.setPlaceholderText(_translate("Account_Form", "Введите возраст"))
        self.emai_line_account.setPlaceholderText(_translate("Account_Form", "Введите адрес электронной почты"))
        self.username_reg_account.setPlaceholderText(_translate("Account_Form", "Введите выбранный ник"))
        self.passwd_reg_account.setPlaceholderText(_translate("Account_Form", "Введите пароль (макс. 10 симв)"))
        self.checkword_account.setPlaceholderText(_translate("Account_Form", "Задайте проверочное слово при смене пароля"))
        self.edit_btn.setText(_translate("Account_Form", "Редактировать "))
        self.delete_btn.setText(_translate("Account_Form", "Удалить учетную запись"))

class Ui_Registration_Form(object):
    def setupUi(self, Registration_Form):
        Registration_Form.setObjectName("Registration_Form")
        Registration_Form.resize(615, 841)
        Registration_Form.setStyleSheet("background-color: rgb(129, 61, 156);")
        self.label = QtWidgets.QLabel(Registration_Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 531, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label.setObjectName("label")
        self.name_line_edit = QtWidgets.QLineEdit(Registration_Form)
        self.name_line_edit.setGeometry(QtCore.QRect(60, 150, 491, 61))
        self.name_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.name_line_edit.setObjectName("name_line_edit")
        self.age_line_edit = QtWidgets.QLineEdit(Registration_Form)
        self.age_line_edit.setGeometry(QtCore.QRect(60, 230, 491, 61))
        self.age_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.age_line_edit.setObjectName("age_line_edit")
        self.emai_line_edit = QtWidgets.QLineEdit(Registration_Form)
        self.emai_line_edit.setGeometry(QtCore.QRect(60, 310, 491, 61))
        self.emai_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.emai_line_edit.setObjectName("emai_line_edit")
        self.username_reg_line = QtWidgets.QLineEdit(Registration_Form)
        self.username_reg_line.setGeometry(QtCore.QRect(60, 390, 491, 61))
        self.username_reg_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.username_reg_line.setObjectName("username_reg_line")
        self.passwd_reg_line = QtWidgets.QLineEdit(Registration_Form)
        self.passwd_reg_line.setGeometry(QtCore.QRect(60, 470, 491, 61))
        self.passwd_reg_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.passwd_reg_line.setMaxLength(10)
        self.passwd_reg_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_reg_line.setObjectName("passwd_reg_line")
        self.checkword_line = QtWidgets.QLineEdit(Registration_Form)
        self.checkword_line.setGeometry(QtCore.QRect(60, 550, 491, 61))
        self.checkword_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.checkword_line.setObjectName("checkword_line")
        self.registration_btn = QtWidgets.QPushButton(Registration_Form)
        self.registration_btn.setGeometry(QtCore.QRect(140, 670, 341, 61))
        self.registration_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"   font: 63 16pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.registration_btn.setObjectName("registration_btn")

        self.retranslateUi(Registration_Form)
        QtCore.QMetaObject.connectSlotsByName(Registration_Form)

    def retranslateUi(self, Registration_Form):
        _translate = QtCore.QCoreApplication.translate
        Registration_Form.setWindowTitle(_translate("Registration_Form", "Окно регистрации новых пользователей"))
        self.label.setText(_translate("Registration_Form", "Регистрация нового пользователя"))
        self.name_line_edit.setPlaceholderText(_translate("Registration_Form", "Введите имя"))
        self.age_line_edit.setPlaceholderText(_translate("Registration_Form", "Введите возраст"))
        self.emai_line_edit.setPlaceholderText(_translate("Registration_Form", "Введите адрес электронной почты"))
        self.username_reg_line.setPlaceholderText(_translate("Registration_Form", "Введите выбранный ник"))
        self.passwd_reg_line.setPlaceholderText(_translate("Registration_Form", "Введите пароль (макс. 10 симв)"))
        self.checkword_line.setPlaceholderText(_translate("Registration_Form", "Задайте проверочное слово при смене пароля"))
        self.registration_btn.setText(_translate("Registration_Form", "Зарегистрироваться"))


class Ui_Reset_Passwd_Form(object):
    def setupUi(self, Reset_Passwd_Form):
        Reset_Passwd_Form.setObjectName("Reset_Passwd_Form")
        Reset_Passwd_Form.resize(611, 666)
        Reset_Passwd_Form.setStyleSheet("background-color: rgb(129, 61, 156);")
        self.label = QtWidgets.QLabel(Reset_Passwd_Form)
        self.label.setGeometry(QtCore.QRect(100, 50, 431, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label.setObjectName("label")
        self.username_resetpasswd_line = QtWidgets.QLineEdit(Reset_Passwd_Form)
        self.username_resetpasswd_line.setGeometry(QtCore.QRect(60, 170, 491, 61))
        self.username_resetpasswd_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.username_resetpasswd_line.setObjectName("username_resetpasswd_line")
        self.new_passwd_line = QtWidgets.QLineEdit(Reset_Passwd_Form)
        self.new_passwd_line.setGeometry(QtCore.QRect(70, 360, 491, 61))
        self.new_passwd_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.new_passwd_line.setMaxLength(10)
        self.new_passwd_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_passwd_line.setObjectName("new_passwd_line")
        self.checkword_resetpasswd_line = QtWidgets.QLineEdit(Reset_Passwd_Form)
        self.checkword_resetpasswd_line.setGeometry(QtCore.QRect(60, 260, 491, 61))
        self.checkword_resetpasswd_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.checkword_resetpasswd_line.setObjectName("checkword_resetpasswd_line")
        self.reset_passwd_btn = QtWidgets.QPushButton(Reset_Passwd_Form)
        self.reset_passwd_btn.setGeometry(QtCore.QRect(140, 490, 341, 61))
        self.reset_passwd_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 170, 224);\n"
"   font: 63 16pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:gray;\n"
"    font: 63 16pt \"URW Gothic\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.reset_passwd_btn.setObjectName("reset_passwd_btn")

        self.retranslateUi(Reset_Passwd_Form)
        QtCore.QMetaObject.connectSlotsByName(Reset_Passwd_Form)

    def retranslateUi(self, Reset_Passwd_Form):
        _translate = QtCore.QCoreApplication.translate
        Reset_Passwd_Form.setWindowTitle(_translate("Reset_Passwd_Form", "Окно восстановления доступа"))
        self.label.setText(_translate("Reset_Passwd_Form", "Восстановление доступа"))
        self.username_resetpasswd_line.setPlaceholderText(_translate("Reset_Passwd_Form", "Введите ваш ник"))
        self.new_passwd_line.setPlaceholderText(_translate("Reset_Passwd_Form", "Введите новый пароль (макс. 10 симв)"))
        self.checkword_resetpasswd_line.setPlaceholderText(_translate("Reset_Passwd_Form", "Задайте проверочное слово при смене пароля"))
        self.reset_passwd_btn.setText(_translate("Reset_Passwd_Form", "Восстановить доступ"))

class Ui_Kind_Form(object):
    def setupUi(self, Kind_Form):
        Kind_Form.setObjectName("Kind_Form")
        Kind_Form.resize(1280, 825)
        Kind_Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));")
        self.cartoons_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.cartoons_btn_kid.setGeometry(QtCore.QRect(110, 210, 311, 121))
        self.cartoons_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.cartoons_btn_kid.setObjectName("cartoons_btn_kid")
        self.comedy_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.comedy_btn_kid.setGeometry(QtCore.QRect(470, 40, 311, 121))
        self.comedy_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.comedy_btn_kid.setObjectName("comedy_btn_kid")
        self.history_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.history_btn_kid.setGeometry(QtCore.QRect(870, 450, 311, 121))
        self.history_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.history_btn_kid.setObjectName("history_btn_kid")
        self.fantasy_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.fantasy_btn_kid.setGeometry(QtCore.QRect(870, 200, 311, 121))
        self.fantasy_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.fantasy_btn_kid.setObjectName("fantasy_btn_kid")
        self.serials_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.serials_btn_kid.setGeometry(QtCore.QRect(470, 610, 311, 121))
        self.serials_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.serials_btn_kid.setObjectName("serials_btn_kid")
        self.new_btn_kid = QtWidgets.QPushButton(Kind_Form)
        self.new_btn_kid.setGeometry(QtCore.QRect(100, 460, 311, 121))
        self.new_btn_kid.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.301508         rgba(58, 247, 131, 255), stop:0.929648 rgba(10, 30, 234, 255));\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.new_btn_kid.setObjectName("new_btn_kid")

        self.retranslateUi(Kind_Form)
        QtCore.QMetaObject.connectSlotsByName(Kind_Form)

    def retranslateUi(self, Kind_Form):
        _translate = QtCore.QCoreApplication.translate
        Kind_Form.setWindowTitle(_translate("Kind_Form", "Режим \"Детская комната\""))
        self.cartoons_btn_kid.setText(_translate("Kind_Form", "Мультфильмы"))
        self.comedy_btn_kid.setText(_translate("Kind_Form", "Комедии"))
        self.history_btn_kid.setText(_translate("Kind_Form", "Исторические"))
        self.fantasy_btn_kid.setText(_translate("Kind_Form", "Фантастика"))
        self.serials_btn_kid.setText(_translate("Kind_Form", "Сериалы"))
        self.new_btn_kid.setText(_translate("Kind_Form", "Новинки проката"))


class Ui_Adult_Form(object):
    def setupUi(self, Adult_Form):
        Adult_Form.setObjectName("Adult_Form")
        Adult_Form.resize(1280, 825)
        Adult_Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));")
        self.comedy_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.comedy_btn_adult.setGeometry(QtCore.QRect(70, 60, 311, 121))
        self.comedy_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.comedy_btn_adult.setObjectName("comedy_btn_adult")
        self.history_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.history_btn_adult.setGeometry(QtCore.QRect(70, 410, 311, 121))
        self.history_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.history_btn_adult.setObjectName("history_btn_adult")
        self.fantasy_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.fantasy_btn_adult.setGeometry(QtCore.QRect(70, 240, 311, 121))
        self.fantasy_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.fantasy_btn_adult.setObjectName("fantasy_btn_adult")
        self.horror_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.horror_btn_adult.setGeometry(QtCore.QRect(920, 60, 311, 121))
        self.horror_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.horror_btn_adult.setObjectName("horror_btn_adult")
        self.new_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.new_btn_adult.setGeometry(QtCore.QRect(520, 60, 311, 121))
        self.new_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.new_btn_adult.setObjectName("new_btn_adult")
        self.serials_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.serials_btn_adult.setGeometry(QtCore.QRect(70, 590, 311, 121))
        self.serials_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.serials_btn_adult.setObjectName("serials_btn_adult")
        self.dram_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.dram_btn_adult.setGeometry(QtCore.QRect(920, 230, 311, 121))
        self.dram_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.dram_btn_adult.setObjectName("dram_btn_adult")
        self.action_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.action_btn_adult.setGeometry(QtCore.QRect(920, 400, 311, 121))
        self.action_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.action_btn_adult.setObjectName("action_btn_adult")
        self.detective_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.detective_btn_adult.setGeometry(QtCore.QRect(920, 590, 311, 121))
        self.detective_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.detective_btn_adult.setObjectName("detective_btn_adult")
        self.animation_btn_adult = QtWidgets.QPushButton(Adult_Form)
        self.animation_btn_adult.setGeometry(QtCore.QRect(510, 590, 311, 121))
        self.animation_btn_adult.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(112, 19, 190);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: white;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: lightGray;\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.animation_btn_adult.setObjectName("animation_btn_adult")

        self.retranslateUi(Adult_Form)
        QtCore.QMetaObject.connectSlotsByName(Adult_Form)

    def retranslateUi(self, Adult_Form):
        _translate = QtCore.QCoreApplication.translate
        Adult_Form.setWindowTitle(_translate("Adult_Form", "Обычный режим"))
        self.comedy_btn_adult.setText(_translate("Adult_Form", "Комедии"))
        self.history_btn_adult.setText(_translate("Adult_Form", "Исторические"))
        self.fantasy_btn_adult.setText(_translate("Adult_Form", "Фантастика"))
        self.horror_btn_adult.setText(_translate("Adult_Form", "Ужасы"))
        self.new_btn_adult.setText(_translate("Adult_Form", "Новинки проката"))
        self.serials_btn_adult.setText(_translate("Adult_Form", "Сериалы"))
        self.dram_btn_adult.setText(_translate("Adult_Form", "Драмы"))
        self.action_btn_adult.setText(_translate("Adult_Form", "Боевики"))
        self.detective_btn_adult.setText(_translate("Adult_Form", "Детективы"))
        self.animation_btn_adult.setText(_translate("Adult_Form", "Анимация"))


class Ui_Admin_Form(object):
    def setupUi(self, Admin_Form):
        Admin_Form.setObjectName("Admin_Form")
        Admin_Form.resize(1280, 825)
        Admin_Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));")
        self.comedy_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.comedy_btn_admin.setGeometry(QtCore.QRect(70, 60, 311, 121))
        self.comedy_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.comedy_btn_admin.setObjectName("comedy_btn_admin")
        self.history_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.history_btn_admin.setGeometry(QtCore.QRect(70, 410, 311, 121))
        self.history_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.history_btn_admin.setObjectName("history_btn_admin")
        self.fantasy_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.fantasy_btn_admin.setGeometry(QtCore.QRect(70, 240, 311, 121))
        self.fantasy_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.fantasy_btn_admin.setObjectName("fantasy_btn_admin")
        self.horror_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.horror_btn_admin.setGeometry(QtCore.QRect(500, 590, 311, 121))
        self.horror_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.horror_btn_admin.setObjectName("horror_btn_admin")
        self.new_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.new_btn_admin.setGeometry(QtCore.QRect(510, 60, 311, 121))
        self.new_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.new_btn_admin.setObjectName("new_btn_admin")
        self.serials_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.serials_btn_admin.setGeometry(QtCore.QRect(70, 590, 311, 121))
        self.serials_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.serials_btn_admin.setObjectName("serials_btn_admin")
        self.animation_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.animation_btn_admin.setGeometry(QtCore.QRect(920, 60, 311, 121))
        self.animation_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.animation_btn_admin.setObjectName("animation_btn_admin")
        self.dram_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.dram_btn_admin.setGeometry(QtCore.QRect(920, 230, 311, 121))
        self.dram_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.dram_btn_admin.setObjectName("dram_btn_admin")
        self.action_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.action_btn_admin.setGeometry(QtCore.QRect(920, 400, 311, 121))
        self.action_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.action_btn_admin.setObjectName("action_btn_admin")
        self.detective_btn_admin = QtWidgets.QPushButton(Admin_Form)
        self.detective_btn_admin.setGeometry(QtCore.QRect(920, 590, 311, 121))
        self.detective_btn_admin.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(192, 191, 188);\n"
"    font: 63 20pt \"URW Gothic\" bold;\n"
"    color: dark;\n"
"    border: 2px solid gray;\n"
"    border-radius: 40\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 63 20pt \"URW Gothic\" bold dark gray;\n"
"    border: 2px solid  light gray;\n"
"    border-radius: 40\n"
"}\n"
"")
        self.detective_btn_admin.setObjectName("detective_btn_admin")

        self.retranslateUi(Admin_Form)
        QtCore.QMetaObject.connectSlotsByName(Admin_Form)

    def retranslateUi(self, Admin_Form):
        _translate = QtCore.QCoreApplication.translate
        Admin_Form.setWindowTitle(_translate("Admin_Form", "Режим администратора"))
        self.comedy_btn_admin.setText(_translate("Admin_Form", "Комедии"))
        self.history_btn_admin.setText(_translate("Admin_Form", "Исторические"))
        self.fantasy_btn_admin.setText(_translate("Admin_Form", "Фантастика"))
        self.horror_btn_admin.setText(_translate("Admin_Form", "Ужасы"))
        self.new_btn_admin.setText(_translate("Admin_Form", "Новинки проката"))
        self.serials_btn_admin.setText(_translate("Admin_Form", "Сериалы"))
        self.animation_btn_admin.setText(_translate("Admin_Form", "Анимация"))
        self.dram_btn_admin.setText(_translate("Admin_Form", "Драмы"))
        self.action_btn_admin.setText(_translate("Admin_Form", "Боевики"))
        self.detective_btn_admin.setText(_translate("Admin_Form", "Детективы"))


