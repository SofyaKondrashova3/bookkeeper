"""Модуль виджета редактирования категорий и записей о расходах"""
from PySide6 import QtWidgets, QtCore


class AddExpensesWidget(QtWidgets.QWidget):
    """Класс виджета таблицы бюджета"""
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet('background-color: #CCFFCC; color: #0000CC; font-size: 12pt')

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QtWidgets.QLabel("Стоимость"), 0, 0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QtWidgets.QLabel("Название объкта"), 1, 0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QtWidgets.QLabel("Категория объекта"), 2, 0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QtWidgets.QLabel("Дата покупки"), 3, 0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QtWidgets.QLabel("Новая категория"), 5, 0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.edit_box = QtWidgets.QLineEdit()
        layout.addWidget(self.edit_box, 0, 1, 1, 3)

        self.edit_comment_box = QtWidgets.QLineEdit()
        layout.addWidget(self.edit_comment_box, 1, 1, 1, 3)

        self.categories_list = ["Продукты", "Одежда"]
        self.categories_list_widget = QtWidgets.QComboBox()
        self.categories_list_widget.addItems(self.categories_list)
        layout.addWidget(self.categories_list_widget, 2, 1, 1, 3)

        self.add_button = QtWidgets.QPushButton("Добавить запись")
        layout.addWidget(self.add_button, 4, 1)

        self.edit_expense_button = QtWidgets.QPushButton("Исправить запись")
        layout.addWidget(self.edit_expense_button, 4, 2)

        self.del_button = QtWidgets.QPushButton("Удалить запись")
        layout.addWidget(self.del_button, 4, 3)

        self.add_comment_button = QtWidgets.QPushButton("Добавить категорию")
        layout.addWidget(self.add_comment_button, 6, 1)

        self.edit_comment_button = QtWidgets.QPushButton("Исправить категорию")
        layout.addWidget(self.edit_comment_button, 6, 2)

        self.del_comment_button = QtWidgets.QPushButton("Удалить категорию")
        layout.addWidget(self.del_comment_button, 6, 3)

        self.edit_category_box = QtWidgets.QLineEdit()
        layout.addWidget(self.edit_category_box, 5, 1, 1, 3)

        self.edit_date = QtWidgets.QDateTimeEdit(QtCore.QDateTime.currentDateTime())
        layout.addWidget(self.edit_date, 3, 1, 1, 3)
