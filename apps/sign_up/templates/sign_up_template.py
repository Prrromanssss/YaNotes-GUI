from PyQt5 import QtCore, QtWidgets


class Ui_SigningUp(object):
    def setupUi(self, SigningUp):
        SigningUp.setObjectName("SigningUp")
        SigningUp.resize(495, 438)
        self.login_sign_up_label = QtWidgets.QLabel(SigningUp)
        self.login_sign_up_label.setGeometry(QtCore.QRect(30, 80, 145, 21))
        self.login_sign_up_label.setObjectName("login_sign_up_label")
        self.password_sign_up_label = QtWidgets.QLabel(SigningUp)
        self.password_sign_up_label.setGeometry(QtCore.QRect(30, 150, 145, 21))
        self.password_sign_up_label.setObjectName("password_sign_up_label")
        self.login_sign_up_edit = QtWidgets.QLineEdit(SigningUp)
        self.login_sign_up_edit.setGeometry(QtCore.QRect(30, 100, 181, 31))
        self.login_sign_up_edit.setBaseSize(QtCore.QSize(40, 68))
        self.login_sign_up_edit.setObjectName("login_sign_up_edit")
        self.registarion_name = QtWidgets.QLabel(SigningUp)
        self.registarion_name.setGeometry(QtCore.QRect(160, 20, 131, 41))
        self.registarion_name.setObjectName("registarion_name")
        self.password_sign_up_edit = QtWidgets.QLineEdit(SigningUp)
        self.password_sign_up_edit.setGeometry(QtCore.QRect(30, 170, 181, 31))
        self.password_sign_up_edit.setBaseSize(QtCore.QSize(40, 68))
        self.password_sign_up_edit.setObjectName("password_sign_up_edit")
        self.password2_sign_up_edit = QtWidgets.QLineEdit(SigningUp)
        self.password2_sign_up_edit.setGeometry(QtCore.QRect(30, 210, 181, 31))
        self.password2_sign_up_edit.setBaseSize(QtCore.QSize(40, 68))
        self.password2_sign_up_edit.setObjectName("password2_sign_up_edit")
        self.email_sign_up_edit = QtWidgets.QLineEdit(SigningUp)
        self.email_sign_up_edit.setGeometry(QtCore.QRect(30, 280, 181, 31))
        self.email_sign_up_edit.setBaseSize(QtCore.QSize(40, 68))
        self.email_sign_up_edit.setObjectName("email_sign_up_edit")
        self.email_sign_up_label = QtWidgets.QLabel(SigningUp)
        self.email_sign_up_label.setGeometry(QtCore.QRect(30, 260, 145, 21))
        self.email_sign_up_label.setObjectName("email_sign_up_label")
        self.confirm_personal_data_checkbox = QtWidgets.QCheckBox(SigningUp)
        self.confirm_personal_data_checkbox.setGeometry(QtCore.QRect(30, 340, 20, 21))
        self.confirm_personal_data_checkbox.setText("")
        self.confirm_personal_data_checkbox.setObjectName("confirm_personal_data_checkbox")
        self.confirm_personal_data_label = QtWidgets.QLabel(SigningUp)
        self.confirm_personal_data_label.setGeometry(QtCore.QRect(50, 320, 331, 71))
        self.confirm_personal_data_label.setObjectName("confirm_personal_data_label")
        self.kitty = QtWidgets.QLabel(SigningUp)
        self.kitty.setGeometry(QtCore.QRect(229, 29, 261, 321))
        self.kitty.setObjectName("kitty")
        self.sign_up_confirm_button = QtWidgets.QPushButton(SigningUp)
        self.sign_up_confirm_button.setGeometry(QtCore.QRect(330, 360, 131, 41))
        self.sign_up_confirm_button.setObjectName("sign_up_confirm_button")

        self.not_all_data_status_bar = QtWidgets.QStatusBar(SigningUp)
        self.not_all_data_status_bar.setObjectName("statusbar")
        SigningUp.setStatusBar(self.not_all_data_status_bar)

        self.retranslateUi(SigningUp)
        QtCore.QMetaObject.connectSlotsByName(SigningUp)

    def retranslateUi(self, SigningUp):
        _translate = QtCore.QCoreApplication.translate
        SigningUp.setWindowTitle(_translate("SigningUp", "Dialog"))
        self.login_sign_up_label.setText(_translate("SigningUp", "<html><head/><body><p><span style=\" font-size:18pt;\">Login</span><span style=\" font-size:18pt; color:#fa3737; vertical-align:super;\">*</span></p></body></html>"))
        self.password_sign_up_label.setText(_translate("SigningUp", "<html><head/><body><p><span style=\" font-size:18pt;\">Password<span style=\"color: rgb(250, 55, 55);\">*</span></span></p></body></html>"))
        self.registarion_name.setText(_translate("SigningUp", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Registration</span></p></body></html>"))
        self.email_sign_up_label.setText(_translate("SigningUp", "<html><head/><body><p><span style=\" font-size:18pt;\">Email<span style=\"color: rgb(250, 55, 55);\">*</span></span></p></body></html>"))
        self.confirm_personal_data_label.setText(_translate("SigningUp", "<html><head/><body><p><span style=\" font-size:11pt;\">By clicking on the </span><span style=\" font-size:11pt; font-weight:600;\">Register</span><span style=\" font-size:11pt;\"> button, I consent to the processing</span></p><p><span style=\" font-size:11pt;\">of personal data in accordance with the </span><a href=\"https://ya.ru/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">Personal Data</span></a></p><p><a href=\"https://ya.ru\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">Processing Policy</span></a></p></body></html>"))
        self.kitty.setText(_translate("SigningUp", "⣿⣿⣿⣿⣿⢙⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢋⠉⠘⣿⣿\n"
"⣿⣿⣿⣿⡏⠄⠄⠄⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠄⠄⠄⠄⠁⢸⣿\n"
"⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠈⠙⢿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⢀⠄⠄⢹⣿\n"
"⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⢸⣿\n"
"⣿⣿⣿⠿⢤⣤⡔⠒⣶⣶⣶⣶⣶⡖⠒⠒⠒⠒⣶⣖⠒⣶⣦⣤⣤⣄⣸⣿\n"
"⣿⣷⡀⠄⠈⣿⣿⡄⢻⣿⣿⣿⣿⣿⡄⠄⠄⠄⢹⣿⡆⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣷⠄⠄⠸⣿⣷⡈⣿⣿⡿⠹⣿⣿⡀⠄⠄⠄⢻⣿⡄⢻⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣷⣾⣷⣿⣿⣿⣿⡿⠁⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠄⣿⣿⣿⣿⡿⠁⠄⣤⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿\n"
"⣿⣿⣿⠟⠄⠄⠉⠉⠉⠄⠄⡿⠛⢻⠈⠙⠟⠛⠛⠻⠿⠿⢿⠿⠿⠁⢀⣿\n"
"⣿⣿⣿⣿⡝⠐⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠩⠐⡀⠄⠄⠈⠉⢿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡖⠄⣀⠄⠄⠛⠻⣿⣿⠟⠛⠄⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⠇⣠⠊⠈⠐⠤⢤⣀⣀⣠⠤⣀⣀⣀⠛⠉⠄⠉⠻⣿⣿⣿⣿\n"
"⣿⣿⣿⡿⢋⡰⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿\n"
"⣿⣿⡋⠐⢰⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿"))
        self.sign_up_confirm_button.setText(_translate("SigningUp", "Sign up"))
