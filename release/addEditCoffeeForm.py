# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AddingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(80, 310, 75, 23))
        self.button_add.setObjectName("button_add")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.cancel.setObjectName("cancel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 331, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_sort = QtWidgets.QComboBox(self.layoutWidget)
        self.name_sort.setObjectName("name_sort")
        self.verticalLayout_2.addWidget(self.name_sort)
        self.stepen_obzharki = QtWidgets.QComboBox(self.layoutWidget)
        self.stepen_obzharki.setObjectName("stepen_obzharki")
        self.stepen_obzharki.addItem("")
        self.stepen_obzharki.addItem("")
        self.stepen_obzharki.addItem("")
        self.verticalLayout_2.addWidget(self.stepen_obzharki)
        self.molot = QtWidgets.QComboBox(self.layoutWidget)
        self.molot.setObjectName("molot")
        self.molot.addItem("")
        self.molot.addItem("")
        self.verticalLayout_2.addWidget(self.molot)
        self.opisanie = QtWidgets.QLineEdit(self.layoutWidget)
        self.opisanie.setObjectName("opisanie")
        self.verticalLayout_2.addWidget(self.opisanie)
        self.cena = QtWidgets.QSpinBox(self.layoutWidget)
        self.cena.setObjectName("cena")
        self.verticalLayout_2.addWidget(self.cena)
        self.obem = QtWidgets.QSpinBox(self.layoutWidget)
        self.obem.setObjectName("obem")
        self.verticalLayout_2.addWidget(self.obem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/В зернах"))
        self.label_4.setText(_translate("MainWindow", "Описание"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объём"))
        self.stepen_obzharki.setItemText(0, _translate("MainWindow", "Светлая"))
        self.stepen_obzharki.setItemText(1, _translate("MainWindow", "Тёмная"))
        self.stepen_obzharki.setItemText(2, _translate("MainWindow", "Средняя"))
        self.molot.setItemText(0, _translate("MainWindow", "Молотый"))
        self.molot.setItemText(1, _translate("MainWindow", "В зернах"))