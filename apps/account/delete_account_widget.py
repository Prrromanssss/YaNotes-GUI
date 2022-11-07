import sqlite3

from PyQt5.QtWidgets import QMainWindow

from .templates.delete_account_template import Ui_DeleteAccount


class DeleteAccount(QMainWindow, Ui_DeleteAccount):
    def __init__(self, ex, login):
        super().__init__()
        self.setupUi(self)
        self.ex = ex
        self.login = login
        self.form = None
        self.confirm_del_button.clicked.connect(self.confirm_deletion)

    @staticmethod
    def delete_user(login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE FROM users
                                  WHERE login = '{login}' '''
        con.execute(request)
        con.commit()

    def confirm_deletion(self):
        yes = self.yes_radio_button.isChecked()

        if yes:
            from ..sign_in.sign_in_widget import SignInWidget

            self.delete_user(self.login)

            self.ex.hide()
            self.form = SignInWidget()
            self.form.show()

        self.hide()
