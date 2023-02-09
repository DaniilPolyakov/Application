from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_action(object):
    def setupUi(self, Form_action):
        Form_action.setObjectName("Form_action")
        Form_action.resize(1448, 904)
        Form_action.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_action = QtWidgets.QLineEdit(Form_action)
        self.search_line_action.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_action.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_action.setObjectName("search_line_action")
        self.search_btn_action = QtWidgets.QPushButton(Form_action)
        self.search_btn_action.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_action.setStyleSheet("QPushButton {\n"
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
        self.search_btn_action.setObjectName("search_btn_action")
        self.table_action = QtWidgets.QTableWidget(Form_action)
        self.table_action.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_action.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_action.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_action.setObjectName("table_action")
        self.table_action.setColumnCount(5)
        self.table_action.setRowCount(0)
        self.table_action.setColumnWidth(0,400)
        self.table_action.setColumnWidth(1,300)
        self.table_action.setColumnWidth(2,200)
        self.table_action.setColumnWidth(3,200)
        self.table_action.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_action.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_action.setHorizontalHeaderItem(4, item)
        self.lable_info_action = QtWidgets.QLabel(Form_action)
        self.lable_info_action.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_action.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_action.setText("")
        self.lable_info_action.setObjectName("lable_info_action")
        self.actioninfo_action = QtWidgets.QAction(Form_action)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_action.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_action)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_action.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_action)
        QtCore.QMetaObject.connectSlotsByName(Form_action)
        


    def retranslateUi(self, Form_action):
        _translate = QtCore.QCoreApplication.translate
        Form_action.setWindowTitle(_translate("Form_action", "Раздел \"Боевики\""))
        self.search_line_action.setPlaceholderText(_translate("Form_action", "Введите название фильма"))
        self.search_btn_action.setText(_translate("Form_action", "Поиск"))
        item = self.table_action.horizontalHeaderItem(0)
        item.setText(_translate("Form_action", "Название фильма"))
        item = self.table_action.horizontalHeaderItem(1)
        item.setText(_translate("Form_action", "Страна производства"))
        item = self.table_action.horizontalHeaderItem(2)
        item.setText(_translate("Form_action", "Год выхода"))
        item = self.table_action.horizontalHeaderItem(3)
        item.setText(_translate("Form_action", "Возрастное ограничение"))
        item = self.table_action.horizontalHeaderItem(4)
        item.setText(_translate("Form_action", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_action", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_action", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_action", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_action", "Ctrl+U"))

class Ui_Form_comedy(object):
    def setupUi(self, Form_comedy):
        Form_comedy.setObjectName("Form_comedy")
        Form_comedy.resize(1448, 904)
        Form_comedy.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_comedy = QtWidgets.QLineEdit(Form_comedy)
        self.search_line_comedy.setGeometry(QtCore.QRect(80, 30, 781, 51))

        self.search_line_comedy.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_comedy.setObjectName("search_line_comedy")
        self.search_btn_comedy = QtWidgets.QPushButton(Form_comedy)
        self.search_btn_comedy.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_comedy.setStyleSheet("QPushButton {\n"
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
        self.search_btn_comedy.setObjectName("search_btn_comedy")
        self.table_comedy = QtWidgets.QTableWidget(Form_comedy)
        self.table_comedy.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_comedy.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_comedy.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_comedy.setObjectName("table_comedy")
        self.table_comedy.setColumnCount(5)
        self.table_comedy.setRowCount(0)
        self.table_comedy.setColumnWidth(0,400)
        self.table_comedy.setColumnWidth(1,300)
        self.table_comedy.setColumnWidth(2,200)
        self.table_comedy.setColumnWidth(3,200)
        self.table_comedy.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_comedy.setHorizontalHeaderItem(4, item)
        self.lable_info_comedy = QtWidgets.QLabel(Form_comedy)
        self.lable_info_comedy.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_comedy.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_comedy.setText("")
        self.lable_info_comedy.setObjectName("lable_info_comedy")
        self.actioninfo_action = QtWidgets.QAction(Form_comedy)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_comedy.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_comedy)
        self.actionupgrade_action.setObjectName("actionupgarde_action")
        self.table_comedy.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_comedy)
        QtCore.QMetaObject.connectSlotsByName(Form_comedy)

    def retranslateUi(self, Form_comedy):
        _translate = QtCore.QCoreApplication.translate
        Form_comedy.setWindowTitle(_translate("Form_comedy", "Раздел \"Комедии\""))
        self.search_line_comedy.setPlaceholderText(_translate("Form_comedy", "Введите название фильма"))
        self.search_btn_comedy.setText(_translate("Form_comedy", "Поиск"))
        item = self.table_comedy.horizontalHeaderItem(0)
        item.setText(_translate("Form_comedy", "Название фильма"))
        item = self.table_comedy.horizontalHeaderItem(1)
        item.setText(_translate("Form_comedy", "Страна производства"))
        item = self.table_comedy.horizontalHeaderItem(2)
        item.setText(_translate("Form_comedy", "Год выхода"))
        item = self.table_comedy.horizontalHeaderItem(3)
        item.setText(_translate("Form_comedy", "Возрастное ограничение"))
        item = self.table_comedy.horizontalHeaderItem(4)
        item.setText(_translate("Form_comedy", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_comedy", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_comedy", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_comedy", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_comedy", "Ctrl+U"))

