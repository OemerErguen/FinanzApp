# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\fixtransaction_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 412)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.verticalLayout.addWidget(self.label_header)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_tableoverview = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_tableoverview.setFont(font)
        self.label_tableoverview.setObjectName("label_tableoverview")
        self.verticalLayout.addWidget(self.label_tableoverview)
        self.tableWidget_fixtransaction = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_fixtransaction.setObjectName("tableWidget_fixtransaction")
        self.tableWidget_fixtransaction.setColumnCount(3)
        self.tableWidget_fixtransaction.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget_fixtransaction)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setEnabled(False)
        self.btn_delete.setObjectName("btn_delete")
        self.hori# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\fixtransaction_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 412)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.verticalLayout.addWidget(self.label_header)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_tableoverview = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_tableoverview.setFont(font)
        self.label_tableoverview.setObjectName("label_tableoverview")
        self.verticalLayout.addWidget(self.label_tableoverview)
        self.tableWidget_fixtransaction = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_fixtransaction.setObjectName("tableWidget_fixtransaction")
        self.tableWidget_fixtransaction.setColumnCount(3)
        self.tableWidget_fixtransaction.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fixtransaction.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget_fixtransaction)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setEnabled(False)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_newentry = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_newentry.setFont(font)
        self.label_newentry.setObjectName("label_newentry")
        self.verticalLayout.addWidget(self.label_newentry)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_amount = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.gridLayout.addWidget(self.label_amount, 0, 2, 1, 1)
        self.label_date = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 0, 0, 1, 1)
        self.doubleSpinBox_amount = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_amount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_amount.setMaximum(1000000.0)
        self.doubleSpinBox_amount.setObjectName("doubleSpinBox_amount")
        self.gridLayout.addWidget(self.doubleSpinBox_amount, 1, 2, 1, 1)
        self.label_category = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setObjectName("label_category")
        self.gridLayout.addWidget(self.label_category, 0, 1, 1, 1)
        self.comboBox_category = QtWidgets.QComboBox(Dialog)
        self.comboBox_category.setObjectName("comboBox_category")
        self.gridLayout.addWidget(self.comboBox_category, 1, 1, 1, 1)
        self.spinBox_date = QtWidgets.QSpinBox(Dialog)
        self.spinBox_date.setMinimum(1)
        self.spinBox_date.setMaximum(31)
        self.spinBox_date.setObjectName("spinBox_date")
        self.gridLayout.addWidget(self.spinBox_date, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_add_element = QtWidgets.QPushButton(Dialog)
        self.btn_add_element.setEnabled(False)
        self.btn_add_element.setStyleSheet("")
        self.btn_add_element.setObjectName("btn_add_element")
        self.horizontalLayout_2.addWidget(self.btn_add_element)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_header.setText(_translate("Dialog", "Header"))
        self.label_tableoverview.setText(_translate("Dialog", "Übersicht"))
        item = self.tableWidget_fixtransaction.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Buchungsdatum"))
        item = self.tableWidget_fixtransaction.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Kategorie"))
        item = self.tableWidget_fixtransaction.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Betrag"))
        self.btn_delete.setText(_translate("Dialog", "Löschen"))
        self.label_newentry.setText(_translate("Dialog", "Neuer Eintrag"))
        self.label_amount.setText(_translate("Dialog", "Betrag"))
        self.label_date.setText(_translate("Dialog", "Buchungsdatum (Mitte des Monats: 15)"))
        self.label_category.setText(_translate("Dialog", "Kategorie"))
        self.btn_add_element.setText(_translate("Dialog", "Hinzufügen"))
