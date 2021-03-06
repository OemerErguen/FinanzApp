from qtpy import QtWidgets

import sql_manager
from datetime import datetime
import operator


class Transaction:
    def __init__(self, table_widget, label_spending, label_income):
        self.table_widget = table_widget
        self.label_spending = label_spending
        self.label_income = label_income
        self.spending_value = 0
        self.income_value = 0

    def create_table(self, selected_date):
        datetime_object = datetime.strptime(selected_date, '%Y-%m-%d').date()
        self.table_widget.setRowCount(0)

        self.spending_value = 0
        self.income_value = 0

        list_transaction = sql_manager.get_transaction_table_list()
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        list_transaction.sort(key=lambda x: x[1])

        for row in list_transaction:
            entry_date = datetime.strptime(row[1], '%Y-%m-%d')

            if datetime_object.month == entry_date.month and datetime_object.year == entry_date.year:
                if row[3]< 0:
                    self.spending_value += row[3]
                else:
                    self.income_value += row[3]

            if datetime_object.month == entry_date.month and datetime_object.year == entry_date.year:
                column = 0
                self.table_widget.insertRow(column)

                self.table_widget.setItem(column, 0, QtWidgets.QTableWidgetItem(str(row[1])))
                self.table_widget.setItem(column, 1, QtWidgets.QTableWidgetItem(str(row[2])))
                self.table_widget.setItem(column, 2, QtWidgets.QTableWidgetItem(str(row[3])))
                self.table_widget.setItem(column, 3, QtWidgets.QTableWidgetItem(str(row[4])))

                column = +1

        self.label_spending.setText(str(self.spending_value))
        self.label_income.setText(str(self.income_value))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          from qtpy import QtWidgets

import sql_manager
from datetime import datetime
import operator


class Transaction:
    def __init__(self, table_widget, label_spending, label_income):
        self.table_widget = table_widget
        self.label_spending = label_spending
        self.label_income = label_income
        self.spending_value = 0
        self.income_value = 0

    def create_table(self, selected_date):
        datetime_object = datetime.strptime(selected_date, '%Y-%m-%d').date()
        self.table_widget.setRowCount(0)

        self.spending_value = 0
        self.income_value = 0

        list_transaction = sql_manager.get_transaction_table_list()
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        list_transaction.sort(key=lambda x: x[1])

        for row in list_transaction:
            entry_date = datetime.strptime(row[1], '%Y-%m-%d')

            if datetime_object.month == entry_date.month and datetime_object.year == entry_date.year:
                if row[3]< 0:
                    self.spending_value += row[3]
                else:
                    self.income_value += row[3]

            if datetime_object.month == entry_date.month and datetime_object.year == entry_date.year:
                column = 0
                self.table_widget.insertRow(column)

                self.table_widget.setItem(column, 0, QtWidgets.QTableWidgetItem(str(row[1])))
                self.table_widget.setItem(column, 1, QtWidgets.QTableWidgetItem(str(row[2])))
                self.table_widget.setItem(column, 2, QtWidgets.QTableWidgetItem(str(row[3])))
                self.table_widget.setItem(column, 3, QtWidgets.QTableWidgetItem(str(row[4])))

                column = +1

        self.label_spending.setText(str(self.spending_value))
        self.label_income.setText(str(self.income_value))