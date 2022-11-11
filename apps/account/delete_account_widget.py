from PyQt5.QtWidgets import QMainWindow

from .models import users_model
from .templates.delete_account_template import Ui_DeleteAccount


class DeleteAccount(QMainWindow, Ui_DeleteAccount):
    def __init__(self, ex, login):
        super().__init__()
        self.setupUi(self)
        self.ex = ex
        self.login = login
        self.form = None
        self.confirm_del_button.clicked.connect(self.confirm_deletion)

    def confirm_deletion(self):
        yes = self.yes_radio_button.isChecked()
        if yes:
            from ..sign_in.sign_in_widget import SignInWidget

            users_model.delete_user(login=self.login)
            self.ex.hide()
            self.form = SignInWidget()
            self.form.show()

        self.hide()
