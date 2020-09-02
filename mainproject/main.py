import sys
import sql_manager

from qtpy import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from ui.mainwindow import Ui_MainWindow
from transaction_dialog_manager import TransactionDialogManager
from fix_transaction_dialog_manager import FixTransactionDialogManager
from transaction import Transaction
from fix_transaction import FixTransaction
from balance import Balance
from calculator import Calculator


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.currentDate = QDate.currentDate()
        self.currentBalance = self.ui.et_balanceEdit.text()

        self.ui.btn_monthBackwards.clicked.connect(self.btn_month_backwards_clicked)
        self.ui.btn_monthForwards.clicked.connect(self.btn_month_forwards_clicked)
        self.ui.btn_update.clicked.connect(self.btn_update_clicked)
        self.ui.btn_newIncome.clicked.connect(self.btn_new_income_clicked)
        self.ui.btn_newSpending.clicked.connect(self.btn_new_spending_clicked)
        self.ui.btn_manageFixSpendings.clicked.connect(self.btn_manage_fix_spending_clicked)
        self.ui.btn_manageFixIncome.clicked.connect(self.btn_manage_fix_income_clicked)

    def create_main_window(self):
        self.set_current_date()
        self.set_current_balance()
        self.refresh_fix_transactions()
        self.refresh_balance()

    def refresh_table(self):
        table = Transaction(self.ui.tableWidget_overview, self.ui.et_monthlySpendings, self.ui.et_monthlyIncome)
        table.create_table(str(self.ui.et_dateEdit.date().toPyDate()))


    def refresh_balance(self):
        calculator = Calculator(self.ui.et_fixSpendings, self.ui.et_fixIncome, self.ui.et_monthlySpendings,
                          self.ui.et_monthlyIncome, self.ui.et_endBalance, self.currentDate)
        calculator.calculate_balance()

    def refresh_fix_transactions(self):
        fix_transactions = FixTransaction(self.ui.et_fixSpendings, self.ui.et_fixIncome)
        fix_transactions.set_fix_transaction_values()

    def set_current_balance(self):
        balance = Balance(self.ui.label_currentBalance, self.ui.et_balanceEdit)
        balance.get_balance(str(self.ui.et_dateEdit.date().toPyDate()))

    def btn_update_clicked(self):
        self.currentBalance = self.ui.et_balanceEdit.text()
        print("Current Balance is:" + self.currentBalance)
        balance = Balance(self.ui.label_currentBalance, self.ui.et_balanceEdit)
        balance.set_balance(str(self.ui.et_dateEdit.date().toPyDate()))
        self.refresh_balance()

    def set_current_date(self):
        self.ui.et_dateEdit.setDate(self.currentDate)
        print("Date is set to: " + str(self.ui.et_dateEdit.date().toPyDate()))
        self.refresh_table()

    def btn_month_forwards_clicked(self):
        if self.currentDate >= QDate.currentDate().addYears(3):
            self.ui.btn_monthForwards.setDisabled(True)
        self.currentDate = self.currentDate.addMonths(1)
        self.ui.btn_monthBackwards.setDisabled(False)
        self.set_current_date()

    def btn_month_backwards_clicked(self):
        if self.currentDate <= QDate.currentDate().addYears(-1):
            self.ui.btn_monthBackwards.setDisabled(True)
        self.currentDate = self.currentDate.addMonths(-1)
        self.ui.btn_monthForwards.setDisabled(False)
        self.set_current_date()

    def btn_new_income_clicked(self):
        # TransactionWidget().create_dialog(False)
        dialog = TransactionDialogManager(self)
        dialog.create_dialog(False)
        self.refresh_table()
        self.refresh_table()
        self.refresh_balance()

    def btn_new_spending_clicked(self):
        dialog = TransactionDialogManager(self)
        dialog.create_dialog(True)
 import sys
import sql_manager

