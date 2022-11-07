from PIL import Image
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from .delete_account_widget import DeleteAccount
from .templates.account_template import Ui_Account


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
        self.form = None

    def load_picture(self):
        file = QFileDialog.getOpenFileName(
            self,
            'Выбрать картинку', '',
            'Картинка (*.png)'
        )[0]
        self.picture_label.setPixmap(QPixmap(file))
        # im = Image.open(file)
        # im.save('media/')
        # print(file)
        # ToDo: insert into database

    def delete_account(self):
        login = self.login_label.text()
        self.form = DeleteAccount(self, login)
        self.form.show()

    def text_notes(self):
        ...

    def calendar_notes(self):
        ...

    def table_notes(self):
        ...
