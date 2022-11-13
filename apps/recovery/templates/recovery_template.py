from PyQt5 import QtCore, QtWidgets


class Ui_Recovery(object):
    def setupUi(self, Recovery):
        Recovery.setObjectName("Recovery")
        Recovery.resize(481, 356)
        self.login_recovery_label = QtWidgets.QLabel(Recovery)
        self.login_recovery_label.setGeometry(QtCore.QRect(30, 80, 145, 21))
        self.login_recovery_label.setObjectName("login_recovery_label")
        self.password_recovery_label = QtWidgets.QLabel(Recovery)
        self.password_recovery_label.setGeometry(QtCore.QRect(30, 150, 145, 21))
        self.password_recovery_label.setObjectName("password_recovery_label")
        self.login_recovery_edit = QtWidgets.QLineEdit(Recovery)
        self.login_recovery_edit.setGeometry(QtCore.QRect(30, 100, 181, 31))
        self.login_recovery_edit.setBaseSize(QtCore.QSize(40, 68))
        self.login_recovery_edit.setObjectName("login_recovery_edit")
        self.recovery_name = QtWidgets.QLabel(Recovery)
        self.recovery_name.setGeometry(QtCore.QRect(120, 0, 211, 41))
        self.recovery_name.setObjectName("recovery_name")
        self.password_recovery_edit = QtWidgets.QLineEdit(Recovery)
        self.password_recovery_edit.setGeometry(QtCore.QRect(30, 170, 181, 31))
        self.password_recovery_edit.setBaseSize(QtCore.QSize(40, 68))
        self.password_recovery_edit.setObjectName("password_recovery_edit")
        self.password2_recovery_edit = QtWidgets.QLineEdit(Recovery)
        self.password2_recovery_edit.setGeometry(QtCore.QRect(30, 210, 181, 31))
        self.password2_recovery_edit.setBaseSize(QtCore.QSize(40, 68))
        self.password2_recovery_edit.setObjectName("password2_recovery_edit")
        self.finger_recovery_label = QtWidgets.QLabel(Recovery)
        self.finger_recovery_label.setGeometry(QtCore.QRect(220, 40, 251, 301))
        self.finger_recovery_label.setObjectName("finger_recovery_label")
        self.recovery_button = QtWidgets.QPushButton(Recovery)
        self.recovery_button.setGeometry(QtCore.QRect(30, 280, 113, 41))
        self.recovery_button.setObjectName("recovery_button")

        self.retranslateUi(Recovery)
        QtCore.QMetaObject.connectSlotsByName(Recovery)

    def retranslateUi(self, Recovery):
        _translate = QtCore.QCoreApplication.translate
        Recovery.setWindowTitle(_translate("Recovery", "Dialog"))
        self.login_recovery_label.setText(_translate("Recovery", "<html><head/><body><p><span style=\" font-size:18pt;\">Login</span><span style=\" font-size:18pt; color:#fa3737; vertical-align:super;\">*</span></p></body></html>"))
        self.password_recovery_label.setText(_translate("Recovery", "<html><head/><body><p><span style=\" font-size:18pt;\">Password<span style=\"color: rgb(250, 55, 55);\">*</span></span></p></body></html>"))
        self.recovery_name.setText(_translate("Recovery", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Password recovery</span></p></body></html>"))
        self.finger_recovery_label.setText(_translate("Recovery", "+88_________________+880_______\n"
"_+880_______________++80_______\n"
"_++88______________+880________\n"
"_++88_____________++88________\n"
"__+880___________++88_________\n"
"__+888_________++880__________\n"
"__++880_______++880___________\n"
"__++888_____+++880____________\n"
"__++8888__+++8880++88_________\n"
"__+++8888+++8880++8888________\n"
"___++888++8888+++888888+80____\n"
"___++88++8888++8888888++888___\n"
"___++++++888888fx88888888888___\n"
"____++++++88888888888888888___\n"
"____++++++++000888888888888___\n"
"_____+++++++00008f8888888888___\n"
"______+++++++00088888888888___\n"
"_______+++++++0888f8888888\n"
""))
        self.recovery_button.setText(_translate("Recovery", "Recover"))
