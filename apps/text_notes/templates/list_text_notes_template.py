from PyQt5 import QtCore, QtWidgets


class Ui_ListTextNotes(object):
    def setupUi(self, ListTextNotes):
        ListTextNotes.setObjectName("ListTextNotes")
        ListTextNotes.resize(616, 586)
        self.to_main_menu_button = QtWidgets.QPushButton(ListTextNotes)
        self.to_main_menu_button.setGeometry(QtCore.QRect(0, 30, 101, 41))
        self.to_main_menu_button.setObjectName("to_main_menu_button")
        self.add_folder_button = QtWidgets.QPushButton(ListTextNotes)
        self.add_folder_button.setGeometry(QtCore.QRect(0, 80, 101, 41))
        self.add_folder_button.setObjectName("add_folder_button")
        self.scrollArea = QtWidgets.QScrollArea(ListTextNotes)
        self.scrollArea.setGeometry(QtCore.QRect(109, 19, 491, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.not_unique_title_status_bar = QtWidgets.QStatusBar(ListTextNotes)
        self.not_unique_title_status_bar.setObjectName("statusbar")
        ListTextNotes.setStatusBar(self.not_unique_title_status_bar)

        self.retranslateUi(ListTextNotes)
        QtCore.QMetaObject.connectSlotsByName(ListTextNotes)

    def retranslateUi(self, ListTextNotes):
        _translate = QtCore.QCoreApplication.translate
        ListTextNotes.setWindowTitle(_translate("ListTextNotes", "Dialog"))
        self.to_main_menu_button.setText(_translate("ListTextNotes", "<- Back"))
        self.add_folder_button.setText(_translate("ListTextNotes", "Add folder"))
