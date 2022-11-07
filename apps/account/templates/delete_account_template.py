from PyQt5 import QtCore, QtWidgets


class Ui_DeleteAccount(object):
    def setupUi(self, DeleteAccount):
        DeleteAccount.setObjectName("DeleteAccount")
        DeleteAccount.resize(328, 169)
        self.confirm_del_label = QtWidgets.QLabel(DeleteAccount)
        self.confirm_del_label.setGeometry(QtCore.QRect(10, 30, 311, 61))
        self.confirm_del_label.setObjectName("label")
        self.confirm_del_button = QtWidgets.QPushButton(DeleteAccount)
        self.confirm_del_button.setGeometry(QtCore.QRect(90, 130, 113, 32))
        self.confirm_del_button.setObjectName("confirm_del_button")
        self.yes_radio_button = QtWidgets.QRadioButton(DeleteAccount)
        self.yes_radio_button.setGeometry(QtCore.QRect(40, 90, 100, 20))
        self.yes_radio_button.setObjectName("yes_radio_button")
        self.no_radio_button = QtWidgets.QRadioButton(DeleteAccount)
        self.no_radio_button.setGeometry(QtCore.QRect(190, 90, 100, 20))
        self.no_radio_button.setObjectName("no_radio_button")

        self.retranslateUi(DeleteAccount)
        QtCore.QMetaObject.connectSlotsByName(DeleteAccount)

    def retranslateUi(self, DeleteAccount):
        _translate = QtCore.QCoreApplication.translate
        DeleteAccount.setWindowTitle(_translate("DeleteAccount", "Dialog"))
        self.confirm_del_label.setText(_translate("DeleteAccount", "Are you sure you want to delete your account?"))
        self.confirm_del_button.setText(_translate("DeleteAccount", "Confirm"))
        self.yes_radio_button.setText(_translate("DeleteAccount", "Yes"))
        self.no_radio_button.setText(_translate("DeleteAccount", "No"))