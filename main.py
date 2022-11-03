import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QStatusBar
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from templates.sign_in import Ui_SigningIn


class MainWidget(QMainWindow, Ui_SigningIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.password_sign_in_edit.setEchoMode(QLineEdit.Password)

    def sign_in(self):
        con = sqlite3.connect('db.sqlite3')
        login = self.login_sign_in_edit.text()
        password = self.password_sign_in_edit.text()
        request = f'''SELECT login, password FROM users 
                     WHERE login = {login} AND password = {password}'''
        data = con.execute(request).fetchall()
        assert len(data) == 1, 'Some users have the same login'
        if data is None:
            self.user_not_found_status_bar.showMessage('You are not registered')
        login, password = data[0][0], data[0][-1]

    def sign_up(self):
        ...


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