class Ui_Form_dram(object):
    def setupUi(self, Form_dram):
        Form_dram.setObjectName("Form_dram")
        Form_dram.resize(1448, 904)
        Form_dram.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_dram = QtWidgets.QLineEdit(Form_dram)
        self.search_line_dram.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_dram.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_dram.setObjectName("search_line_dram")
        self.search_btn_dram = QtWidgets.QPushButton(Form_dram)
        self.search_btn_dram.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_dram.setStyleSheet("QPushButton {\n"
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
        self.search_btn_dram.setObjectName("search_btn_dram")
        self.table_dram = QtWidgets.QTableWidget(Form_dram)
        self.table_dram.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_dram.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_dram.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_dram.setObjectName("table_dram")
        self.table_dram.setColumnCount(5)
        self.table_dram.setRowCount(0)
        self.table_dram.setColumnWidth(0,400)
        self.table_dram.setColumnWidth(1,300)
        self.table_dram.setColumnWidth(2,200)
        self.table_dram.setColumnWidth(3,200)
        self.table_dram.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_dram.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dram.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dram.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dram.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dram.setHorizontalHeaderItem(4, item)
        self.lable_info_dram = QtWidgets.QLabel(Form_dram)
        self.lable_info_dram.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_dram.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_dram.setText("")
        self.lable_info_dram.setObjectName("lable_info_dram")
        self.actioninfo_action = QtWidgets.QAction(Form_dram)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_dram.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_dram)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_dram.addAction(self.actionupgrade_action)
        self.retranslateUi(Form_dram)
        QtCore.QMetaObject.connectSlotsByName(Form_dram)

    def retranslateUi(self, Form_dram):
        _translate = QtCore.QCoreApplication.translate
        Form_dram.setWindowTitle(_translate("Form_dram", "Раздел \"Драмы\""))
        self.search_line_dram.setPlaceholderText(_translate("Form_dram", "Введите название фильма"))
        self.search_btn_dram.setText(_translate("Form_dram", "Поиск"))
        item = self.table_dram.horizontalHeaderItem(0)
        item.setText(_translate("Form_dram", "Название фильма"))
        item = self.table_dram.horizontalHeaderItem(1)
        item.setText(_translate("Form_dram", "Страна производства"))
        item = self.table_dram.horizontalHeaderItem(2)
        item.setText(_translate("Form_dram", "Год выхода"))
        item = self.table_dram.horizontalHeaderItem(3)
        item.setText(_translate("Form_dram", "Возрастное ограничение"))
        item = self.table_dram.horizontalHeaderItem(4)
        item.setText(_translate("Form_dram", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_dram", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_dram", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_dram", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_dram", "Ctrl+U"))

