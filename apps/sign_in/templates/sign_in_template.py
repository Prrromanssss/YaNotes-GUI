from PyQt5 import QtCore, QtWidgets


class Ui_SigningIn(object):
    def setupUi(self, SigningIn):
        SigningIn.setObjectName("SigningIn")
        SigningIn.resize(650, 386)
        self.project_name = QtWidgets.QLabel(SigningIn)
        self.project_name.setGeometry(QtCore.QRect(210, 0, 221, 41))
        self.project_name.setObjectName("project_name")
        self.sign_up_button = QtWidgets.QPushButton(SigningIn)
        self.sign_up_button.setGeometry(QtCore.QRect(470, 50, 131, 41))
        self.sign_up_button.setObjectName("sign_up_button")
        self.login_sign_in_edit = QtWidgets.QLineEdit(SigningIn)
        self.login_sign_in_edit.setGeometry(QtCore.QRect(250, 130, 181, 31))
        self.login_sign_in_edit.setBaseSize(QtCore.QSize(40, 68))
        self.login_sign_in_edit.setObjectName("login_sign_in_edit")
        self.login_sign_in_label = QtWidgets.QLabel(SigningIn)
        self.login_sign_in_label.setGeometry(QtCore.QRect(170, 120, 81, 59))
        self.login_sign_in_label.setObjectName("login_sign_in_label")
        self.password_sign_in_label = QtWidgets.QLabel(SigningIn)
        self.password_sign_in_label.setGeometry(QtCore.QRect(160, 190, 91, 59))
        self.password_sign_in_label.setObjectName("password_sign_in_label")
        self.password_sign_in_edit = QtWidgets.QLineEdit(SigningIn)
        self.password_sign_in_edit.setGeometry(QtCore.QRect(250, 200, 181, 31))
        self.password_sign_in_edit.setBaseSize(QtCore.QSize(40, 68))
        self.password_sign_in_edit.setObjectName("password_sign_in_edit")
        self.sign_in_button = QtWidgets.QPushButton(SigningIn)
        self.sign_in_button.setGeometry(QtCore.QRect(152, 260, 291, 51))
        self.sign_in_button.setObjectName("sign_in_button")
        self.forgot_password_button = QtWidgets.QPushButton(SigningIn)
        self.forgot_password_button.setGeometry(QtCore.QRect(230, 310, 141, 41))
        self.forgot_password_button.setObjectName("forgot_password_button")

        self.user_not_found_status_bar = QtWidgets.QStatusBar(SigningIn)
        self.user_not_found_status_bar.setObjectName("statusbar")
        SigningIn.setStatusBar(self.user_not_found_status_bar)

        self.retranslateUi(SigningIn)
        QtCore.QMetaObject.connectSlotsByName(SigningIn)

    def retranslateUi(self, SigningIn):
        _translate = QtCore.QCoreApplication.translate
        SigningIn.setWindowTitle(_translate("SigningIn", "Dialog"))
        self.project_name.setText(_translate("SigningIn", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\"><strong><span style=\"color: rgb(250, 55, 55);\" >Ya</span>Notes</strong></span></p></body></html>"))
        self.sign_up_button.setText(_translate("SigningIn", "Sign up"))
        self.login_sign_in_label.setText(_translate("SigningIn", "<html><head/><body><p><span style=\" font-size:18pt;\">Login:</span></p></body></html>"))
        self.password_sign_in_label.setText(_translate("SigningIn", "<html><head/><body><p><span style=\" font-size:18pt;\">Password:</span></p></body></html>"))
        self.sign_in_button.setText(_translate("SigningIn", "Sign in"))
        self.forgot_password_button.setText(_translate("SigningIn", "Forgot password?"))
