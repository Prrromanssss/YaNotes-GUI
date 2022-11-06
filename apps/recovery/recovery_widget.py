from .templates.recovery_template import Ui_Recovery
from PyQt5.QtWidgets import QMainWindow, QLineEdit


class RecoveryWidget(QMainWindow, Ui_Recovery):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_recovery_edit.setPlaceholderText('Enter the password')
        self.password2_recovery_edit.setPlaceholderText('Repeat the password')
        self.password_recovery_edit.setEchoMode(QLineEdit.Password)
        self.password2_recovery_edit.setEchoMode(QLineEdit.Password)
        self.recovery_button.clicked.connect(self.recovery)

    def recovery(self):
        ...