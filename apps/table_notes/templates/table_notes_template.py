# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apps/table_notes/templates/table_notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableNotes(object):
    def setupUi(self, TableNotes):
        TableNotes.setObjectName("TableNotes")
        TableNotes.resize(771, 747)
        self.tabWidget = QtWidgets.QTabWidget(TableNotes)
        self.tabWidget.setGeometry(QtCore.QRect(19, 59, 741, 661))
        self.tabWidget.setObjectName("tabWidget")
        self.to_list_table_notes_button = QtWidgets.QPushButton(TableNotes)
        self.to_list_table_notes_button.setGeometry(QtCore.QRect(10, 10, 113, 51))
        self.to_list_table_notes_button.setMinimumSize(QtCore.QSize(40, 40))
        self.to_list_table_notes_button.setObjectName("to_list_table_notes_button")
        self.layoutWidget = QtWidgets.QWidget(TableNotes)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 10, 409, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_file_button = QtWidgets.QPushButton(self.layoutWidget)
        self.load_file_button.setMinimumSize(QtCore.QSize(40, 40))
        self.load_file_button.setObjectName("load_file_button")
        self.horizontalLayout.addWidget(self.load_file_button)
        self.change_title_button = QtWidgets.QPushButton(self.layoutWidget)
        self.change_title_button.setMinimumSize(QtCore.QSize(40, 40))
        self.change_title_button.setObjectName("change_title_button")
        self.horizontalLayout.addWidget(self.change_title_button)
        self.delete_file_button = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_file_button.setMinimumSize(QtCore.QSize(40, 40))
        self.delete_file_button.setObjectName("delete_file_button")
        self.horizontalLayout.addWidget(self.delete_file_button)

        self.status_bar = QtWidgets.QStatusBar(TableNotes)
        self.status_bar.setObjectName("statusbar")
        TableNotes.setStatusBar(self.status_bar)

        self.retranslateUi(TableNotes)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TableNotes)

    def retranslateUi(self, TableNotes):
        _translate = QtCore.QCoreApplication.translate
        TableNotes.setWindowTitle(_translate("TableNotes", "Dialog"))
        self.to_list_table_notes_button.setText(_translate("TableNotes", "<- Back"))
        self.load_file_button.setText(_translate("TableNotes", "Load file"))
        self.change_title_button.setText(_translate("TableNotes", "Change title"))
        self.delete_file_button.setText(_translate("TableNotes", "Delete file"))