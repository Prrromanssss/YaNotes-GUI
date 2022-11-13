from PIL import Image
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from ..calendar_notes.calendar_notes_widget import CalendarNotes
from ..table_notes.list_table_notes_widget import ListTableNotes
from ..text_notes.list_text_notes_widget import ListTextNotes
from .delete_account_widget import DeleteAccount
from .models import users_model
from .templates.account_template import Ui_Account


class AccountWidget(QMainWindow, Ui_Account):
    def __init__(self, login, email, image):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.email_edit.setText(email)
        self.email_edit.setReadOnly(True)
        self.login_label.setText(login)
        self.login_label.setFont(QFont('Arial', 24))
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image = image
        if image:
            self.picture_label.setPixmap(QPixmap(image))
        self.delete_acc_button.clicked.connect(self.delete_account)
        self.text_notes_button.clicked.connect(self.text_notes)
        self.calendar_notes_button.clicked.connect(self.calendar_notes)
        self.table_notes_button.clicked.connect(self.table_notes)
        self.load_picture_button.clicked.connect(self.load_picture)
        self.form = None

    def load_picture(self):
        file = QFileDialog.getOpenFileName(
            self,
            'Choose the image', '',
            'Image (*.png)'
        )[0]

        if file:
            self.picture_label.setPixmap(QPixmap(file))
            login = self.login_label.text()
            im = Image.open(file)
            image = f'media/{login}.png'
            self.image = image
            im.save(image)

            users_model.insert_image(file=image, login=login)

    def delete_account(self):
        login = self.login_label.text()
        self.form = DeleteAccount(self, login)
        self.form.show()

    def text_notes(self):
        login = self.login_label.text()
        self.form = ListTextNotes(login, self.email_edit.text(), self.image)
        self.form.show()
        self.hide()

    def table_notes(self):
        login = self.login_label.text()
        self.form = ListTableNotes(login, self.email_edit.text(), self.image)
        self.form.show()
        self.hide()

    def calendar_notes(self):
        login = self.login_label.text()
        self.form = CalendarNotes(login, self.email_edit.text(), self.image)
        self.form.show()
        self.hide()

    def back_to_sign_in(self):
        ...
        # ToDo:  button to go back to sign in
