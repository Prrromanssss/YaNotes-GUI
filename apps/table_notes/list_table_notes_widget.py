from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QInputDialog, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget, QMessageBox)

from .models import list_table_notes_model
from .table_notes_widget import TableNotes
from .templates.list_table_notes_template import Ui_ListTableNotes


class ListTableNotes(QMainWindow, Ui_ListTableNotes):
    def __init__(self, user_login, user_email, user_image):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.user_login = user_login
        self.user_email = user_email
        self.user_image = user_image
        self.form = None
        self.to_main_main_button.clicked.connect(self.main_menu)
        self.add_table_button.clicked.connect(self.add_table)
        self.change_title_of_the_table_button.clicked.connect(
            self.change_title
        )
        self.delete_table_button.clicked.connect(self.delete_table)

        self.load_data()

    def load_data(self):
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        data = list_table_notes_model.select_user_id(login=self.user_login)
        for i in range(len(data)):
            title = data[i][-1]
            btn = self.create_button(title)
            self.layout.addWidget(btn)
        self.widget.setLayout(self.layout)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

    def add_table(self):
        title, ok_pressed = QInputDialog.getText(self, 'Creation new table',
                                                       'Enter the title')
        if not ok_pressed and not title.strip():
            return

        if not list_table_notes_model.check_unique_title(
                login=self.user_login,
                title_of_the_table=title
        ):
            btn = self.create_button(title)
            self.layout.addWidget(btn)
            self.widget.setLayout(self.layout)

            list_table_notes_model.insert(
                login=self.user_login,
                title_of_the_table=title,
                table=self.layout.count(),
            )
        else:
            QMessageBox.warning(
                self,
                'Error',
                'Title of the table must be unique',
                QMessageBox.Ok,
            )
            return

    def change_title(self):
        title, ok_pressed = QInputDialog.getText(
            self, 'Changing the title of the table',
            'Enter the title of the existing table you want to change'
        )
        if not ok_pressed and not title.strip():
            return

        data = list_table_notes_model.check_unique_title(
            login=self.user_login,
            title_of_the_table=title
        )
        if not data:
            QMessageBox.warning(
                self,
                'Error',
                'Such table doesn\'t exist',
                QMessageBox.Ok,
            )
            return

        new_title, ok_pressed = QInputDialog.getText(
            self, 'Changing the title of the table',
            'Enter new title'
        )

        if not ok_pressed and not title.strip():
            return

        entry_id = data[0][0]
        list_table_notes_model.update_title_of_the_folder(
            entry_id=entry_id,
            new_title=new_title,
        )

        self.load_data()

    def delete_table(self):
        title, ok_pressed = QInputDialog.getText(self, 'Deleting the table',
                                                       'Enter the title')
        if not ok_pressed and not title.strip():
            return

        data = list_table_notes_model.check_unique_title(
            login=self.user_login,
            title_of_the_table=title
        )
        if not data:
            QMessageBox.warning(
                self,
                'Error',
                'Such table doesn\'t exist',
                QMessageBox.Ok,
            )
            return

        entry_id = data[0][0]
        list_table_notes_model.cascade_delete_folder(entry_id=entry_id)

        self.load_data()

    def main_menu(self):
        from ..account.account_widget import AccountWidget

        self.form = AccountWidget(
            self.user_login,
            self.user_email,
            self.user_image
        )
        self.form.show()
        self.hide()

    def go_on_table_notes(self):
        sender = self.sender().text()
        data = list_table_notes_model.select_foreign_key_table_notes(
            login=self.user_login,
            title_of_the_table=sender
        )
        if not data:
            table_id = list_table_notes_model.select(
                login=self.user_login,
                title_of_the_table=sender,
            )[0][0]
        else:
            table_id = data[0][2]

        self.form = TableNotes(self, table_id)
        self.form.show()
        self.hide()

    def create_button(self, title):
        obj = QPushButton(title)
        obj.setMinimumHeight(50)
        obj.clicked.connect(self.go_on_table_notes)
        return obj
