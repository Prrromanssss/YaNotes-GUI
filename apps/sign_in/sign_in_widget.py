from PyQt5.QtWidgets import QLineEdit, QMainWindow

from ..account.account_widget import AccountWidget
from ..recovery.recovery_widget import RecoveryWidget
from ..sign_up.sign_up_widget import SignUpWidget
from .templates.sign_in_template import Ui_SigningIn
from .models import users_model


class SignInWidget(QMainWindow, Ui_SigningIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.forgot_password_button.clicked.connect(self.recovery)
        self.password_sign_in_edit.setEchoMode(QLineEdit.Password)
        self.form = None

    def sign_in(self):
        login = self.login_sign_in_edit.text()
        password = self.password_sign_in_edit.text()
        data = users_model.select_user(login)

        if not data:
            self.user_not_found_status_bar.showMessage('You are not registered')
            return

        if data[0][2] != password:
            self.user_not_found_status_bar.showMessage('Wrong password')
            return

        assert len(data) <= 1, 'Some users have the same login'

        self.form = AccountWidget(login=data[0][1], email=data[0][3],
                                  image=data[0][4])
        self.form.show()
        self.hide()

    def sign_up(self):
        self.form = SignUpWidget()
        self.form.show()
        self.hide()

    def recovery(self):
        self.form = RecoveryWidget()
        self.form.show()
        self.hide()
