from PyQt5.QtWidgets import QDialogButtonBox

import sql_manager

from PyQt5.QtCore import QDate
from qtpy import QtWidgets
from ui.fixtransaction_dialog import Ui_Dialog
from datetime import datetime

fix_spendingHeader = "Fix Ausgaben Verwalten"
fix_incomeHeader = "Fix Einnahmen Verwalten"
fix_spendingList = ["Allgemein", "Versicherung", "Miete",
                    "Strom", "Kredit", "Verträge",
                    "Krankenkasse", "Finanzierung", "Mitgliedschaften",
                    "Spenden", "Haustiere", "Abos",
                    "Sonstiges"]
fix_incomeList = ["Gehalt", "Vermietung", "Familie",
                  "Nebenverdienst", "Sonstiges"]


class FixTransactionDialogManager(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
    from PyQt5.QtWidgets import QDialogButtonBox

import sql_manager

from PyQt5.QtCore import QDate
from qtpy import QtWidgets
from ui.fixtransaction_dialog import Ui_Dialog
from datetime import datetime

fix_spendingHeader = "Fix Ausgaben Verwalten"
fix_incomeHeader = "Fix Einnahmen Verwalten"
fix_spendingList = ["Allgemein", "Versicherung", "Miete",
                    "Strom", "Kredit", "Verträge",
                    "Krankenkasse", "Finanzierung", "Mitgliedschaften",
                    "Spenden", "Haustiere", "Abos",
                    "Sonstiges"]
fix_incomeList = ["Gehalt", "Vermietung", "Familie",
                  "Nebenverdienst", "Sonstiges"]


class FixTransactionDialogManager(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.dialog = QtWidgets.QDialog()
        self.is_spending = False

    def create_dialog(self, is_spending):
        self.ui.setupUi(self.dialog)
        self.is_spending = is_spending

        self.create_table()

        self.ui.doubleSpinBox_amount.valueChanged.connect(self.enable_add_button)
        self.ui.btn_add_element.clicked.connect(self.btn_add_pressed)

        if self.is_spending:
            self.ui.label_header.setText(fix_spendingHeader)
            self.set_combobox(fix_spendingList)
        else:
            self.ui.label_header.setText(fix_incomeHeader)
            self.set_combobox(fix_incomeList)

        self.dialog.setWindowTitle("Monatliche Fix-Transaktionen")
        self.dialog.show()
        self.dialog.exec_()

    def create_table(self):
        self.ui.tableWidget_fixtransaction.setRowCount(0)
        list_fixtransaction = sql_manager.get_fix_transaction_table_list()
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        list_fixtransaction.sort(key=lambda x: x[1])

        for row in list_fixtransaction:
            column = 0
            if self.is_spending and row[3] < 0:
                self.ui.tableWidget_fixtransaction.insertRow(column)

                self.ui.tableWidget_fixtransaction.setItem(column, 0, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.tableWidget_fixtransaction.setItem(column, 1, QtWidgets.QTableWidgetItem(str(row[2])))
                self.ui.tableWidget_fixtransaction.setItem(column, 2, QtWidgets.QTableWidgetItem(str(row[3])))

                column = +1

            if not self.is_spending and row[3] > 0:
                self.ui.tableWidget_fixtransaction.insertRow(column)

                self.ui.tableWidget_fixtransaction.setItem(column, 0, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.tableWidget_fixtransaction.setItem(column, 1, QtWidgets.QTableWidgetItem(str(row[2])))
                self.ui.tableWidget_fixtransaction.setItem(column, 2, QtWidgets.QTableWidgetItem(str(row[3])))

                column = +1

    def set_combobox(self, list_entries):
        self.ui.comboBox_category.clear()
        self.ui.comboBox_category.addItems(list_entries)

    def enable_delete_button(self):
        pass

    def btn_delete_pressed(self):
        pass

    def enable_add_button(self):
        if self.ui.doubleSpinBox_amount.value() > 0:
            self.ui.btn_add_element.setEnabled(True)
        else:
            self.ui.btn_add_element.setEnabled(False)

    def btn_add_pressed(self):
        date = self.ui.spinBox_date.value()
        category = self.ui.comboBox_category.currentText()
        amount = self.ui.doubleSpinBox_amount.value()

        if self.is_spending:
            sql_manager.insert_item_fix_transaction_table(date, category, -amount, "Fixausgabe")
        else:
            sql_manager.insert_item_fix_transaction_table(date, category, amount, "Fixeinnahme")

        self.create_table()