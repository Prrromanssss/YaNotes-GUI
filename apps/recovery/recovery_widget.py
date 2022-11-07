import sqlite3

from PyQt5.QtWidgets import QLineEdit, QMainWindow

from ..account.account_widget import AccountWidget
from ..core.exceptions import ValidationError
from .templates.recovery_template import Ui_Recovery
from .validators import validate_login, validate_password


class RecoveryWidget(QMainWindow, Ui_Recovery):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_recovery_edit.setPlaceholderText('Enter new password')
        self.password2_recovery_edit.setPlaceholderText('Repeat the password')
        self.password_recovery_edit.setEchoMode(QLineEdit.Password)
        self.password2_recovery_edit.setEchoMode(QLineEdit.Password)
        self.recovery_button.clicked.connect(self.recovery)
        self.form = None

    @staticmethod
    def update_password_of_th_user(login, password):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE users
                      SET password = '{password}'
                      WHERE login = '{login}' '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select_all_user_data(login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT * FROM users
                      WHERE login = '{login}' '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    def recovery(self):
        con = sqlite3.connect('YaNotes.sqlite3')
        login = self.login_recovery_edit.text()
        password1 = self.password_recovery_edit.text()
        password2 = self.password2_recovery_edit.text()

        login = self.validate_show_message(
            login,
            validate_func=validate_login,
            con=con,
        )
        password = self.validate_show_message(
            password1,
            password2,
            validate_func=validate_password,
        )
        if any(x is None for x in (login, password)):
            return

        self.update_password_of_th_user(login=login, password=password)
        data = self.select_all_user_data(login)

        self.form = AccountWidget(
            login=data[0][1],
            email=data[0][3],
            image=data[0][4],
        )
        self.form.show()
        self.hide()

    def validate_show_message(self, *data, validate_func, con):
        try:
            data = validate_func(*data, con)
        except ValidationError as e:
            self.not_all_data_status_bar.showMessage(str(e))
            return
        return data
