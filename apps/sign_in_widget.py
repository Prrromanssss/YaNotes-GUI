import sqlite3
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from templates.sign_in import Ui_SigningIn
from apps.sign_up_widget import SignUpWidget


class SignInWidget(QMainWindow, Ui_SigningIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.password_sign_in_edit.setEchoMode(QLineEdit.Password)
        self.form = None

    def sign_in(self):
        con = sqlite3.connect('YaNotes.sqlite3')
        login = self.login_sign_in_edit.text()
        password = self.password_sign_in_edit.text()
        request = f'''SELECT login, password FROM users 
                     WHERE login = '{login}' AND password = '{password}' '''
        data = con.execute(request).fetchall()
        print(data, len(data))
        if not data:
            self.user_not_found_status_bar.showMessage('You are not registered')
        assert len(data) != 1, 'Some users have the same login'

    def sign_up(self):
        self.form = SignUpWidget()
        self.form.show()
        self.hide()

