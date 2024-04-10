"""Модуль виджета таблицы бюджета"""
from PySide6 import QtWidgets


class BudgetTable(QtWidgets.QTableWidget):
    """Класс виджета таблицы бюджета"""
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet('background-color: #CCFFCC; font-size: 12pt')

        column = ['Текущие расходы', 'Бюджет на период']
        row = ['День', 'Неделя', 'Месяц']

        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setFixedHeight(100)
        self.setColumnCount(len(column))
        self.setRowCount(len(row))
        self.setHorizontalHeaderLabels(column)
        self.setVerticalHeaderLabels(row)
        self.verticalHeader()\
            .setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader()\
            .setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader()\
            .setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader()\
            .setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader()\
            .setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)


class BudgetWidget(QtWidgets.QWidget):
    """Класс виджета интерфейса бюджета расходов"""
    def __init__(self) -> None:
        super().__init__()

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self.table_widget = BudgetTable()
        layout.addWidget(self.table_widget, 0, 0, 1, 3)

        self.edit_button = QtWidgets.QPushButton("Добавить бюджет")
        layout.addWidget(QtWidgets.QLabel("Введите бюджет"), 1, 0)
        layout.addWidget(self.edit_button, 1, 2)

        self.edit_box = QtWidgets.QLineEdit()
        layout.addWidget(self.edit_box, 1, 1)

    def set_data(self, data: list[str], column: int = 1) -> None:
        """Функция для записи данных в таблицу"""
        for j, sums in enumerate(data):
            self.table_widget.setItem(j, column, QtWidgets.QTableWidgetItem(sums))