from qtpy import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from ui.mainwindow import Ui_MainWindow
from transaction_dialog_manager import TransactionDialogManager
from fix_transaction_dialog_manager import FixTransactionDialogManager
from transaction import Transaction
from fix_transaction import FixTransaction
from balance import Balance
from calculator import Calculator


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.currentDate = QDate.currentDate()
        self.currentBalance = self.ui.et_balanceEdit.text()

        self.ui.btn_monthBackwards.clicked.connect(self.btn_month_backwards_clicked)
        self.ui.btn_monthForwards.clicked.connect(self.btn_month_forwards_clicked)
        self.ui.btn_update.clicked.connect(self.btn_update_clicked)
        self.ui.btn_newIncome.clicked.connect(self.btn_new_income_clicked)
        self.ui.btn_newSpending.clicked.connect(self.btn_new_spending_clicked)
        self.ui.btn_manageFixSpendings.clicked.connect(self.btn_manage_fix_spending_clicked)
        self.ui.btn_manageFixIncome.clicked.connect(self.btn_manage_fix_income_clicked)

    def create_main_window(self):
        self.set_current_date()
        self.set_current_balance()
        self.refresh_fix_transactions()
        self.refresh_balance()

    def refresh_table(self):
        table = Transaction(self.ui.tableWidget_overview, self.ui.et_monthlySpendings, self.ui.et_monthlyIncome)
        table.create_table(str(self.ui.et_dateEdit.date().toPyDate()))


    def refresh_balance(self):
        calculator = Calculator(self.ui.et_fixSpendings, self.ui.et_fixIncome, self.ui.et_monthlySpendings,
                          self.ui.et_monthlyIncome, self.ui.et_endBalance, self.currentDate)
        calculator.calculate_balance()

    def refresh_fix_transactions(self):
        fix_transactions = FixTransaction(self.ui.et_fixSpendings, self.ui.et_fixIncome)
        fix_transactions.set_fix_transaction_values()

    def set_current_balance(self):
        balance = Balance(self.ui.label_currentBalance, self.ui.et_balanceEdit)
        balance.get_balance(str(self.ui.et_dateEdit.date().toPyDate()))

    def btn_update_clicked(self):
        self.currentBalance = self.ui.et_balanceEdit.text()
        print("Current Balance is:" + self.currentBalance)
        balance = Balance(self.ui.label_currentBalance, self.ui.et_balanceEdit)
        balance.set_balance(str(self.ui.et_dateEdit.date().toPyDate()))
        self.refresh_balance()

    def set_current_date(self):
        self.ui.et_dateEdit.setDate(self.currentDate)
        print("Date is set to: " + str(self.ui.et_dateEdit.date().toPyDate()))
        self.refresh_table()

    def btn_month_forwards_clicked(self):
        if self.currentDate >= QDate.currentDate().addYears(3):
            self.ui.btn_monthForwards.setDisabled(True)
        self.currentDate = self.currentDate.addMonths(1)
        self.ui.btn_monthBackwards.setDisabled(False)
        self.set_current_date()

    def btn_month_backwards_clicked(self):
        if self.currentDate <= QDate.currentDate().addYears(-1):
            self.ui.btn_monthBackwards.setDisabled(True)
        self.currentDate = self.currentDate.addMonths(-1)
        self.ui.btn_monthForwards.setDisabled(False)
        self.set_current_date()

    def btn_new_income_clicked(self):
        # TransactionWidget().create_dialog(False)
        dialog = TransactionDialogManager(self)
        dialog.create_dialog(False)
        self.refresh_table()
        self.refresh_table()
        self.refresh_balance()

    def btn_new_spending_clicked(self):
        dialog = TransactionDialogManager(self)
        dialog.create_dialog(True)
        self.refresh_table()
        self.refresh_table()
        self.refresh_balance()

    def btn_manage_fix_spending_clicked(self):
        dialog = FixTransactionDialogManager(self)
        dialog.create_dialog(True)
        self.refresh_table()
        self.refresh_fix_transactions()
        self.refresh_balance()

    def btn_manage_fix_income_clicked(self):
        dialog = FixTransactionDialogManager(self)
        dialog.create_dialog(False)
        self.refresh_table()
        self.refresh_fix_transactions()
        self.refresh_balance()


app = QtWidgets.QApplication(sys.argv)
sql_manager.create_transaction_table()
sql_manager.create_fix_transaction_table()
window = MainWindow()
window.setWindowTitle("FinanzApp")
window.create_main_window()
window.show()
sys.exit(app.exec_())
