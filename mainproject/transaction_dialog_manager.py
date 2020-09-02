from PyQt5.QtWidgets import QDialogButtonBox

import sql_manager

from PyQt5.QtCore import QDate
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from transaction import Transaction
from ui.transactionDialogWindow import Ui_Dialog

spendingHeader = "Neue Ausgabe"
incomeHeader = "Neue Einnahme"
spendingList = ["Allgemein", "Kleidung", "Lebensmittel",
                "Kleidersachen", "Miete", "Haus",
                "Versicherung", "Gesungheit", "Reisen",
                "Freizeit", "Haustiere", "Bücher",
                "Ausflüge", "Geschenke", "Strom/Wasser",
                "Tanken", "Auto", "Schule",
                "Sport", "Musik", "Freunde", "Sonstiges"]
incomeList = ["Gehalt", "Vermietung", "Geschenk",
              "Familie", "Nebenverdienst", "Sonstiges"]


class TransactionDialogManager(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.dialog = QtWidgets.QDialog()
        self.is_spending = False

    def create_dialog(self, is_spending):
        self.ui.setupUi(self.dialog)
        self.is_spending = is_spending
        self.set_current_date()
        self.enable_ok_button()
        self.ui.doubleSpinBox_balance.valueChanged.connect(self.enable_ok_button)

        if self.is_spending:
            self.ui.label_header.setText(spendingHeader)
            self.set_combobox(spendingList)
        else:
            self.ui.label_header.setText(incomeHeader)
            self.set_combobox(incomeList)

        self.ui.buttonBox.accepted.connect(self.btn_ok_pressed)

        self.dialog.setWindowTitle("Transaktion")
        self.dialog.show()
        self.dialog.exec_()

    def set_combobox(self, list_entries):
        self.ui.comboBox_category.clear()
        self.ui.comboBox_category.addItems(list_entries)

    def set_current_date(self):
        self.uifrom PyQt5.QtWidgets import QDialogButtonBox

import sql_manager

from PyQt5.QtCore import QDate
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from transaction import Transaction
from ui.transactionDialogWindow import Ui_Dialog

spendingHeader = "Neue Ausgabe"
incomeHeader = "Neue Einnahme"
spendingList = ["Allgemein", "Kleidung", "Lebensmittel",
                "Kleidersachen", "Miete", "Haus",
                "Versicherung", "Gesungheit", "Reisen",
                "Freizeit", "Haustiere", "Bücher",
                "Ausflüge", "Geschenke", "Strom/Wasser",
                "Tanken", "Auto", "Schule",
                "Sport", "Musik", "Freunde", "Sonstiges"]
incomeList = ["Gehalt", "Vermietung", "Geschenk",
              "Familie", "Nebenverdienst", "Sonstiges"]


class TransactionDialogManager(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.dialog = QtWidgets.QDialog()
        self.is_spending = False

    def create_dialog(self, is_spending):
        self.ui.setupUi(self.dialog)
        self.is_spending = is_spending
        self.set_current_date()
        self.enable_ok_button()
        self.ui.doubleSpinBox_balance.valueChanged.connect(self.enable_ok_button)

        if self.is_spending:
            self.ui.label_header.setText(spendingHeader)
            self.set_combobox(spendingList)
        else:
            self.ui.label_header.setText(incomeHeader)
            self.set_combobox(incomeList)

        self.ui.buttonBox.accepted.connect(self.btn_ok_pressed)

        self.dialog.setWindowTitle("Transaktion")
        self.dialog.show()
        self.dialog.exec_()

    def set_combobox(self, list_entries):
        self.ui.comboBox_category.clear()
        self.ui.comboBox_category.addItems(list_entries)

    def set_current_date(self):
        self.ui.dateEdit_date.setDate(QDate.currentDate())

    def enable_ok_button(self):
        if self.ui.doubleSpinBox_balance.value() > 0:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def btn_ok_pressed(self):
        date = self.ui.dateEdit_date.date().toPyDate()
        category = self.ui.comboBox_category.currentText()
        amount = self.ui.doubleSpinBox_balance.value()

        if self.is_spending:
            sql_manager.insert_item_transaction_table(date, category, -amount, "Ausgabe")
        else:
            sql_manager.insert_item_transaction_table(date, category, amount, "Einnahme")
