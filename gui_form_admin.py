from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_detective_admin(object):
    def setupUi(self, Form_detective_admin):
        Form_detective_admin.setObjectName("Form_detective_admin")
        Form_detective_admin.resize(1448, 904)
        Form_detective_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_detective_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_detective_admin = QtWidgets.QLineEdit(Form_detective_admin)
        self.search_line_detective_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_detective_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_detective_admin.setObjectName("search_line_detective_admin")
        self.search_btn_detective_admin = QtWidgets.QPushButton(Form_detective_admin)
        self.search_btn_detective_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_detective_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_detective_admin.setObjectName("search_btn_detective_admin")
        self.table_detective_admin = QtWidgets.QTableWidget(Form_detective_admin)
        self.table_detective_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_detective_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_detective_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_detective_admin.setObjectName("table_detective_admin")
        self.table_detective_admin.setColumnCount(5)
        self.table_detective_admin.setRowCount(0)
        self.table_detective_admin.setColumnWidth(0,400)
        self.table_detective_admin.setColumnWidth(1,300)
        self.table_detective_admin.setColumnWidth(2,200)
        self.table_detective_admin.setColumnWidth(3,200)
        self.table_detective_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_detective_admin = QtWidgets.QLabel(Form_detective_admin)
        self.lable_info_detective_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_detective_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_detective_admin.setText("")
        self.lable_info_detective_admin.setObjectName("lable_info_detective_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_detective_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_detective_btn = QtWidgets.QPushButton(Form_detective_admin)
        self.insert_detective_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_detective_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_detective_btn.setObjectName("insert_detective_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_detective_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_detective_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_detective_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_detective_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_detective_admin.addAction(self.edit_detective_action)
        self.table_detective_admin.addAction(self.delete_detective_action)
        self.table_detective_admin.addAction(self.info_detective_action)
        self.table_detective_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_detective_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_detective_admin)

    def retranslateUi(self, Form_detective_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_detective_admin.setWindowTitle(_translate("Form_detective_admin", "Раздел \"Детективы\""))
        self.search_line_detective_admin.setPlaceholderText(_translate("Form_detective_admin", "Введите название фильма"))
        self.search_btn_detective_admin.setText(_translate("Form_detective_admin", "Поиск"))
        item = self.table_detective_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_detective_admin", "Название фильма"))
        item = self.table_detective_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_detective_admin", "Страна производства"))
        item = self.table_detective_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_detective_admin", "Год выхода"))
        item = self.table_detective_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_detective_admin", "Возрастное ограничение"))
        item = self.table_detective_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_detective_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_detective_admin", "БД Пользователей"))
        self.insert_detective_btn.setText(_translate("Form_detective_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_detective_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_detective_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_detective_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_detective_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_detective_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_detective_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_detective_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_detective_admin", "Ctrl+U"))

class Ui_Form_action_admin(object):
    def setupUi(self, Form_action_admin):
        Form_action_admin.setObjectName("Form_action_admin")
        Form_action_admin.resize(1448, 904)
        Form_action_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_action_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_action_admin = QtWidgets.QLineEdit(Form_action_admin)
        self.search_line_action_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_action_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_action_admin.setObjectName("search_line_action_admin")
        self.search_btn_action_admin = QtWidgets.QPushButton(Form_action_admin)
        self.search_btn_action_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_action_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_action_admin.setObjectName("search_btn_action_admin")
        self.table_action_admin = QtWidgets.QTableWidget(Form_action_admin)
        self.table_action_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_action_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_action_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_action_admin.setObjectName("table_action_admin")
        self.table_action_admin.setColumnCount(5)
        self.table_action_admin.setRowCount(0)
        self.table_action_admin.setColumnWidth(0,400)
        self.table_action_admin.setColumnWidth(1,300)
        self.table_action_admin.setColumnWidth(2,200)
        self.table_action_admin.setColumnWidth(3,200)
        self.table_action_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_action_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_action_admin = QtWidgets.QLabel(Form_action_admin)
        self.lable_info_action_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_action_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_action_admin.setText("")
        self.lable_info_action_admin.setObjectName("lable_info_action_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_action_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_action_btn = QtWidgets.QPushButton(Form_action_admin)
        self.insert_action_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_action_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_action_btn.setObjectName("insert_action_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_action_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_action_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_action_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_action_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_action_admin.addAction(self.edit_detective_action)
        self.table_action_admin.addAction(self.delete_detective_action)
        self.table_action_admin.addAction(self.info_detective_action)
        self.table_action_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_action_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_action_admin)

    def retranslateUi(self, Form_action_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_action_admin.setWindowTitle(_translate("Form_action_admin", "Раздел \"Боевики\""))
        self.search_line_action_admin.setPlaceholderText(_translate("Form_action_admin", "Введите название фильма"))
        self.search_btn_action_admin.setText(_translate("Form_action_admin", "Поиск"))
        item = self.table_action_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_action_admin", "Название фильма"))
        item = self.table_action_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_action_admin", "Страна производства"))
        item = self.table_action_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_action_admin", "Год выхода"))
        item = self.table_action_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_action_admin", "Возрастное ограничение"))
        item = self.table_action_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_action_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_action_admin", "БД Пользователей"))
        self.insert_action_btn.setText(_translate("Form_action_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_action_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_action_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_action_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_action_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_action_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_action_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_action_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_action_admin", "Ctrl+U"))

class Ui_Form_animation_admin(object):
    def setupUi(self, Form_animation_admin):
        Form_animation_admin.setObjectName("Form_animation_admin")
        Form_animation_admin.resize(1448, 904)
        Form_animation_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_animation_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_animation_admin = QtWidgets.QLineEdit(Form_animation_admin)
        self.search_line_animation_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_animation_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_animation_admin.setObjectName("search_line_animation_admin")
        self.search_btn_animation_admin = QtWidgets.QPushButton(Form_animation_admin)
        self.search_btn_animation_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_animation_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_animation_admin.setObjectName("search_btn_animation_admin")
        self.table_animation_admin = QtWidgets.QTableWidget(Form_animation_admin)
        self.table_animation_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_animation_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_animation_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_animation_admin.setObjectName("table_animation_admin")
        self.table_animation_admin.setColumnCount(5)
        self.table_animation_admin.setRowCount(0)
        self.table_animation_admin.setColumnWidth(0,400)
        self.table_animation_admin.setColumnWidth(1,300)
        self.table_animation_admin.setColumnWidth(2,200)
        self.table_animation_admin.setColumnWidth(3,200)
        self.table_animation_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_animation_admin = QtWidgets.QLabel(Form_animation_admin)
        self.lable_info_animation_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_animation_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_animation_admin.setText("")
        self.lable_info_animation_admin.setObjectName("lable_info_animation_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_animation_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_animation_btn = QtWidgets.QPushButton(Form_animation_admin)
        self.insert_animation_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_animation_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_animation_btn.setObjectName("insert_animation_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_animation_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_animation_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_animation_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_animation_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_animation_admin.addAction(self.edit_detective_action)
        self.table_animation_admin.addAction(self.delete_detective_action)
        self.table_animation_admin.addAction(self.info_detective_action)
        self.table_animation_admin.addAction(self.update_detective_action)

        self.retranslateUi(Form_animation_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_animation_admin)

    def retranslateUi(self, Form_animation_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_animation_admin.setWindowTitle(_translate("Form_animation_admin", "Раздел \"Анимационные фильмы\""))
        self.search_line_animation_admin.setPlaceholderText(_translate("Form_animation_admin", "Введите название фильма"))
        self.search_btn_animation_admin.setText(_translate("Form_animation_admin", "Поиск"))
        item = self.table_animation_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_animation_admin", "Название фильма"))
        item = self.table_animation_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_animation_admin", "Страна производства"))
        item = self.table_animation_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_animation_admin", "Год выхода"))
        item = self.table_animation_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_animation_admin", "Возрастное ограничение"))
        item = self.table_animation_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_animation_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_animation_admin", "БД Пользователей"))
        self.insert_animation_btn.setText(_translate("Form_animation_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_animation_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_animation_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_animation_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_animation_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_animation_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_animation_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_animation_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_animation_admin", "Ctrl+U"))


class Ui_Form_comedy_admin(object):
    def setupUi(self, Form_comedy_admin):
        Form_comedy_admin.setObjectName("Form_comedy_admin")
        Form_comedy_admin.resize(1448, 904)
        Form_comedy_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_comedy_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_comedy_admin = QtWidgets.QLineEdit(Form_comedy_admin)
        self.search_line_comedy_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_comedy_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_comedy_admin.setObjectName("search_line_comedy_admin")
        self.search_btn_comedy_admin = QtWidgets.QPushButton(Form_comedy_admin)
        self.search_btn_comedy_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_comedy_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_comedy_admin.setObjectName("search_btn_comedy_admin")
        self.table_comedy_admin = QtWidgets.QTableWidget(Form_comedy_admin)
        self.table_comedy_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_comedy_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_comedy_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_comedy_admin.setObjectName("table_comedy_admin")
        self.table_comedy_admin.setColumnCount(5)
        self.table_comedy_admin.setRowCount(0)
        self.table_comedy_admin.setColumnWidth(0,400)
        self.table_comedy_admin.setColumnWidth(1,300)
        self.table_comedy_admin.setColumnWidth(2,200)
        self.table_comedy_admin.setColumnWidth(3,200)
        self.table_comedy_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_comedy_admin = QtWidgets.QLabel(Form_comedy_admin)
        self.lable_info_comedy_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_comedy_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_comedy_admin.setText("")
        self.lable_info_comedy_admin.setObjectName("lable_info_comedy_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_comedy_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_comedy_btn = QtWidgets.QPushButton(Form_comedy_admin)
        self.insert_comedy_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_comedy_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_comedy_btn.setObjectName("insert_comedy_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_comedy_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_comedy_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_comedy_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_comedy_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_comedy_admin.addAction(self.edit_detective_action)
        self.table_comedy_admin.addAction(self.delete_detective_action)
        self.table_comedy_admin.addAction(self.info_detective_action)
        self.table_comedy_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_comedy_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_comedy_admin)

    def retranslateUi(self, Form_comedy_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_comedy_admin.setWindowTitle(_translate("Form_comedy_admin", "Раздел \"Комедии\""))
        self.search_line_comedy_admin.setPlaceholderText(_translate("Form_comedy_admin", "Введите название фильма"))
        self.search_btn_comedy_admin.setText(_translate("Form_comedy_admin", "Поиск"))
        item = self.table_comedy_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_comedy_admin", "Название фильма"))
        item = self.table_comedy_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_comedy_admin", "Страна производства"))
        item = self.table_comedy_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_comedy_admin", "Год выхода"))
        item = self.table_comedy_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_comedy_admin", "Возрастное ограничение"))
        item = self.table_comedy_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_comedy_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_comedy_admin", "БД Пользователей"))
        self.insert_comedy_btn.setText(_translate("Form_comedy_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_comedy_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_comedy_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_comedy_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_comedy_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_comedy_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_comedy_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_comedy_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_comedy_admin", "Ctrl+U"))

class Ui_Form_dram_admin(object):
    def setupUi(self, Form_dram_admin):
        Form_dram_admin.setObjectName("Form_dram_admin")
        Form_dram_admin.resize(1448, 904)
        Form_dram_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_dram_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_drama_admin = QtWidgets.QLineEdit(Form_dram_admin)
        self.search_line_drama_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_drama_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_drama_admin.setObjectName("search_line_drama_admin")
        self.search_btn_drama_admin = QtWidgets.QPushButton(Form_dram_admin)
        self.search_btn_drama_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_drama_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_drama_admin.setObjectName("search_btn_drama_admin")
        self.table_drama_admin = QtWidgets.QTableWidget(Form_dram_admin)
        self.table_drama_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_drama_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_drama_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_drama_admin.setObjectName("table_drama_admin")
        self.table_drama_admin.setColumnCount(5)
        self.table_drama_admin.setRowCount(0)
        self.table_drama_admin.setColumnWidth(0,400)
        self.table_drama_admin.setColumnWidth(1,300)
        self.table_drama_admin.setColumnWidth(2,200)
        self.table_drama_admin.setColumnWidth(3,200)
        self.table_drama_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_drama_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_drama_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_drama_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_drama_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_drama_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_drama_admin = QtWidgets.QLabel(Form_dram_admin)
        self.lable_info_drama_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_drama_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_drama_admin.setText("")
        self.lable_info_drama_admin.setObjectName("lable_info_drama_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_dram_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_drama_btn = QtWidgets.QPushButton(Form_dram_admin)
        self.insert_drama_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_drama_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_drama_btn.setObjectName("insert_drama_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_dram_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_dram_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_dram_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_dram_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_drama_admin.addAction(self.edit_detective_action)
        self.table_drama_admin.addAction(self.delete_detective_action)
        self.table_drama_admin.addAction(self.info_detective_action)
        self.table_drama_admin.addAction(self.update_detective_action)

        self.retranslateUi(Form_dram_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_dram_admin)

    def retranslateUi(self, Form_dram_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_dram_admin.setWindowTitle(_translate("Form_dram_admin", "Раздел \"Драмы\""))
        self.search_line_drama_admin.setPlaceholderText(_translate("Form_dram_admin", "Введите название фильма"))
        self.search_btn_drama_admin.setText(_translate("Form_dram_admin", "Поиск"))
        item = self.table_drama_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_dram_admin", "Название фильма"))
        item = self.table_drama_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_dram_admin", "Страна производства"))
        item = self.table_drama_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_dram_admin", "Год выхода"))
        item = self.table_drama_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_dram_admin", "Возрастное органичение"))
        item = self.table_drama_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_dram_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_dram_admin", "БД Пользователей"))
        self.insert_drama_btn.setText(_translate("Form_dram_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_dram_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_dram_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_dram_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_dram_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_dram_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_dram_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_dram_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_dram_admin", "Ctrl+U"))


class Ui_Form_fantasy_admin(object):
    def setupUi(self, Form_fantasy_admin):
        Form_fantasy_admin.setObjectName("Form_fantasy_admin")
        Form_fantasy_admin.resize(1448, 904)
        Form_fantasy_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_fantasy_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_fantasy_admin = QtWidgets.QLineEdit(Form_fantasy_admin)
        self.search_line_fantasy_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_fantasy_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_fantasy_admin.setObjectName("search_line_fantasy_admin")
        self.search_btn_fantasy_admin = QtWidgets.QPushButton(Form_fantasy_admin)
        self.search_btn_fantasy_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_fantasy_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_fantasy_admin.setObjectName("search_btn_fantasy_admin")
        self.table_fantasy_admin = QtWidgets.QTableWidget(Form_fantasy_admin)
        self.table_fantasy_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_fantasy_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_fantasy_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_fantasy_admin.setObjectName("table_fantasy_admin")
        self.table_fantasy_admin.setColumnCount(5)
        self.table_fantasy_admin.setRowCount(0)
        self.table_fantasy_admin.setColumnWidth(0,400)
        self.table_fantasy_admin.setColumnWidth(1,300)
        self.table_fantasy_admin.setColumnWidth(2,200)
        self.table_fantasy_admin.setColumnWidth(3,200)
        self.table_fantasy_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_fantasy_admin = QtWidgets.QLabel(Form_fantasy_admin)
        self.lable_info_fantasy_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_fantasy_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_fantasy_admin.setText("")
        self.lable_info_fantasy_admin.setObjectName("lable_info_fantasy_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_fantasy_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_fantasy_btn = QtWidgets.QPushButton(Form_fantasy_admin)
        self.insert_fantasy_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_fantasy_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_fantasy_btn.setObjectName("insert_fantasy_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_fantasy_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_fantasy_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_fantasy_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_fantasy_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_fantasy_admin.addAction(self.edit_detective_action)
        self.table_fantasy_admin.addAction(self.delete_detective_action)
        self.table_fantasy_admin.addAction(self.info_detective_action)
        self.table_fantasy_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_fantasy_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_fantasy_admin)

    def retranslateUi(self, Form_fantasy_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_fantasy_admin.setWindowTitle(_translate("Form_fantasy_admin", "Раздел \"Фантастические фильмы\""))
        self.search_line_fantasy_admin.setPlaceholderText(_translate("Form_fantasy_admin", "Введите название фильма"))
        self.search_btn_fantasy_admin.setText(_translate("Form_fantasy_admin", "Поиск"))
        item = self.table_fantasy_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_fantasy_admin", "Название фильма"))
        item = self.table_fantasy_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_fantasy_admin", "Страна производства"))
        item = self.table_fantasy_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_fantasy_admin", "Год выхода"))
        item = self.table_fantasy_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_fantasy_admin", "Возрастное ограничение"))
        item = self.table_fantasy_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_fantasy_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_fantasy_admin", "БД Пользователей"))
        self.insert_fantasy_btn.setText(_translate("Form_fantasy_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_fantasy_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_fantasy_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_fantasy_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_fantasy_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_fantasy_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_fantasy_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_fantasy_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_fantasy_admin", "Ctrl+U"))

class Ui_Form_history_admin(object):
    def setupUi(self, Form_history_admin):
        Form_history_admin.setObjectName("Form_history_admin")
        Form_history_admin.resize(1448, 904)
        Form_history_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_history_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_history_admin = QtWidgets.QLineEdit(Form_history_admin)
        self.search_line_history_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_history_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_history_admin.setObjectName("search_line_history_admin")
        self.search_btn_history_admin = QtWidgets.QPushButton(Form_history_admin)
        self.search_btn_history_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_history_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_history_admin.setObjectName("search_btn_history_admin")
        self.table_history_admin = QtWidgets.QTableWidget(Form_history_admin)
        self.table_history_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_history_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_history_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_history_admin.setObjectName("table_history_admin")
        self.table_history_admin.setColumnCount(5)
        self.table_history_admin.setRowCount(0)
        self.table_history_admin.setColumnWidth(0,400)
        self.table_history_admin.setColumnWidth(1,300)
        self.table_history_admin.setColumnWidth(2,200)
        self.table_history_admin.setColumnWidth(3,200)
        self.table_history_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_history_admin = QtWidgets.QLabel(Form_history_admin)
        self.lable_info_history_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_history_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_history_admin.setText("")
        self.lable_info_history_admin.setObjectName("lable_info_history_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_history_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_history_btn = QtWidgets.QPushButton(Form_history_admin)
        self.insert_history_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_history_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_history_btn.setObjectName("insert_history_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_history_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_history_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_history_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_history_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_history_admin.addAction(self.edit_detective_action)
        self.table_history_admin.addAction(self.delete_detective_action)
        self.table_history_admin.addAction(self.info_detective_action)
        self.table_history_admin.addAction(self.update_detective_action)

        self.retranslateUi(Form_history_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_history_admin)

    def retranslateUi(self, Form_history_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_history_admin.setWindowTitle(_translate("Form_history_admin", "Раздел \"Итсорические фильмы и Биографии\""))
        self.search_line_history_admin.setPlaceholderText(_translate("Form_history_admin", "Введите название фильма"))
        self.search_btn_history_admin.setText(_translate("Form_history_admin", "Поиск"))
        item = self.table_history_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_history_admin", "Название фильма"))
        item = self.table_history_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_history_admin", "Страна производства"))
        item = self.table_history_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_history_admin", "Год выхода"))
        item = self.table_history_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_history_admin", "Возрастное ограничение"))
        item = self.table_history_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_history_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_history_admin", "БД Пользователей"))
        self.insert_history_btn.setText(_translate("Form_history_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_history_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_history_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_history_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_history_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_history_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_history_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_history_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_history_admin", "Ctrl+U"))

class Ui_Form_horror_admin(object):
    def setupUi(self, Form_horror_admin):
        Form_horror_admin.setObjectName("Form_horror_admin")
        Form_horror_admin.resize(1448, 904)
        Form_horror_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_horror_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_horror_admin = QtWidgets.QLineEdit(Form_horror_admin)
        self.search_line_horror_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_horror_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_horror_admin.setObjectName("search_line_horror_admin")
        self.search_btn_horror_admin = QtWidgets.QPushButton(Form_horror_admin)
        self.search_btn_horror_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_horror_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_horror_admin.setObjectName("search_btn_horror_admin")
        self.table_horror_admin = QtWidgets.QTableWidget(Form_horror_admin)
        self.table_horror_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_horror_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_horror_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_horror_admin.setObjectName("table_horror_admin")
        self.table_horror_admin.setColumnCount(5)
        self.table_horror_admin.setRowCount(0)
        self.table_horror_admin.setColumnWidth(0,400)
        self.table_horror_admin.setColumnWidth(1,300)
        self.table_horror_admin.setColumnWidth(2,200)
        self.table_horror_admin.setColumnWidth(3,200)
        self.table_horror_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_horror_admin = QtWidgets.QLabel(Form_horror_admin)
        self.lable_info_horror_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_horror_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_horror_admin.setText("")
        self.lable_info_horror_admin.setObjectName("lable_info_horror_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_horror_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_horror_btn = QtWidgets.QPushButton(Form_horror_admin)
        self.insert_horror_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_horror_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_horror_btn.setObjectName("insert_horror_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_horror_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_horror_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_horror_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_horror_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_horror_admin.addAction(self.edit_detective_action)
        self.table_horror_admin.addAction(self.delete_detective_action)
        self.table_horror_admin.addAction(self.info_detective_action)
        self.table_horror_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_horror_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_horror_admin)

    def retranslateUi(self, Form_horror_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_horror_admin.setWindowTitle(_translate("Form_horror_admin", "Раздел \"Фильмы ужасов\""))
        self.search_line_horror_admin.setPlaceholderText(_translate("Form_horror_admin", "Введите название фильма"))
        self.search_btn_horror_admin.setText(_translate("Form_horror_admin", "Поиск"))
        item = self.table_horror_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_horror_admin", "Название фильма"))
        item = self.table_horror_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_horror_admin", "Страна производства"))
        item = self.table_horror_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_horror_admin", "Год выхода"))
        item = self.table_horror_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_horror_admin", "Возрастное ограничение"))
        item = self.table_horror_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_horror_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_horror_admin", "БД Пользователей"))
        self.insert_horror_btn.setText(_translate("Form_horror_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_horror_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_horror_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_horror_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_horror_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_horror_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_horror_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_horror_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_horror_admin", "Ctrl+U"))

class Ui_Form_new_admin(object):
    def setupUi(self, Form_new_admin):
        Form_new_admin.setObjectName("Form_new_admin")
        Form_new_admin.resize(1448, 904)
        Form_new_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_new_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_new_admin = QtWidgets.QLineEdit(Form_new_admin)
        self.search_line_new_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_new_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_new_admin.setObjectName("search_line_new_admin")
        self.search_btn_new_admin = QtWidgets.QPushButton(Form_new_admin)
        self.search_btn_new_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_new_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_new_admin.setObjectName("search_btn_new_admin")
        self.table_new_admin = QtWidgets.QTableWidget(Form_new_admin)
        self.table_new_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_new_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_new_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_new_admin.setObjectName("table_new_admin")
        self.table_new_admin.setColumnCount(6)
        self.table_new_admin.setRowCount(0)
        self.table_new_admin.setColumnWidth(0,400)
        self.table_new_admin.setColumnWidth(1,300)
        self.table_new_admin.setColumnWidth(2,200)
        self.table_new_admin.setColumnWidth(3,200)
        self.table_new_admin.setColumnWidth(4,190)
        self.table_new_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_admin.setHorizontalHeaderItem(5, item)
        self.lable_info_new_admin = QtWidgets.QLabel(Form_new_admin)
        self.lable_info_new_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_new_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_new_admin.setText("")
        self.lable_info_new_admin.setObjectName("lable_info_new_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_new_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_new_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_new_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_new_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_new_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_new_admin.addAction(self.edit_detective_action)
        self.table_new_admin.addAction(self.delete_detective_action)
        self.table_new_admin.addAction(self.info_detective_action)
        self.table_new_admin.addAction(self.update_detective_action)


        self.retranslateUi(Form_new_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_new_admin)

    def retranslateUi(self, Form_new_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_new_admin.setWindowTitle(_translate("Form_new_admin", "Раздел \"Новинки\""))
        self.search_line_new_admin.setPlaceholderText(_translate("Form_new_admin", "Введите название фильма"))
        self.search_btn_new_admin.setText(_translate("Form_new_admin", "Поиск"))
        item = self.table_new_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_new_admin", "Название фильма"))
        item = self.table_new_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_new_admin", "Жанр"))
        item = self.table_new_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_new_admin", "Страна производства"))
        item = self.table_new_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_new_admin", "Год выхода"))
        item = self.table_new_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_new_admin", "Возрастное ограничение"))
        item = self.table_new_admin.horizontalHeaderItem(5)
        item.setText(_translate("Form_new_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_new_admin", "БД Пользователей"))
        self.edit_detective_action.setText(_translate("Form_new_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_new_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_new_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_new_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_new_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_new_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_new_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_new_admin", "Ctrl+U"))

class Ui_Form_serial_admin(object):
    def setupUi(self, Form_serial_admin):
        Form_serial_admin.setObjectName("Form_serial_admin")
        Form_serial_admin.resize(1448, 904)
        Form_serial_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_serial_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_serial_admin = QtWidgets.QLineEdit(Form_serial_admin)
        self.search_line_serial_admin.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_serial_admin.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_serial_admin.setObjectName("search_line_serial_admin")
        self.search_btn_serial_admin = QtWidgets.QPushButton(Form_serial_admin)
        self.search_btn_serial_admin.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_serial_admin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_serial_admin.setObjectName("search_btn_serial_admin")
        self.table_serial_admin = QtWidgets.QTableWidget(Form_serial_admin)
        self.table_serial_admin.setGeometry(QtCore.QRect(30, 100, 1301, 541))
        self.table_serial_admin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_serial_admin.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_serial_admin.setObjectName("table_serial_admin")
        self.table_serial_admin.setColumnCount(5)
        self.table_serial_admin.setRowCount(0)
        self.table_serial_admin.setColumnWidth(0,400)
        self.table_serial_admin.setColumnWidth(1,300)
        self.table_serial_admin.setColumnWidth(2,200)
        self.table_serial_admin.setColumnWidth(3,200)
        self.table_serial_admin.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial_admin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial_admin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial_admin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial_admin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial_admin.setHorizontalHeaderItem(4, item)
        self.lable_info_serial_admin = QtWidgets.QLabel(Form_serial_admin)
        self.lable_info_serial_admin.setGeometry(QtCore.QRect(30, 660, 1081, 181))
        self.lable_info_serial_admin.setStyleSheet("background-color:  rgb(187, 230, 200);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_serial_admin.setText("")
        self.lable_info_serial_admin.setObjectName("lable_info_serial_admin")
        self.db_users_btn = QtWidgets.QPushButton(Form_serial_admin)
        self.db_users_btn.setGeometry(QtCore.QRect(1090, 30, 171, 51))
        self.db_users_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.db_users_btn.setObjectName("db_users_btn")
        self.insert_serial_btn = QtWidgets.QPushButton(Form_serial_admin)
        self.insert_serial_btn.setGeometry(QtCore.QRect(1160, 760, 171, 51))
        self.insert_serial_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid Gray;\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    text-aling:center\n"
"}")
        self.insert_serial_btn.setObjectName("insert_serial_btn")
        self.edit_detective_action = QtWidgets.QAction(Form_serial_admin)
        self.edit_detective_action.setObjectName("edit_detective_action")
        self.delete_detective_action = QtWidgets.QAction(Form_serial_admin)
        self.delete_detective_action.setObjectName("delete_detective_action")
        self.info_detective_action = QtWidgets.QAction(Form_serial_admin)
        self.info_detective_action.setObjectName("info_detective_action")
        self.update_detective_action = QtWidgets.QAction(Form_serial_admin)
        self.update_detective_action.setObjectName("update_detective_action")
        self.table_serial_admin.addAction(self.edit_detective_action)
        self.table_serial_admin.addAction(self.delete_detective_action)
        self.table_serial_admin.addAction(self.info_detective_action)
        self.table_serial_admin.addAction(self.update_detective_action)

        self.retranslateUi(Form_serial_admin)
        QtCore.QMetaObject.connectSlotsByName(Form_serial_admin)

    def retranslateUi(self, Form_serial_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_serial_admin.setWindowTitle(_translate("Form_serial_admin", "Раздел \"Сериалы\""))
        self.search_line_serial_admin.setPlaceholderText(_translate("Form_serial_admin", "Введите название сериала"))
        self.search_btn_serial_admin.setText(_translate("Form_serial_admin", "Поиск"))
        item = self.table_serial_admin.horizontalHeaderItem(0)
        item.setText(_translate("Form_serial_admin", "Название сериала"))
        item = self.table_serial_admin.horizontalHeaderItem(1)
        item.setText(_translate("Form_serial_admin", "Страна производства"))
        item = self.table_serial_admin.horizontalHeaderItem(2)
        item.setText(_translate("Form_serial_admin", "Год выхода"))
        item = self.table_serial_admin.horizontalHeaderItem(3)
        item.setText(_translate("Form_serial_admin", "Возрастные ограничения"))
        item = self.table_serial_admin.horizontalHeaderItem(4)
        item.setText(_translate("Form_serial_admin", "Оценки"))
        self.db_users_btn.setText(_translate("Form_serial_admin", "БД Пользователей"))
        self.insert_serial_btn.setText(_translate("Form_serial_admin", "Создать запись"))
        self.edit_detective_action.setText(_translate("Form_serial_admin", "Редактировать"))
        self.edit_detective_action.setShortcut(_translate("Form_serial_admin", "Ctrl+E"))
        self.delete_detective_action.setText(_translate("Form_serial_admin", "Удалить"))
        self.delete_detective_action.setShortcut(_translate("Form_serial_admin", "Del"))
        self.info_detective_action.setText(_translate("Form_serial_admin", "Подробнее"))
        self.info_detective_action.setShortcut(_translate("Form_serial_admin", "Ctrl+I"))
        self.update_detective_action.setText(_translate("Form_serial_admin", "Обновить"))
        self.update_detective_action.setShortcut(_translate("Form_serial_admin", "Ctrl+U"))

class Ui_Form_users_database(object):
    def setupUi(self, Form_users_database):
        Form_users_database.setObjectName("Form_users_database")
        Form_users_database.resize(1448, 904)
        Form_users_database.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form_users_database.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));\n"
"")
        self.search_line_users_database = QtWidgets.QLineEdit(Form_users_database)
        self.search_line_users_database.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_users_database.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_users_database.setObjectName("search_line_users_database")
        self.search_btn_users_database = QtWidgets.QPushButton(Form_users_database)
        self.search_btn_users_database.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_users_database.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(154, 153, 150);\n"
"    text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(154, 153, 150);\n"
"    color: rgb(222, 221, 218);\n"
"    font: 63 12pt \"URW Gothic\";\n"
"    border: 2px solid rgb(119, 118, 123);\n"
"    text-aling:center\n"
"}")
        self.search_btn_users_database.setObjectName("search_btn_users_database")
        self.table_users_database = QtWidgets.QTableWidget(Form_users_database)
        self.table_users_database.setGeometry(QtCore.QRect(30, 100, 1301, 711))
        self.table_users_database.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_users_database.setStyleSheet("background-color: rgb(187, 230, 200);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_users_database.setObjectName("table_users_database")
        self.table_users_database.setColumnCount(7)
        self.table_users_database.setRowCount(0)
        self.table_users_database.setColumnWidth(0,100)
        self.table_users_database.setColumnWidth(1,300)
        self.table_users_database.setColumnWidth(2,150)
        self.table_users_database.setColumnWidth(3,300)
        self.table_users_database.setColumnWidth(4,300)
        self.table_users_database.setColumnWidth(5,300)
        self.table_users_database.setColumnWidth(6,300)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users_database.setHorizontalHeaderItem(6, item)
        self.update_action = QtWidgets.QAction(Form_users_database)
        self.update_action.setObjectName("update_action")
        self.table_users_database.addAction(self.update_action)

        self.retranslateUi(Form_users_database)
        QtCore.QMetaObject.connectSlotsByName(Form_users_database)

    def retranslateUi(self, Form_users_database):
        _translate = QtCore.QCoreApplication.translate
        Form_users_database.setWindowTitle(_translate("Form_users_database", "База данных пользователей"))
        self.search_line_users_database.setPlaceholderText(_translate("Form_users_database", "Введите ник пользователя"))
        self.search_btn_users_database.setText(_translate("Form_users_database", "Поиск"))
        self.update_action.setText(_translate("Form_users_database", "Обновить"))
        self.update_action.setShortcut(_translate("Form_users_database", "Ctrl+U"))
        item = self.table_users_database.horizontalHeaderItem(0)
        item.setText(_translate("Form_users_database", "ID пользователя"))
        item = self.table_users_database.horizontalHeaderItem(1)
        item.setText(_translate("Form_users_database", "Имя пользователя"))
        item = self.table_users_database.horizontalHeaderItem(2)
        item.setText(_translate("Form_users_database", "Возраст"))
        item = self.table_users_database.horizontalHeaderItem(3)
        item.setText(_translate("Form_users_database", "Электронная почта"))
        item = self.table_users_database.horizontalHeaderItem(4)
        item.setText(_translate("Form_users_database", "Ник пользователя"))
        item = self.table_users_database.horizontalHeaderItem(5)
        item.setText(_translate("Form_users_database", "Пароль"))
        item = self.table_users_database.horizontalHeaderItem(6)
        item.setText(_translate("Form_users_database", "Контрольное слово"))
        

class Ui_Insert_simena_Form(object):
    def setupUi(self, Insert_simena_Form):
        Insert_simena_Form.setObjectName("Insert_simena_Form")
        Insert_simena_Form.resize(952, 896)
        Insert_simena_Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));")
        self.label = QtWidgets.QLabel(Insert_simena_Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 531, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label.setObjectName("label")
        self.name_film_insert_line_edit = QtWidgets.QLineEdit(Insert_simena_Form)
        self.name_film_insert_line_edit.setGeometry(QtCore.QRect(120, 120, 621, 61))
        self.name_film_insert_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.name_film_insert_line_edit.setObjectName("name_film_insert_line_edit")
        self.country_film_insert_line_edit = QtWidgets.QLineEdit(Insert_simena_Form)
        self.country_film_insert_line_edit.setGeometry(QtCore.QRect(120, 190, 621, 61))
        self.country_film_insert_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.country_film_insert_line_edit.setObjectName("country_film_insert_line_edit")
        self.age_lim_flim_insert_line_edit = QtWidgets.QLineEdit(Insert_simena_Form)
        self.age_lim_flim_insert_line_edit.setGeometry(QtCore.QRect(120, 260, 621, 61))
        self.age_lim_flim_insert_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.age_lim_flim_insert_line_edit.setObjectName("age_lim_flim_insert_line_edit")
        self.year_film_insert_line = QtWidgets.QLineEdit(Insert_simena_Form)
        self.year_film_insert_line.setGeometry(QtCore.QRect(120, 330, 621, 61))
        self.year_film_insert_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.year_film_insert_line.setObjectName("year_film_insert_line")
        self.director_film_insert_line = QtWidgets.QLineEdit(Insert_simena_Form)
        self.director_film_insert_line.setGeometry(QtCore.QRect(120, 400, 621, 61))
        self.director_film_insert_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.director_film_insert_line.setMaxLength(32767)
        self.director_film_insert_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.director_film_insert_line.setObjectName("director_film_insert_line")
        self.insert_film_btn = QtWidgets.QPushButton(Insert_simena_Form)
        self.insert_film_btn.setGeometry(QtCore.QRect(710, 800, 201, 61))
        self.insert_film_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"   font: 63 14pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 14pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.insert_film_btn.setObjectName("insert_film_btn")
        self.sinosis_film_insert_textEdit = QtWidgets.QTextEdit(Insert_simena_Form)
        self.sinosis_film_insert_textEdit.setGeometry(QtCore.QRect(120, 550, 761, 221))
        self.sinosis_film_insert_textEdit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.sinosis_film_insert_textEdit.setObjectName("sinosis_film_insert_textEdit")
        self.score_film_insert_line = QtWidgets.QLineEdit(Insert_simena_Form)
        self.score_film_insert_line.setGeometry(QtCore.QRect(120, 470, 621, 61))
        self.score_film_insert_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.score_film_insert_line.setMaxLength(32767)
        self.score_film_insert_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.score_film_insert_line.setObjectName("score_film_insert_line")

        self.retranslateUi(Insert_simena_Form)
        QtCore.QMetaObject.connectSlotsByName(Insert_simena_Form)

    def retranslateUi(self, Insert_simena_Form):
        _translate = QtCore.QCoreApplication.translate
        Insert_simena_Form.setWindowTitle(_translate("Insert_simena_Form", "Окно добавления фильма"))
        self.label.setText(_translate("Insert_simena_Form", "Окно добавления фильма"))
        self.name_film_insert_line_edit.setPlaceholderText(_translate("Insert_simena_Form", "Название фильма"))
        self.country_film_insert_line_edit.setPlaceholderText(_translate("Insert_simena_Form", "Страна производства"))
        self.age_lim_flim_insert_line_edit.setPlaceholderText(_translate("Insert_simena_Form", "Возрастное ограничение"))
        self.year_film_insert_line.setPlaceholderText(_translate("Insert_simena_Form", "Год выхода"))
        self.director_film_insert_line.setPlaceholderText(_translate("Insert_simena_Form", "Режессер фильма"))
        self.insert_film_btn.setText(_translate("Insert_simena_Form", "Добавить"))
        self.score_film_insert_line.setPlaceholderText(_translate("Insert_simena_Form", "Оценки "))

class Ui_edit_film_Form(object):
    def setupUi(self, edit_film_Form):
        edit_film_Form.setObjectName("edit_film_Form")
        edit_film_Form.resize(952, 896)
        edit_film_Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.155779 rgba(255, 178, 102, 255), stop:1 rgba(74, 214, 112, 255));")
        self.label = QtWidgets.QLabel(edit_film_Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 611, 61))
        self.label.setStyleSheet("font: 63 22pt \"URW Gothic\" bold;\n"
"color: white")
        self.label.setObjectName("label")
        self.name_film_edit_line_edit = QtWidgets.QLineEdit(edit_film_Form)
        self.name_film_edit_line_edit.setGeometry(QtCore.QRect(120, 110, 621, 61))
        self.name_film_edit_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.name_film_edit_line_edit.setObjectName("name_film_edit_line_edit")
        self.country_film_edit_line_edit = QtWidgets.QLineEdit(edit_film_Form)
        self.country_film_edit_line_edit.setGeometry(QtCore.QRect(120, 180, 621, 61))
        self.country_film_edit_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.country_film_edit_line_edit.setObjectName("country_film_edit_line_edit")
        self.age_lim_flim_edit_line_edit = QtWidgets.QLineEdit(edit_film_Form)
        self.age_lim_flim_edit_line_edit.setGeometry(QtCore.QRect(120, 250, 621, 61))
        self.age_lim_flim_edit_line_edit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.age_lim_flim_edit_line_edit.setObjectName("age_lim_flim_edit_line_edit")
        self.year_film_edit_line = QtWidgets.QLineEdit(edit_film_Form)
        self.year_film_edit_line.setGeometry(QtCore.QRect(120, 320, 621, 61))
        self.year_film_edit_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.year_film_edit_line.setObjectName("year_film_edit_line")
        self.director_film_edit_line = QtWidgets.QLineEdit(edit_film_Form)
        self.director_film_edit_line.setGeometry(QtCore.QRect(120, 390, 621, 61))
        self.director_film_edit_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.director_film_edit_line.setMaxLength(32767)
        self.director_film_edit_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.director_film_edit_line.setObjectName("director_film_edit_line")
        self.edit_film_btn = QtWidgets.QPushButton(edit_film_Form)
        self.edit_film_btn.setGeometry(QtCore.QRect(710, 800, 201, 61))
        self.edit_film_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 230, 200);\n"
"    color: rgb(36, 31, 49);\n"
"   font: 63 14pt \"URW Gothic\";\n"
"   border: 2px solid gray;\n"
"   border-radius: 10px;\n"
"   text-align:center\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(158, 183, 174);\n"
"    color: White;\n"
"    font: 63 14pt \"URW Gothic\";\n"
"    border: 2px solid DarkGray;\n"
"    border-radius: 10px;\n"
"    text-align:center\n"
"}")
        self.edit_film_btn.setObjectName("edit_film_btn")
        self.sinosis_film_edit_textEdit = QtWidgets.QTextEdit(edit_film_Form)
        self.sinosis_film_edit_textEdit.setGeometry(QtCore.QRect(120, 530, 761, 251))
        self.sinosis_film_edit_textEdit.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.sinosis_film_edit_textEdit.setObjectName("sinosis_film_edit_textEdit")
        self.score_film_edit_line = QtWidgets.QLineEdit(edit_film_Form)
        self.score_film_edit_line.setGeometry(QtCore.QRect(120, 460, 621, 61))
        self.score_film_edit_line.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"font: 63 15pt \"URW Gothic\";\n"
"color: rgb(36, 31, 49);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"padding-left: 20px")
        self.score_film_edit_line.setMaxLength(32767)
        self.score_film_edit_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.score_film_edit_line.setObjectName("score_film_edit_line")

        self.retranslateUi(edit_film_Form)
        QtCore.QMetaObject.connectSlotsByName(edit_film_Form)

    def retranslateUi(self, edit_film_Form):
        _translate = QtCore.QCoreApplication.translate
        edit_film_Form.setWindowTitle(_translate("edit_film_Form", "Окно редактирования записи фильма"))
        self.label.setText(_translate("edit_film_Form", "Окно редактирования данных фильма"))
        self.name_film_edit_line_edit.setPlaceholderText(_translate("edit_film_Form", "Название фильма"))
        self.country_film_edit_line_edit.setPlaceholderText(_translate("edit_film_Form", "Страна производства"))
        self.age_lim_flim_edit_line_edit.setPlaceholderText(_translate("edit_film_Form", "Возрастное ограничение"))
        self.year_film_edit_line.setPlaceholderText(_translate("edit_film_Form", "Год выхода"))
        self.director_film_edit_line.setPlaceholderText(_translate("edit_film_Form", "Режессер фильма"))
        self.edit_film_btn.setText(_translate("edit_film_Form", "Редактировать"))
        self.score_film_edit_line.setPlaceholderText(_translate("edit_film_Form", "Оценки"))