class Ui_Form_fantasy(object):
    def setupUi(self, Form_fantasy):
        Form_fantasy.setObjectName("Form_fantasy")
        Form_fantasy.resize(1448, 904)
        Form_fantasy.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_fantasy = QtWidgets.QLineEdit(Form_fantasy)
        self.search_line_fantasy.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_fantasy.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_fantasy.setObjectName("search_line_fantasy")
        self.search_btn_fantasy = QtWidgets.QPushButton(Form_fantasy)
        self.search_btn_fantasy.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_fantasy.setStyleSheet("QPushButton {\n"
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
        self.search_btn_fantasy.setObjectName("search_btn_fantasy")
        self.table_fantasy = QtWidgets.QTableWidget(Form_fantasy)
        self.table_fantasy.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_fantasy.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_fantasy.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_fantasy.setObjectName("table_fantasy")
        self.table_fantasy.setColumnCount(5)
        self.table_fantasy.setRowCount(0)
        self.table_fantasy.setColumnWidth(0,400)
        self.table_fantasy.setColumnWidth(1,300)
        self.table_fantasy.setColumnWidth(2,200)
        self.table_fantasy.setColumnWidth(3,200)
        self.table_fantasy.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fantasy.setHorizontalHeaderItem(4, item)
        self.lable_info_fantasy = QtWidgets.QLabel(Form_fantasy)
        self.lable_info_fantasy.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_fantasy.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_fantasy.setText("")
        self.lable_info_fantasy.setObjectName("lable_info_fantasy")
        self.actioninfo_action = QtWidgets.QAction(Form_fantasy)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_fantasy.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_fantasy)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_fantasy.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_fantasy)
        QtCore.QMetaObject.connectSlotsByName(Form_fantasy)

    def retranslateUi(self, Form_fantasy):
        _translate = QtCore.QCoreApplication.translate
        Form_fantasy.setWindowTitle(_translate("Form_fantasy", "Раздел \"Фантастические фильмы\""))
        self.search_line_fantasy.setPlaceholderText(_translate("Form_fantasy", "Введите название фильма"))
        self.search_btn_fantasy.setText(_translate("Form_fantasy", "Поиск"))
        item = self.table_fantasy.horizontalHeaderItem(0)
        item.setText(_translate("Form_fantasy", "Название фильма"))
        item = self.table_fantasy.horizontalHeaderItem(1)
        item.setText(_translate("Form_fantasy", "Страна производства"))
        item = self.table_fantasy.horizontalHeaderItem(2)
        item.setText(_translate("Form_fantasy", "Год выхода"))
        item = self.table_fantasy.horizontalHeaderItem(3)
        item.setText(_translate("Form_fantasy", "Возрастное ограничение"))
        item = self.table_fantasy.horizontalHeaderItem(4)
        item.setText(_translate("Form_fantasy", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_fantasy", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_fantasy", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_fantasy", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_fantasy", "Ctrl+U"))

