import sqlite3

from PyQt5.QtWidgets import QLineEdit, QMainWindow

from ..account.account_widget import AccountWidget
from ..core.exceptions import ValidationError
from .templates.sign_up_template import Ui_SigningUp
from .validators import (validate_agreement, validate_email, validate_login,
                         validate_password)
from .models import users_model


class SignUpWidget(QMainWindow, Ui_SigningUp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.password_sign_up_edit.setEchoMode(QLineEdit.Password)
        self.password2_sign_up_edit.setEchoMode(QLineEdit.Password)
        self.sign_up_confirm_button.clicked.connect(self.registrate_user)
        self.password_sign_up_edit.setPlaceholderText('Enter the password')
        self.password2_sign_up_edit.setPlaceholderText('Repeat the password')
        self.form = None

    def registrate_user(self):
        con = sqlite3.connect('YaNotes.sqlite3')

        login = self.login_sign_up_edit.text()
        password1 = self.password_sign_up_edit.text()
        password2 = self.password2_sign_up_edit.text()
        email = self.email_sign_up_edit.text()
        agreement = self.confirm_personal_data_checkbox.isChecked()

        login = self.validate_show_message(
            login,
            validate_func=validate_login,
            con=con,
        )
        email = self.validate_show_message(
            email,
            validate_func=validate_email,
            con=con,
        )
        password = self.validate_show_message(
            password1,
            password2,
            validate_func=validate_password,
        )
        agreement = self.validate_show_message(
            agreement,
            validate_func=validate_agreement,
        )
        if any(x is None for x in (login, email, password, agreement)):
            return

        users_model.insert_new_user(login=login, password=password, email=email)
        con.commit()

        self.form = AccountWidget(login=login, email=email, image=None)
        self.form.show()
        self.hide()

    def validate_show_message(self, *data, validate_func, con=None):
        try:
            data = validate_func(*data, con)
        except ValidationError as e:
            self.not_all_data_status_bar.showMessage(str(e))
            return
        return data
