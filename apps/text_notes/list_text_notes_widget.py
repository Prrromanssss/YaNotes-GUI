from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QInputDialog, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)

from .models import list_text_notes_model
from .templates.list_text_notes_template import Ui_ListTextNotes
from .text_notes_widget import TextNotes


class ListTextNotes(QMainWindow, Ui_ListTextNotes):
    def __init__(self, user_login, user_email, user_image):
        super().__init__()
        self.user_login = user_login
        self.user_email = user_email
        self.user_image = user_image
        self.form = None
        self.setupUi(self)
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.add_folder_button.clicked.connect(self.add_folder)
        self.to_main_menu_button.clicked.connect(self.main_menu)
        data = list_text_notes_model.select(login=self.user_login)
        for i in range(len(data)):
            title = data[i][-1]
            btn = self.create_button(title)
            self.layout.addWidget(btn)
        self.widget.setLayout(self.layout)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

    def add_folder(self):
        title, ok_pressed = QInputDialog.getText(self, "Create new folder",
                                                       "Enter  title")
        if not ok_pressed and not title.strip():
            return

        if list_text_notes_model.check_unique_title(
            login=self.user_login,
            title_of_the_folder=title
        ):
            btn = self.create_button(title)
            self.layout.addWidget(btn)
            self.widget.setLayout(self.layout)

            list_text_notes_model.insert(
                login=self.user_login,
                title_of_the_folder=title,
                folder=self.layout.count(),
            )
        else:
            self.not_unique_title_status_bar.showMessage(
                'Title of the folder must be unique'
            )

    def create_button(self, title):
        obj = QPushButton(title)
        obj.setMinimumHeight(50)
        obj.clicked.connect(self.go_on_text_notes)
        return obj

    def main_menu(self):
        from ..account.account_widget import AccountWidget

        self.form = AccountWidget(
            self.user_login,
            self.user_email,
            self.user_image
        )
        self.form.show()
        self.hide()

    def go_on_text_notes(self):
        sender = self.sender().text()
        data = list_text_notes_model.select_foreign_key_text_notes(
            login=self.user_login,
            title_of_the_folder=sender
        )
        if not data:
            folder_id = list_text_notes_model.select(
                login=self.user_login
            )[0][0]
        else:
            folder_id = data[0][2]

        self.form = TextNotes(self, data, folder_id)
        self.form.show()
        self.hide()
