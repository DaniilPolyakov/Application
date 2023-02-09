from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_history_kids(object):
    def setupUi(self, Form_history_kids):
        Form_history_kids.setObjectName("Form_history_kids")
        Form_history_kids.resize(1448, 904)
        Form_history_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_history_kid = QtWidgets.QLineEdit(Form_history_kids)
        self.search_line_history_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_history_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_history_kid.setObjectName("search_line_history_kid")
        self.search_btn_history_kid = QtWidgets.QPushButton(Form_history_kids)
        self.search_btn_history_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_history_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_history_kid.setObjectName("search_btn_history_kid")
        self.table_history_kid = QtWidgets.QTableWidget(Form_history_kids)
        self.table_history_kid.setGeometry(QtCore.QRect(80, 120, 1201, 541))
        self.table_history_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_history_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_history_kid.setObjectName("table_history_kid")
        self.table_history_kid.setColumnCount(4)
        self.table_history_kid.setRowCount(0)
        self.table_history_kid.setColumnWidth(0,400)
        self.table_history_kid.setColumnWidth(1,300)
        self.table_history_kid.setColumnWidth(2,200)
        self.table_history_kid.setColumnWidth(3,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history_kid.setHorizontalHeaderItem(3, item)
        self.label_info_history_kid = QtWidgets.QLabel(Form_history_kids)
        self.label_info_history_kid.setGeometry(QtCore.QRect(80, 670, 1201, 181))
        self.label_info_history_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_history_kid.setText("")
        self.label_info_history_kid.setObjectName("label_info_history_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_history_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_history_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_history_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_history_kid.addAction(self.actionupgrade_action)


        self.retranslateUi(Form_history_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_history_kids)

    def retranslateUi(self, Form_history_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_history_kids.setWindowTitle(_translate("Form_history_kids", "Раздел \"Исторические фильмы\""))
        self.search_line_history_kid.setPlaceholderText(_translate("Form_history_kids", "Введите название фильма"))
        self.search_btn_history_kid.setText(_translate("Form_history_kids", "Поиск"))
        item = self.table_history_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_history_kids", "Название фильма"))
        item = self.table_history_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_history_kids", "Страна производства"))
        item = self.table_history_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_history_kids", "Год выхода"))
        item = self.table_history_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_history_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_history_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_history_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_history_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_history_kids", "Ctrl+U"))

class Ui_Form_fantasy_kids(object):
    def setupUi(self, Form_fantasy_kids):
        Form_fantasy_kids.setObjectName("Form_fantasy_kids")
        Form_fantasy_kids.resize(1448, 904)
        Form_fantasy_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_fantasy_kid = QtWidgets.QLineEdit(Form_fantasy_kids)
        self.search_line_fantasy_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_fantasy_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_fantasy_kid.setObjectName("search_line_fantasy_kid")
        self.search_btn_fantasy_kid = QtWidgets.QPushButton(Form_fantasy_kids)
        self.search_btn_fantasy_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_fantasy_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_fantasy_kid.setObjectName("search_btn_fantasy_kid")
        self.table_fantasy_kid = QtWidgets.QTableWidget(Form_fantasy_kids)
        self.table_fantasy_kid.setGeometry(QtCore.QRect(80, 120, 1201, 541))
        self.table_fantasy_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_fantasy_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_fantasy_kid.setObjectName("table_fantasy_kid")
        self.table_fantasy_kid.setColumnCount(4)
        self.table_fantasy_kid.setRowCount(0)
        self.table_fantasy_kid.setColumnWidth(0,400)
        self.table_fantasy_kid.setColumnWidth(1,300)
        self.table_fantasy_kid.setColumnWidth(2,200)
        self.table_fantasy_kid.setColumnWidth(3,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy_kid.setHorizontalHeaderItem(3, item)
        self.label_info_fantasy_kid = QtWidgets.QLabel(Form_fantasy_kids)
        self.label_info_fantasy_kid.setGeometry(QtCore.QRect(80, 670, 1201, 181))
        self.label_info_fantasy_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_fantasy_kid.setText("")
        self.label_info_fantasy_kid.setObjectName("label_info_fantasy_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_fantasy_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_fantasy_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_fantasy_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_fantasy_kid.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_fantasy_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_fantasy_kids)

    def retranslateUi(self, Form_fantasy_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_fantasy_kids.setWindowTitle(_translate("Form_fantasy_kids", "Раздел \"Фантастические фильмы\""))
        self.search_line_fantasy_kid.setPlaceholderText(_translate("Form_fantasy_kids", "Введите название фильма"))
        self.search_btn_fantasy_kid.setText(_translate("Form_fantasy_kids", "Поиск"))
        item = self.table_fantasy_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_fantasy_kids", "Название фильма"))
        item = self.table_fantasy_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_fantasy_kids", "Страна производства"))
        item = self.table_fantasy_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_fantasy_kids", "Год выхода"))
        item = self.table_fantasy_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_fantasy_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_fantasy_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_fantasy_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_fantasy_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_fantasy_kids", "Ctrl+U"))


class Ui_Form_comedy_kids(object):
    def setupUi(self, Form_comedy_kids):
        Form_comedy_kids.setObjectName("Form_comedy_kids")
        Form_comedy_kids.resize(1448, 904)
        Form_comedy_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_comedy_kid = QtWidgets.QLineEdit(Form_comedy_kids)
        self.search_line_comedy_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_comedy_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_comedy_kid.setObjectName("search_line_comedy_kid")
        self.search_btn_comedy_kid = QtWidgets.QPushButton(Form_comedy_kids)
        self.search_btn_comedy_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_comedy_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_comedy_kid.setObjectName("search_btn_comedy_kid")
        self.table_comedy_kid = QtWidgets.QTableWidget(Form_comedy_kids)
        self.table_comedy_kid.setGeometry(QtCore.QRect(80, 120, 1201, 541))
        self.table_comedy_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_comedy_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_comedy_kid.setObjectName("table_comedy_kid")
        self.table_comedy_kid.setColumnCount(4)
        self.table_comedy_kid.setRowCount(0)
        self.table_comedy_kid.setColumnWidth(0,400)
        self.table_comedy_kid.setColumnWidth(1,300)
        self.table_comedy_kid.setColumnWidth(2,200)
        self.table_comedy_kid.setColumnWidth(3,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy_kid.setHorizontalHeaderItem(3, item)
        self.label_info_comedy_kid = QtWidgets.QLabel(Form_comedy_kids)
        self.label_info_comedy_kid.setGeometry(QtCore.QRect(80, 670, 1201, 181))
        self.label_info_comedy_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_comedy_kid.setText("")
        self.label_info_comedy_kid.setObjectName("label_info_comedy_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_comedy_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_comedy_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_comedy_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_comedy_kid.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_comedy_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_comedy_kids)

    def retranslateUi(self, Form_comedy_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_comedy_kids.setWindowTitle(_translate("Form_comedy_kids", "Раздел \"Комедии\""))
        self.search_line_comedy_kid.setPlaceholderText(_translate("Form_comedy_kids", "Введите название фильма"))
        self.search_btn_comedy_kid.setText(_translate("Form_comedy_kids", "Поиск"))
        item = self.table_comedy_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_comedy_kids", "Название фильма"))
        item = self.table_comedy_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_comedy_kids", "Страна производства"))
        item = self.table_comedy_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_comedy_kids", "Год выхода"))
        item = self.table_comedy_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_comedy_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_comedy_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_comedy_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_comedy_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_comedy_kids", "Ctrl+U"))

class Ui_Form_serials_kids(object):
    def setupUi(self, Form_serials_kids):
        Form_serials_kids.setObjectName("Form_serials_kids")
        Form_serials_kids.resize(1448, 904)
        Form_serials_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_serials_kid = QtWidgets.QLineEdit(Form_serials_kids)
        self.search_line_serials_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_serials_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_serials_kid.setObjectName("search_line_serials_kid")
        self.search_btn_serials_kid = QtWidgets.QPushButton(Form_serials_kids)
        self.search_btn_serials_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_serials_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_serials_kid.setObjectName("search_btn_serials_kid")
        self.table_serials_kid = QtWidgets.QTableWidget(Form_serials_kids)
        self.table_serials_kid.setGeometry(QtCore.QRect(80, 120, 1201, 541))
        self.table_serials_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_serials_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_serials_kid.setObjectName("table_serials_kid")
        self.table_serials_kid.setColumnCount(4)
        self.table_serials_kid.setRowCount(0)
        self.table_serials_kid.setColumnWidth(0,400)
        self.table_serials_kid.setColumnWidth(1,300)
        self.table_serials_kid.setColumnWidth(2,200)
        self.table_serials_kid.setColumnWidth(3,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_serials_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serials_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serials_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serials_kid.setHorizontalHeaderItem(3, item)
        self.label_info_serials_kid = QtWidgets.QLabel(Form_serials_kids)
        self.label_info_serials_kid.setGeometry(QtCore.QRect(80, 670, 1201, 181))
        self.label_info_serials_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_serials_kid.setText("")
        self.label_info_serials_kid.setObjectName("label_info_serials_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_serials_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_serials_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_serials_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_serials_kid.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_serials_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_serials_kids)

    def retranslateUi(self, Form_serials_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_serials_kids.setWindowTitle(_translate("Form_serials_kids", "Раздел \"Сериалы\""))
        self.search_line_serials_kid.setPlaceholderText(_translate("Form_serials_kids", "Введите название сериала"))
        self.search_btn_serials_kid.setText(_translate("Form_serials_kids", "Поиск"))
        item = self.table_serials_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_serials_kids", "Название сериала"))
        item = self.table_serials_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_serials_kids", "Страна производства"))
        item = self.table_serials_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_serials_kids", "Год выхода"))
        item = self.table_serials_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_serials_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_serial_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_serial_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_serial_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_serial_kids", "Ctrl+U"))

class Ui_Form_new_kids(object):
    def setupUi(self, Form_new_kids):
        Form_new_kids.setObjectName("Form_new_kids")
        Form_new_kids.resize(1448, 904)
        Form_new_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_new_kid = QtWidgets.QLineEdit(Form_new_kids)
        self.search_line_new_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_new_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_new_kid.setObjectName("search_line_new_kid")
        self.search_btn_new_kid = QtWidgets.QPushButton(Form_new_kids)
        self.search_btn_new_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_new_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_new_kid.setObjectName("search_btn_new_kid")
        self.table_new_kid = QtWidgets.QTableWidget(Form_new_kids)
        self.table_new_kid.setGeometry(QtCore.QRect(20, 120, 1321, 541))
        self.table_new_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_new_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_new_kid.setObjectName("table_new_kid")
        self.table_new_kid.setColumnCount(5)
        self.table_new_kid.setRowCount(0)
        self.table_new_kid.setColumnWidth(0,350)
        self.table_new_kid.setColumnWidth(1,350)
        self.table_new_kid.setColumnWidth(2,350)
        self.table_new_kid.setColumnWidth(3,200)
        self.table_new_kid.setColumnWidth(4,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_kid.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new_kid.setHorizontalHeaderItem(4, item)
        self.label_info_new_kid = QtWidgets.QLabel(Form_new_kids)
        self.label_info_new_kid.setGeometry(QtCore.QRect(20, 680, 1321, 181))
        self.label_info_new_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_new_kid.setText("")
        self.label_info_new_kid.setObjectName("label_info_new_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_new_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_new_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_new_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_new_kid.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_new_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_new_kids)

    def retranslateUi(self, Form_new_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_new_kids.setWindowTitle(_translate("Form_new_kids", "Раздел \"Новинки\""))
        self.search_line_new_kid.setPlaceholderText(_translate("Form_new_kids", "Введите название фильма"))
        self.search_btn_new_kid.setText(_translate("Form_new_kids", "Поиск"))
        item = self.table_new_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_new_kids", "Название фильма"))
        item = self.table_new_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_new_kids", "Жанр"))
        item = self.table_new_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_new_kids", "Страна производства"))
        item = self.table_new_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_new_kids", "Год выхода"))
        item = self.table_new_kid.horizontalHeaderItem(4)
        item.setText(_translate("Form_new_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_new_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_new_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_new_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_new_kids", "Ctrl+U"))


class Ui_Form_cartoon_kids(object):
    def setupUi(self, Form_cartoon_kids):
        Form_cartoon_kids.setObjectName("Form_cartoon_kids")
        Form_cartoon_kids.resize(1448, 904)
        Form_cartoon_kids.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.080402 rgba(243, 136, 244, 255), stop:0.316583 rgba(226, 55, 183, 255), stop:0.713568 rgba(124, 94, 234, 255));\n"
"")
        self.search_line_cartoon_kid = QtWidgets.QLineEdit(Form_cartoon_kids)
        self.search_line_cartoon_kid.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_cartoon_kid.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_cartoon_kid.setObjectName("search_line_cartoon_kid")
        self.search_btn_cartoon_kid = QtWidgets.QPushButton(Form_cartoon_kids)
        self.search_btn_cartoon_kid.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_cartoon_kid.setStyleSheet("QPushButton {\n"
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
        self.search_btn_cartoon_kid.setObjectName("search_btn_cartoon_kid")
        self.table_cartoon_kid = QtWidgets.QTableWidget(Form_cartoon_kids)
        self.table_cartoon_kid.setGeometry(QtCore.QRect(80, 120, 1201, 541))
        self.table_cartoon_kid.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_cartoon_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_cartoon_kid.setObjectName("table_cartoon_kid")
        self.table_cartoon_kid.setColumnCount(4)
        self.table_cartoon_kid.setRowCount(0)
        self.table_cartoon_kid.setColumnWidth(0,400)
        self.table_cartoon_kid.setColumnWidth(1,300)
        self.table_cartoon_kid.setColumnWidth(2,200)
        self.table_cartoon_kid.setColumnWidth(3,200)
        item = QtWidgets.QTableWidgetItem()
        self.table_cartoon_kid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cartoon_kid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cartoon_kid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cartoon_kid.setHorizontalHeaderItem(3, item)
        self.label_info_cartoon_kid = QtWidgets.QLabel(Form_cartoon_kids)
        self.label_info_cartoon_kid.setGeometry(QtCore.QRect(80, 670, 1201, 181))
        self.label_info_cartoon_kid.setStyleSheet("background-color: rgb(204, 174, 224);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.label_info_cartoon_kid.setText("")
        self.label_info_cartoon_kid.setObjectName("label_info_cartoon_kid")
        self.actioninfo_action = QtWidgets.QAction(Form_cartoon_kids)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_cartoon_kid.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_cartoon_kids)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_cartoon_kid.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_cartoon_kids)
        QtCore.QMetaObject.connectSlotsByName(Form_cartoon_kids)

    def retranslateUi(self, Form_cartoon_kids):
        _translate = QtCore.QCoreApplication.translate
        Form_cartoon_kids.setWindowTitle(_translate("Form_cartoon_kids", "Раздел \"Мультфильмы\""))
        self.search_line_cartoon_kid.setPlaceholderText(_translate("Form_cartoon_kids", "Введите название фильма"))
        self.search_btn_cartoon_kid.setText(_translate("Form_cartoon_kids", "Поиск"))
        item = self.table_cartoon_kid.horizontalHeaderItem(0)
        item.setText(_translate("Form_cartoon_kids", "Название мультфильма"))
        item = self.table_cartoon_kid.horizontalHeaderItem(1)
        item.setText(_translate("Form_cartoon_kids", "Страна производства"))
        item = self.table_cartoon_kid.horizontalHeaderItem(2)
        item.setText(_translate("Form_cartoon_kids", "Год выхода"))
        item = self.table_cartoon_kid.horizontalHeaderItem(3)
        item.setText(_translate("Form_cartoon_kids", "Возрастное ограничение"))
        self.actioninfo_action.setText(_translate("Form_cartoon_kids", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_cartoon_kids", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_cartoon_kids", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_cartoon_kids", "Ctrl+U"))