class Ui_Form_history(object):
    def setupUi(self, Form_history):
        Form_history.setObjectName("Form_history")
        Form_history.resize(1448, 904)
        Form_history.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_history = QtWidgets.QLineEdit(Form_history)
        self.search_line_history.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_history.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_history.setObjectName("search_line_history")
        self.search_btn_history = QtWidgets.QPushButton(Form_history)
        self.search_btn_history.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_history.setStyleSheet("QPushButton {\n"
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
        self.search_btn_history.setObjectName("search_btn_history")
        self.table_history = QtWidgets.QTableWidget(Form_history)
        self.table_history.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_history.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_history.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_history.setObjectName("table_history")
        self.table_history.setColumnCount(5)
        self.table_history.setRowCount(0)
        self.table_history.setColumnWidth(0,400)
        self.table_history.setColumnWidth(1,300)
        self.table_history.setColumnWidth(2,200)
        self.table_history.setColumnWidth(3,200)
        self.table_history.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(4, item)
        self.lable_info_history = QtWidgets.QLabel(Form_history)
        self.lable_info_history.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_history.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_history.setText("")
        self.lable_info_history.setObjectName("lable_info_history")
        self.actioninfo_action = QtWidgets.QAction(Form_history)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_history.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_history)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_history.addAction(self.actionupgrade_action)


        self.retranslateUi(Form_history)
        QtCore.QMetaObject.connectSlotsByName(Form_history)
        

    def retranslateUi(self, Form_history):
        _translate = QtCore.QCoreApplication.translate
        Form_history.setWindowTitle(_translate("Form_history", "Раздел \"Исторические фильмы и Биографии\""))
        self.search_line_history.setPlaceholderText(_translate("Form_history", "Введите название фильма"))
        self.search_btn_history.setText(_translate("Form_history", "Поиск"))
        item = self.table_history.horizontalHeaderItem(0)
        item.setText(_translate("Form_history", "Название фильма"))
        item = self.table_history.horizontalHeaderItem(1)
        item.setText(_translate("Form_history", "Страна производства"))
        item = self.table_history.horizontalHeaderItem(2)
        item.setText(_translate("Form_history", "гГода выхода"))
        item = self.table_history.horizontalHeaderItem(3)
        item.setText(_translate("Form_history", "Возрастное ограничение"))
        item = self.table_history.horizontalHeaderItem(4)
        item.setText(_translate("Form_history", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_history", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_history", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_history", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_history", "Ctrl+U"))

class Ui_Form_horror(object):
    def setupUi(self, Form_horror):
        Form_horror.setObjectName("Form_horror")
        Form_horror.resize(1448, 904)
        Form_horror.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_horror = QtWidgets.QLineEdit(Form_horror)
        self.search_line_horror.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_horror.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_horror.setObjectName("search_line_horror")
        self.search_btn_horror = QtWidgets.QPushButton(Form_horror)
        self.search_btn_horror.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_horror.setStyleSheet("QPushButton {\n"
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
        self.search_btn_horror.setObjectName("search_btn_horror")
        self.table_horror = QtWidgets.QTableWidget(Form_horror)
        self.table_horror.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_horror.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_horror.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_horror.setObjectName("table_horror")
        self.table_horror.setColumnCount(5)
        self.table_horror.setRowCount(0)
        self.table_horror.setColumnWidth(0,400)
        self.table_horror.setColumnWidth(1,300)
        self.table_horror.setColumnWidth(2,200)
        self.table_horror.setColumnWidth(3,200)
        self.table_horror.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_horror.setHorizontalHeaderItem(4, item)
        self.lable_info_horror = QtWidgets.QLabel(Form_horror)
        self.lable_info_horror.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_horror.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_horror.setText("")
        self.lable_info_horror.setObjectName("lable_info_horror")
        self.actioninfo_action = QtWidgets.QAction(Form_horror)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_horror.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_horror)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_horror.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_horror)
        QtCore.QMetaObject.connectSlotsByName(Form_horror)

    def retranslateUi(self, Form_horror):
        _translate = QtCore.QCoreApplication.translate
        Form_horror.setWindowTitle(_translate("Form_horror", "Раздел \"Фильмы Ужасов\""))
        self.search_line_horror.setPlaceholderText(_translate("Form_horror", "Введите название фильма"))
        self.search_btn_horror.setText(_translate("Form_horror", "Поиск"))
        item = self.table_horror.horizontalHeaderItem(0)
        item.setText(_translate("Form_horror", "Название фильма"))
        item = self.table_horror.horizontalHeaderItem(1)
        item.setText(_translate("Form_horror", "Страна производства"))
        item = self.table_horror.horizontalHeaderItem(2)
        item.setText(_translate("Form_horror", "Года выхода"))
        item = self.table_horror.horizontalHeaderItem(3)
        item.setText(_translate("Form_horror", "Возрастное ограничение"))
        item = self.table_horror.horizontalHeaderItem(4)
        item.setText(_translate("Form_horror", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_horror", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_horror", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_horror", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_horror", "Ctrl+U"))

