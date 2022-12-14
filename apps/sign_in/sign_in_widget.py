from PyQt5.QtWidgets import QLineEdit, QMainWindow, QMessageBox

from ..account.account_widget import AccountWidget
from ..recovery.recovery_widget import RecoveryWidget
from ..sign_up.sign_up_widget import SignUpWidget
from .models import users_model
from .templates.sign_in_template import Ui_SigningIn


class SignInWidget(QMainWindow, Ui_SigningIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.forgot_password_button.clicked.connect(self.recovery)
        self.password_sign_in_edit.setEchoMode(QLineEdit.Password)
        self.form = None

    def sign_in(self):
        login = self.login_sign_in_edit.text()
        password = self.password_sign_in_edit.text()
        data = users_model.select_user(login=login)

        if not data:
            QMessageBox.warning(
                self,
                'Error',
                'You aren\'t registered',
                QMessageBox.Ok,
            )
            return

        if data[0][2] != password:
            QMessageBox.warning(
                self,
                'Error',
                'Wrong password',
                QMessageBox.Ok,
            )
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
