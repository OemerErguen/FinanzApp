# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_headerMain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_headerMain.setFont(font)
        self.label_headerMain.setObjectName("label_headerMain")
        self.verticalLayout_3.addWidget(self.label_headerMain)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_headerTable = QtWidgets.QLabel(self.centralwidget)
        self.label_headerTable.setObjectName("label_headerTable")
        self.verticalLayout_2.addWidget(self.label_headerTable)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.tableWidget_overview = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_overview.setMinimumSize(QtCore.QSize(420, 0))
        self.tableWidget_overview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_overview.setObjectName("tableWidget_overview")
        self.tableWidget_overview.setColumnCount(4)
        self.tableWidget_overview.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_overview)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_headerGeneralOverview = QtWidgets.QLabel(self.centralwidget)
        self.label_headerGeneralOverview.setObjectName("label_headerGeneralOverview")
        self.verticalLayout.addWidget(self.label_headerGeneralOverview)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_timePeriod = QtWidgets.QLabel(self.centralwidget)
        self.label_timePeriod.setObjectName("label_timePeriod")
        self.gridLayout.addWidget(self.label_timePeriod, 0, 0, 1, 1)
        self.label_monthlySpendings = QtWidgets.QLabel(self.centralwidget)
        self.label_monthlySpendings.setObjectName("label_monthlySpendings")
        self.gridLayout.addWidget(self.label_monthlySpendings, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        self.et_monthlySpendings = QtWidgets.QLabel(self.centralwidget)
        self.et_monthlySpendings.setObjectName("et_monthlySpendings")
        self.gridLayout.addWidget(self.et_monthlySpendings, 4, 1, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 1, 2, 1, 1)
        self.label_currentBalance = QtWidgets.QLabel(self.centralwidget)
        self.label_currentBalance.setObjectName("label_currentBalance")
        self.gridLayout.addWidget(self.label_currentBalance, 1, 0, 1, 1)
        self.et_monthlyIncome = QtWidgets.QLabel(self.centralwidget)
        self.et_monthlyIncome.setObjectName("et_monthlyIncome")
        self.gridLayout.addWidget(self.et_monthlyIncome, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 2, 1, 1)
        self.label_fixSpendings = QtWidgets.QLabel(self.centralwidget)
        self.label_fixSpendings.setObjectName("label_fixSpendings")
        self.gridLayout.addWidget(self.label_fixSpendings, 2, 0, 1, 1)
        self.et_fixIncome = QtWidgets.QLabel(self.centralwidget)
        self.et_fixIncome.setObjectName("et_fixIncome")
        self.gridLayout.addWidget(self.et_fixIncome, 3, 1, 1, 1)
        self.label_fixIncome = QtWidgets.QLabel(self.centralwidget)
        self.label_fixIncome.setObjectName("label_fixIncome")
        self.gridLayout.addWidget(self.label_fixIncome, 3, 0, 1, 1)
        self.btn_manageMonthlySpendings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageMonthlySpendings.setObjectName("btn_manageMonthlySpendings")
        self.gridLayout.addWidget(self.btn_manageMonthlySpendings, 4, 2, 1, 1)
        self.et_balanceEdit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.et_balanceEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.et_balanceEdit.setMinimum(-999999999.0)
        self.et_balanceEdit.setMaximum(999999999.0)
        self.et_balanceEdit.setProperty("value", 1000.0)
        self.et_balanceEdit.setObjectName("et_balanceEdit")
        self.gridLayout.addWidget(self.et_balanceEdit, 1, 1, 1, 1)
        self.et_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.et_dateEdit.setFrame(True)
        self.et_dateEdit.setReadOnly(True)
        self.et_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.et_dateEdit.setAccelerated(False)
        self.et_dateEdit.setKeyboardTracking(True)
        self.et_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 11, 1), QtCore.QTime(0, 0, 0)))
        self.et_dateEdit.setMaximumDate(QtCore.QDate(2100, 12, 1))
        self.et_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.et_dateEdit.setCalendarPopup(False)
        self.et_dateEdit.setDate(QtCore.QDate(2019, 10, 1))
        self.et_dateEdit.setObjectName("et_dateEdit")
        self.gridLayout.addWidget(self.et_dateEdit, 0, 1# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_headerMain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_headerMain.setFont(font)
        self.label_headerMain.setObjectName("label_headerMain")
        self.verticalLayout_3.addWidget(self.label_headerMain)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_headerTable = QtWidgets.QLabel(self.centralwidget)
        self.label_headerTable.setObjectName("label_headerTable")
        self.verticalLayout_2.addWidget(self.label_headerTable)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.tableWidget_overview = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_overview.setMinimumSize(QtCore.QSize(420, 0))
        self.tableWidget_overview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_overview.setObjectName("tableWidget_overview")
        self.tableWidget_overview.setColumnCount(4)
        self.tableWidget_overview.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_overview.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_overview)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_headerGeneralOverview = QtWidgets.QLabel(self.centralwidget)
        self.label_headerGeneralOverview.setObjectName("label_headerGeneralOverview")
        self.verticalLayout.addWidget(self.label_headerGeneralOverview)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_timePeriod = QtWidgets.QLabel(self.centralwidget)
        self.label_timePeriod.setObjectName("label_timePeriod")
        self.gridLayout.addWidget(self.label_timePeriod, 0, 0, 1, 1)
        self.label_monthlySpendings = QtWidgets.QLabel(self.centralwidget)
        self.label_monthlySpendings.setObjectName("label_monthlySpendings")
        self.gridLayout.addWidget(self.label_monthlySpendings, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        self.et_monthlySpendings = QtWidgets.QLabel(self.centralwidget)
        self.et_monthlySpendings.setObjectName("et_monthlySpendings")
        self.gridLayout.addWidget(self.et_monthlySpendings, 4, 1, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 1, 2, 1, 1)
        self.label_currentBalance = QtWidgets.QLabel(self.centralwidget)
        self.label_currentBalance.setObjectName("label_currentBalance")
        self.gridLayout.addWidget(self.label_currentBalance, 1, 0, 1, 1)
        self.et_monthlyIncome = QtWidgets.QLabel(self.centralwidget)
        self.et_monthlyIncome.setObjectName("et_monthlyIncome")
        self.gridLayout.addWidget(self.et_monthlyIncome, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 2, 1, 1)
        self.label_fixSpendings = QtWidgets.QLabel(self.centralwidget)
        self.label_fixSpendings.setObjectName("label_fixSpendings")
        self.gridLayout.addWidget(self.label_fixSpendings, 2, 0, 1, 1)
        self.et_fixIncome = QtWidgets.QLabel(self.centralwidget)
        self.et_fixIncome.setObjectName("et_fixIncome")
        self.gridLayout.addWidget(self.et_fixIncome, 3, 1, 1, 1)
        self.label_fixIncome = QtWidgets.QLabel(self.centralwidget)
        self.label_fixIncome.setObjectName("label_fixIncome")
        self.gridLayout.addWidget(self.label_fixIncome, 3, 0, 1, 1)
        self.btn_manageMonthlySpendings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageMonthlySpendings.setObjectName("btn_manageMonthlySpendings")
        self.gridLayout.addWidget(self.btn_manageMonthlySpendings, 4, 2, 1, 1)
        self.et_balanceEdit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.et_balanceEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.et_balanceEdit.setMinimum(-999999999.0)
        self.et_balanceEdit.setMaximum(999999999.0)
        self.et_balanceEdit.setProperty("value", 1000.0)
        self.et_balanceEdit.setObjectName("et_balanceEdit")
        self.gridLayout.addWidget(self.et_balanceEdit, 1, 1, 1, 1)
        self.et_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.et_dateEdit.setFrame(True)
        self.et_dateEdit.setReadOnly(True)
        self.et_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.et_dateEdit.setAccelerated(False)
        self.et_dateEdit.setKeyboardTracking(True)
        self.et_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 11, 1), QtCore.QTime(0, 0, 0)))
        self.et_dateEdit.setMaximumDate(QtCore.QDate(2100, 12, 1))
        self.et_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.et_dateEdit.setCalendarPopup(False)
        self.et_dateEdit.setDate(QtCore.QDate(2019, 10, 1))
        self.et_dateEdit.setObjectName("et_dateEdit")
        self.gridLayout.addWidget(self.et_dateEdit, 0, 1, 1, 1)
        self.btn_manageFixIncome = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageFixIncome.setObjectName("btn_manageFixIncome")
        self.gridLayout.addWidget(self.btn_manageFixIncome, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)
        self.label_monthlyIncome = QtWidgets.QLabel(self.centralwidget)
        self.label_monthlyIncome.setObjectName("label_monthlyIncome")
        self.gridLayout.addWidget(self.label_monthlyIncome, 5, 0, 1, 1)
        self.label_endBalance = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_endBalance.setFont(font)
        self.label_endBalance.setObjectName("label_endBalance")
        self.gridLayout.addWidget(self.label_endBalance, 8, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_monthBackwards = QtWidgets.QPushButton(self.centralwidget)
        self.btn_monthBackwards.setObjectName("btn_monthBackwards")
        self.horizontalLayout.addWidget(self.btn_monthBackwards)
        self.btn_monthForwards = QtWidgets.QPushButton(self.centralwidget)
        self.btn_monthForwards.setObjectName("btn_monthForwards")
        self.horizontalLayout.addWidget(self.btn_monthForwards)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.et_fixSpendings = QtWidgets.QLabel(self.centralwidget)
        self.et_fixSpendings.setObjectName("et_fixSpendings")
        self.gridLayout.addWidget(self.et_fixSpendings, 2, 1, 1, 1)
        self.btn_manageFixSpendings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageFixSpendings.setObjectName("btn_manageFixSpendings")
        self.gridLayout.addWidget(self.btn_manageFixSpendings, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 1, 1, 1)
        self.btn_manageMonthlyIncome = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageMonthlyIncome.setObjectName("btn_manageMonthlyIncome")
        self.gridLayout.addWidget(self.btn_manageMonthlyIncome, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 7, 0, 1, 1)
        self.et_endBalance = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.et_endBalance.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.et_endBalance.setReadOnly(True)
        self.et_endBalance.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.et_endBalance.setMinimum(-1000000.0)
        self.et_endBalance.setMaximum(1000000.0)
        self.et_endBalance.setProperty("value", 0.0)
        self.et_endBalance.setObjectName("et_endBalance")
        self.gridLayout.addWidget(self.et_endBalance, 8, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_newSpending = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_newSpending.setFont(font)
        self.btn_newSpending.setAutoFillBackground(False)
        self.btn_newSpending.setStyleSheet("background-color: rgb(255, 75, 69);\n"
"selection-background-color: rgb(255, 0, 0);")
        self.btn_newSpending.setObjectName("btn_newSpending")
        self.horizontalLayout_4.addWidget(self.btn_newSpending)
        self.btn_newIncome = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_newIncome.setFont(font)
        self.btn_newIncome.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"selection-background-color: rgb(0, 85, 0);")
        self.btn_newIncome.setObjectName("btn_newIncome")
        self.horizontalLayout_4.addWidget(self.btn_newIncome)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_headerDiagramms = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_headerDiagramms.setFont(font)
        self.label_headerDiagramms.setObjectName("label_headerDiagramms")
        self.verticalLayout_3.addWidget(self.label_headerDiagramms)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(50, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3.addWidget(self.widget)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_3.addWidget(self.line_6)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
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
        self.label_headerMain.setText(_translate("MainWindow", "Finanzübersicht"))
        self.label_headerTable.setText(_translate("MainWindow", "Monatsverlauf"))
        item = self.tableWidget_overview.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Datum"))
        item = self.tableWidget_overview.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kategorie"))
        item = self.tableWidget_overview.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Betrag"))
        item = self.tableWidget_overview.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Typ"))
        self.label_headerGeneralOverview.setText(_translate("MainWindow", "Gesamtübersicht"))
        self.label_timePeriod.setText(_translate("MainWindow", "Zeitraum (MM.JJJJ)"))
        self.label_monthlySpendings.setText(_translate("MainWindow", "Monatsausgaben"))
        self.et_monthlySpendings.setText(_translate("MainWindow", "TextLabel"))
        self.btn_update.setText(_translate("MainWindow", "Aktuallisieren"))
        self.label_currentBalance.setText(_translate("MainWindow", "Kontostand Anfang des Monats"))
        self.et_monthlyIncome.setText(_translate("MainWindow", "TextLabel"))
        self.label_fixSpendings.setText(_translate("MainWindow", "Fixausgaben"))
        self.et_fixIncome.setText(_translate("MainWindow", "TextLabel"))
        self.label_fixIncome.setText(_translate("MainWindow", "Fixeinnahmen"))
        self.btn_manageMonthlySpendings.setText(_translate("MainWindow", "Nicht implementiert"))
        self.et_dateEdit.setDisplayFormat(_translate("MainWindow", "MMM.yyyy"))
        self.btn_manageFixIncome.setText(_translate("MainWindow", "Verwalten"))
        self.label_monthlyIncome.setText(_translate("MainWindow", "Monatseinnahmen"))
        self.label_endBalance.setText(_translate("MainWindow", "Kontostand (Ende des Monats)"))
        self.btn_monthBackwards.setText(_translate("MainWindow", "<"))
        self.btn_monthForwards.setText(_translate("MainWindow", ">"))
        self.et_fixSpendings.setText(_translate("MainWindow", "TextLabel"))
        self.btn_manageFixSpendings.setText(_translate("MainWindow", "Verwalten"))
        self.btn_manageMonthlyIncome.setText(_translate("MainWindow", "Nicht implementiert"))
        self.btn_newSpending.setText(_translate("MainWindow", "Neue Ausgabe"))
        self.btn_newIncome.setText(_translate("MainWindow", "Neue Einnahme"))
        self.label_headerDiagramms.setText(_translate("MainWindow", "Diagramme (nicht implementiert)"))