class Ui_Form_new(object):
    def setupUi(self, Form_new):
        Form_new.setObjectName("Form_new")
        Form_new.resize(1448, 904)
        Form_new.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_new = QtWidgets.QLineEdit(Form_new)
        self.search_line_new.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_new.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_new.setObjectName("search_line_new")
        self.search_btn_new = QtWidgets.QPushButton(Form_new)
        self.search_btn_new.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_new.setStyleSheet("QPushButton {\n"
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
        self.search_btn_new.setObjectName("search_btn_new")
        self.table_new = QtWidgets.QTableWidget(Form_new)
        self.table_new.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_new.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_new.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_new.setObjectName("table_new")
        self.table_new.setColumnCount(6)
        self.table_new.setRowCount(0)
        self.table_new.setColumnWidth(0,400)
        self.table_new.setColumnWidth(1,300)
        self.table_new.setColumnWidth(2,200)
        self.table_new.setColumnWidth(3,200)
        self.table_new.setColumnWidth(4,190)
        self.table_new.setColumnWidth(5,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_new.setHorizontalHeaderItem(5, item)
        self.lable_info_new = QtWidgets.QLabel(Form_new)
        self.lable_info_new.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_new.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_new.setText("")
        self.lable_info_new.setObjectName("lable_info_new")
        self.actioninfo_action = QtWidgets.QAction(Form_new)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_new.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_new)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_new.addAction(self.actionupgrade_action)


        self.retranslateUi(Form_new)
        QtCore.QMetaObject.connectSlotsByName(Form_new)

    def retranslateUi(self, Form_new):
        _translate = QtCore.QCoreApplication.translate
        Form_new.setWindowTitle(_translate("Form_new", "Раздел \"Новинки\""))
        self.search_line_new.setPlaceholderText(_translate("Form_new", "Введите название фильма"))
        self.search_btn_new.setText(_translate("Form_new", "Поиск"))
        item = self.table_new.horizontalHeaderItem(0)
        item.setText(_translate("Form_new", "Название фильма"))
        item = self.table_new.horizontalHeaderItem(1)
        item.setText(_translate("Form_new", "Жанр"))
        item = self.table_new.horizontalHeaderItem(2)
        item.setText(_translate("Form_new", "Страна производства"))
        item = self.table_new.horizontalHeaderItem(3)
        item.setText(_translate("Form_new", "Год выхода"))
        item = self.table_new.horizontalHeaderItem(4)
        item.setText(_translate("Form_new", "Возрастное ограничение"))
        item = self.table_new.horizontalHeaderItem(5)
        item.setText(_translate("Form_new", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_new", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_new", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_new", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_new", "Ctrl+U"))

class Ui_Form_serial(object):
    def setupUi(self, Form_serial):
        Form_serial.setObjectName("Form_serial")
        Form_serial.resize(1448, 904)
        Form_serial.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_serial = QtWidgets.QLineEdit(Form_serial)
        self.search_line_serial.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_serial.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_serial.setObjectName("search_line_serial")
        self.search_btn_serial = QtWidgets.QPushButton(Form_serial)
        self.search_btn_serial.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_serial.setStyleSheet("QPushButton {\n"
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
        self.search_btn_serial.setObjectName("search_btn_serial")
        self.table_serial = QtWidgets.QTableWidget(Form_serial)
        self.table_serial.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_serial.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_serial.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_serial.setObjectName("table_serial")
        self.table_serial.setColumnCount(5)
        self.table_serial.setRowCount(0)
        self.table_serial.setColumnWidth(0,400)
        self.table_serial.setColumnWidth(1,300)
        self.table_serial.setColumnWidth(2,200)
        self.table_serial.setColumnWidth(3,200)
        self.table_serial.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_serial.setHorizontalHeaderItem(4, item)
        self.lable_info_serial = QtWidgets.QLabel(Form_serial)
        self.lable_info_serial.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_serial.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_serial.setText("")
        self.lable_info_serial.setObjectName("lable_info_serial")
        self.actioninfo_action = QtWidgets.QAction(Form_serial)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_serial.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_serial)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_serial.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_serial)
        QtCore.QMetaObject.connectSlotsByName(Form_serial)

    def retranslateUi(self, Form_serial):
        _translate = QtCore.QCoreApplication.translate
        Form_serial.setWindowTitle(_translate("Form_serial", "Раздел \"Сериалы\""))
        self.search_line_serial.setPlaceholderText(_translate("Form_serial", "Введите название сериала"))
        self.search_btn_serial.setText(_translate("Form_serial", "Поиск"))
        item = self.table_serial.horizontalHeaderItem(0)
        item.setText(_translate("Form_serial", "Название сериала"))
        item = self.table_serial.horizontalHeaderItem(1)
        item.setText(_translate("Form_serial", "Страна производства"))
        item = self.table_serial.horizontalHeaderItem(2)
        item.setText(_translate("Form_serial", "Год выхода"))
        item = self.table_serial.horizontalHeaderItem(3)
        item.setText(_translate("Form_serial", "Возрастное ограничение"))
        item = self.table_serial.horizontalHeaderItem(4)
        item.setText(_translate("Form_serial", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_serial", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_serial", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_serial", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_serial", "Ctrl+U"))

