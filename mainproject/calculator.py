from qtpy import uic

# transforms ui files into py files
uic.compileUiDir("ui")from qtpy import QtWidgets

import sql_manager
from datetime import datetime


def get_correct_float_value(x):
    return float(x.replace(',', '.'))


class Calculator:
    def __init__(self, et_fixSpendings, et_fixIncome, et_monthlySpendings,
                 et_monthlyIncome, et_endBalance, currentDate):
        self.et_fix_spending = et_fixSpendings
        self.et_fix_income = et_fixIncome
        self.et_monthly_spending = et_monthlySpendings
        self.et_monthly_income = et_monthlyIncome
        self.et_end_balance = et_endBalance
        self.current_date = currentDate

    def calculate_balance(self):
        balance_entry = sql_manager.get_balance_entry()
        balance = balance_entry[0][2]
        balance_difference = 0
        balance_end_of_month = 0

        for element in self.get_transaction_list():
            balance_difference += get_correct_float_value(element)

        balance_end_of_month = get_correct_float_value(balance) + balance_difference

        self.et_end_balance.setValue(balance_end_of_month)


    def get_transaction_list(self):
        temp_list = [self.et_fix_spending.text(), self.et_fix_income.text(),
                     self.et_monthly_spending.text(), self.et_monthly_income.text()]
        return temp_list
