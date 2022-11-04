from templates.sign_up import Ui_SigningUp
from PyQt5.QtWidgets import QMainWindow


class SignUpWidget(QMainWindow, Ui_SigningUp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