class Ui_Form_animation(object):
    def setupUi(self, Form_animation):
        Form_animation.setObjectName("Form_animation")
        Form_animation.resize(1448, 904)
        Form_animation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_animation = QtWidgets.QLineEdit(Form_animation)
        self.search_line_animation.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_animation.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_animation.setObjectName("search_line_animation")
        self.search_btn_animation = QtWidgets.QPushButton(Form_animation)
        self.search_btn_animation.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_animation.setStyleSheet("QPushButton {\n"
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
        self.search_btn_animation.setObjectName("search_btn_animation")
        self.table_animation = QtWidgets.QTableWidget(Form_animation)
        self.table_animation.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_animation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_animation.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_animation.setObjectName("table_animation")
        self.table_animation.setColumnCount(5)
        self.table_animation.setRowCount(0)
        self.table_animation.setColumnWidth(0,400)
        self.table_animation.setColumnWidth(1,300)
        self.table_animation.setColumnWidth(2,200)
        self.table_animation.setColumnWidth(3,200)
        self.table_animation.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_animation.setHorizontalHeaderItem(4, item)
        self.lable_info_animation = QtWidgets.QLabel(Form_animation)
        self.lable_info_animation.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_animation.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_animation.setText("")
        self.lable_info_animation.setObjectName("lable_info_animation")
        self.actioninfo_action = QtWidgets.QAction(Form_animation)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_animation.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_animation)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_animation.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_animation)
        QtCore.QMetaObject.connectSlotsByName(Form_animation)

    def retranslateUi(self, Form_animation):
        _translate = QtCore.QCoreApplication.translate
        Form_animation.setWindowTitle(_translate("Form_animation", "Раздел \"Анимационные фильмы\""))
        self.search_line_animation.setPlaceholderText(_translate("Form_animation", "Введите название фильма"))
        self.search_btn_animation.setText(_translate("Form_animation", "Поиск"))
        item = self.table_animation.horizontalHeaderItem(0)
        item.setText(_translate("Form_animation", "Название фильма"))
        item = self.table_animation.horizontalHeaderItem(1)
        item.setText(_translate("Form_animation", "Страна производства"))
        item = self.table_animation.horizontalHeaderItem(2)
        item.setText(_translate("Form_animation", "Год выхода"))
        item = self.table_animation.horizontalHeaderItem(3)
        item.setText(_translate("Form_animation", "Возрастное ограничение"))
        item = self.table_animation.horizontalHeaderItem(4)
        item.setText(_translate("Form_animation", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_animation", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_animation", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_animation", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_animation", "Ctrl+U"))

