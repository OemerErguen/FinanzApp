from qtpy import QtWidgets

import sql_manager
from datetime import datetime
import operator


class FixTransaction:
    def __init__(self, label_fix_spending, label_fix_income):
        self.label_fix_spending = label_fix_spending
        self.label_fix_income = label_fix_income
        self.fix_spending_value = 0
        self.fix_income_value = 0

    def set_fix_transaction_values(self):
        list_fix_transaction = sql_manager.get_fix_transaction_table_list()

        for row in list_fix_transaction:
            if row[3] < 0:
                self.fix_spending_value += row[3]
            else:
                self.fix_income_value += row[3]

        self.label_fix_income.setText(str(self.fix_income_value))
        self.label_fix_spending.setText(str(self.fix_spending_value))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            from qtpy import QtWidgets

import sql_manager
from datetime import datetime
import operator


class FixTransaction:
    def __init__(self, label_fix_spending, label_fix_income):
        self.label_fix_spending = label_fix_spending
        self.label_fix_income = label_fix_income
        self.fix_spending_value = 0
        self.fix_income_value = 0

    def set_fix_transaction_values(self):
        list_fix_transaction = sql_manager.get_fix_transaction_table_list()

        for row in list_fix_transaction:
            if row[3] < 0:
                self.fix_spending_value += row[3]
            else:
                self.fix_income_value += row[3]

        self.label_fix_income.setText(str(self.fix_income_value))
        self.label_fix_spending.setText(str(self.fix_spending_value))