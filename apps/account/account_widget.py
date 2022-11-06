from .templates.account_template import Ui_Account
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore


class AccountWidget(QMainWindow, Ui_Account):
    def __init__(self, login, email, image):
        super().__init__()
        self.setupUi(self)
        self.email_edit.setText(email)
        self.email_edit.setReadOnly(True)
        self.login_label.setText(login)
        self.setFixedSize(self.width(), self.height())
        self.login_label.setFont(QFont('Arial', 24))
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        if image:
            self.picture_label.setPixmap(QPixmap(image))
        self.delete_acc_button.clicked.connect(self.delete_account)
        self.text_notes_button.clicked.connect(self.text_notes)
        self.calendar_notes_button.clicked.connect(self.calendar_notes)
        self.table_notes_button.clicked.connect(self.table_notes)
        self.load_picture_button.clicked.connect(self.load_picture)

    def load_picture(self):
        ...

    def delete_account(self):
        ...

    def text_notes(self):
        ...

    def calendar_notes(self):
        ...

    def table_notes(self):
        ...