class Ui_Form_detective(object):
    def setupUi(self, Form_detective):
        Form_detective.setObjectName("Form_detective")
        Form_detective.resize(1448, 904)
        Form_detective.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.125628 rgba(102, 13, 141, 255), stop:0.38191 rgba(89, 10, 77, 255), stop:0.78392 rgba(45, 0, 103, 255));\n"
"")
        self.search_line_detective = QtWidgets.QLineEdit(Form_detective)
        self.search_line_detective.setGeometry(QtCore.QRect(80, 30, 781, 51))
        self.search_line_detective.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 14pt \"URW Gothic\";\n"
"border: 2px solid rgb(154, 153, 150);\n"
"padding-left:20")
        self.search_line_detective.setObjectName("search_line_detective")
        self.search_btn_detective = QtWidgets.QPushButton(Form_detective)
        self.search_btn_detective.setGeometry(QtCore.QRect(890, 30, 101, 51))
        self.search_btn_detective.setStyleSheet("QPushButton {\n"
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
        self.search_btn_detective.setObjectName("search_btn_detective")
        self.table_detective = QtWidgets.QTableWidget(Form_detective)
        self.table_detective.setGeometry(QtCore.QRect(30, 110, 1301, 541))
        self.table_detective.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_detective.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(36, 31, 49);\n"
"font: 63 12pt \"URW Gothic\";")
        self.table_detective.setObjectName("table_detective")
        self.table_detective.setColumnCount(5)
        self.table_detective.setRowCount(0)
        self.table_detective.setColumnWidth(0,400)
        self.table_detective.setColumnWidth(1,300)
        self.table_detective.setColumnWidth(2,200)
        self.table_detective.setColumnWidth(3,200)
        self.table_detective.setColumnWidth(4,190)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_detective.setHorizontalHeaderItem(4, item)
        self.lable_info_detective = QtWidgets.QLabel(Form_detective)
        self.lable_info_detective.setGeometry(QtCore.QRect(30, 670, 1301, 181))
        self.lable_info_detective.setStyleSheet("background-color: rgb(230, 212, 250);\n"
"color: rgb(0, 0, 0);\n"
"padding:10;\n"
"text-align:left")
        self.lable_info_detective.setText("")
        self.lable_info_detective.setObjectName("lable_info_detective")
        self.actioninfo_action = QtWidgets.QAction(Form_detective)
        self.actioninfo_action.setObjectName("actioninfo_action")
        self.table_detective.addAction(self.actioninfo_action)
        self.actionupgrade_action = QtWidgets.QAction(Form_detective)
        self.actionupgrade_action.setObjectName("actionupgrade_action")
        self.table_detective.addAction(self.actionupgrade_action)

        self.retranslateUi(Form_detective)
        QtCore.QMetaObject.connectSlotsByName(Form_detective)

    def retranslateUi(self, Form_detective):
        _translate = QtCore.QCoreApplication.translate
        Form_detective.setWindowTitle(_translate("Form_detective", "Раздел \"Детективы\""))
        self.search_line_detective.setPlaceholderText(_translate("Form_detective", "Введите название фильма"))
        self.search_btn_detective.setText(_translate("Form_detective", "Поиск"))
        item = self.table_detective.horizontalHeaderItem(0)
        item.setText(_translate("Form_detective", "Название фильма"))
        item = self.table_detective.horizontalHeaderItem(1)
        item.setText(_translate("Form_detective", "Страна производства"))
        item = self.table_detective.horizontalHeaderItem(2)
        item.setText(_translate("Form_detective", "Год выхода"))
        item = self.table_detective.horizontalHeaderItem(3)
        item.setText(_translate("Form_detective", "Возрастное ограничение"))
        item = self.table_detective.horizontalHeaderItem(4)
        item.setText(_translate("Form_detective", "Оценки"))
        self.actioninfo_action.setText(_translate("Form_detective", "Подробнее"))
        self.actioninfo_action.setShortcut(_translate("Form_detective", "Ctrl+I"))
        self.actionupgrade_action.setText(_translate("Form_detective", "Обновить"))
        self.actionupgrade_action.setShortcut(_translate("Form_detective", "Ctrl+U"))
