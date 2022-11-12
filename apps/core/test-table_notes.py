import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 597)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 621, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 611, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_add_film.setObjectName("btn_add_film")
        self.horizontalLayout.addWidget(self.btn_add_film)
        self.btn_change_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_change_film.setObjectName("btn_change_film")
        self.horizontalLayout.addWidget(self.btn_change_film)
        self.btn_delete_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_delete_film.setObjectName("btn_delete_film")
        self.horizontalLayout.addWidget(self.btn_delete_film)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 51, 601, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 611, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add_genre = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_add_genre.setObjectName("btn_add_genre")
        self.horizontalLayout_2.addWidget(self.btn_add_genre)
        self.btn_change_genre = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_change_genre.setObjectName("btn_change_genre")
        self.horizontalLayout_2.addWidget(self.btn_change_genre)
        self.btn_delete_genre = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_delete_genre.setObjectName("btn_delete_genre")
        self.horizontalLayout_2.addWidget(self.btn_delete_genre)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(5, 51, 601, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")

        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Фильмотека 2.0"))
        self.tabWidget.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Фильмы</p></body></html>"))
        self.tabWidget.setWhatsThis(_translate("Dialog", "Жанры"))
        self.btn_add_film.setText(_translate("Dialog", "Добавить фильм"))
        self.btn_change_film.setText(_translate("Dialog", "Изменить фильм"))
        self.btn_delete_film.setText(_translate("Dialog", "Удалить фильм"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Tab 1"))
        self.btn_add_genre.setText(_translate("Dialog", "Добавить жанр"))
        self.btn_change_genre.setText(_translate("Dialog", "Редактировать жанр"))
        self.btn_delete_genre.setText(_translate("Dialog", "Удалить жанр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))


class Ui_AddWindowFilm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 342)
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setGeometry(QtCore.QRect(380, 281, 113, 41))
        self.btnAdd.setObjectName("btnAdd")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 29, 141, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 30, 191, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.spinYear = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinYear.setObjectName("spinYear")
        self.verticalLayout_2.addWidget(self.spinYear)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.spinDuration = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinDuration.setObjectName("spinDuration")
        self.verticalLayout_2.addWidget(self.spinDuration)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить фильм"))
        self.btnAdd.setText(_translate("Dialog", "Сохранить"))
        self.label_2.setText(_translate("Dialog", "Название"))
        self.label_4.setText(_translate("Dialog", "Год выпуска"))
        self.label.setText(_translate("Dialog", "Жанр"))
        self.label_3.setText(_translate("Dialog", "Длина"))


class Ui_AddWindowGenre(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 342)
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setGeometry(QtCore.QRect(380, 281, 113, 41))
        self.btnAdd.setObjectName("btnAdd")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 29, 141, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 30, 191, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить фильм"))
        self.btnAdd.setText(_translate("Dialog", "Сохранить"))
        self.label_2.setText(_translate("Dialog", "Название"))


class Ui_DelWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 169)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 311, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 130, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 90, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 90, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Действительно хотите удалить данную запись?"))
        self.pushButton.setText(_translate("Dialog", "Подтвердить"))
        self.radioButton.setText(_translate("Dialog", "Да"))
        self.radioButton_2.setText(_translate("Dialog", "Нет"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setTabText(0, 'Фильмы')
        self.tabWidget.setTabText(1, 'Жанры')

        self.con = sqlite3.connect("films_db.sqlite")
        self.load_films()
        self.load_genres()

        self.btn_add_film.clicked.connect(self.add_film)
        self.btn_change_film.clicked.connect(self.change_film)
        self.btn_delete_film.clicked.connect(self.delete_film)

        self.btn_add_genre.clicked.connect(self.add_genre)
        self.btn_change_genre.clicked.connect(self.change_genre)
        self.btn_delete_genre.clicked.connect(self.delete_genre)

        self.addForm = None

    def load_films(self):
        res = self.con.cursor().execute(
            f"""SELECT films.id, films.title,
                films.year, genres.title, films.duration FROM films
                INNER JOIN genres ON genres.id = films.genre
                ORDER BY films.id DESC;"""
        ).fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название фильма", "Год выпуска", "Жанр", "Продолжительность"]
        )
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def load_genres(self):
        res = self.con.cursor().execute(
            f"""SELECT id, title FROM genres"""
        ).fetchall()
        self.tableWidget_2.setColumnCount(len(res[0]))
        self.tableWidget_2.setHorizontalHeaderLabels(
            ["ID", "Название жанра"]
        )
        self.tableWidget_2.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add_film(self):
        self.addForm = AddWidgetFilm(self.con)
        self.addForm.show()

    def change_film(self):
        item = self.tableWidget.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget.item(item[0].row(), 0).text()
        title = self.tableWidget.item(item[0].row(), 1).text()
        year = self.tableWidget.item(item[0].row(), 2).text()
        genre = self.tableWidget.item(item[0].row(), 3).text()
        duration = self.tableWidget.item(item[0].row(), 4).text()

        self.addForm = AddWidgetFilm(self.con, title=title, year=year, genre=genre, duration=duration, pk=pk)
        self.addForm.show()

    def delete_film(self):
        item = self.tableWidget.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget.item(item[0].row(), 0).text()
        self.addForm = DelWidget(self.con, pk=pk, table='films')
        self.addForm.show()

    def add_genre(self):
        self.addForm = AddWidgetGenre(self.con)
        self.addForm.show()

    def change_genre(self):
        item = self.tableWidget_2.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget_2.item(item[0].row(), 0).text()
        title = self.tableWidget_2.item(item[0].row(), 1).text()

        self.addForm = AddWidgetGenre(self.con, title=title, pk=pk)
        self.addForm.show()

    def delete_genre(self):
        item = self.tableWidget_2.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget_2.item(item[0].row(), 0).text()
        self.addForm = DelWidget(self.con, pk=pk, table='genres')
        self.addForm.show()


class AddWidgetFilm(QMainWindow, Ui_AddWindowFilm):
    def __init__(self, con, *, title=None, year=None, genre=None, duration=None, pk=None):
        super().__init__()
        self.setupUi(self)
        self.con = con
        self.spinDuration.setMaximum(1000)
        self.spinYear.setMaximum(2030)
        self.spinYear.setMinimum(1800)
        if genre:
            self.get_genres(genre)
            self.spinDuration.setValue(int(duration))
            self.spinYear.setValue(int(year))
            self.lineEdit.setText(title)
            self.btnAdd.setText('Изменить')
            self.setWindowTitle('Редактировать фильм')
            state = 'update'
        else:
            state = 'insert'
            self.get_genres()
            self.btnAdd.setText('Сохранить')
            self.setWindowTitle('Добавить фильм')

        self.btnAdd.clicked.connect(lambda: self.add(state, pk))

    def get_genres(self, genre=None):
        res = self.con.cursor().execute(
            f"SELECT title FROM genres ORDER BY title"
        ).fetchall()
        res = [elem[0] for elem in res]
        if genre:
            res.remove(genre)
            res.insert(0, genre)
        self.comboBox.addItems(res)

    def add(self, state, pk):
        year = self.spinYear.value()
        duration = self.spinDuration.value()
        title = self.lineEdit.text()
        genre_title = self.comboBox.currentText()
        genre_id = self.con.cursor().execute(
            f"""SELECT id FROM genres
            WHERE title = '{genre_title}'""").fetchone()[0]
        if state == 'insert':
            requset = (f"""INSERT INTO films(title, duration, year, genre) 
                       VALUES ('{title}', {duration}, {year}, {genre_id});""")

        elif state == 'update':
            requset = (f"""UPDATE films
                       SET title = "{title}", duration = {duration}, year = {year}, genre = {genre_id}
                       WHERE id = {pk}""")
        else:
            raise ValueError('Not valid SQL operation')
        try:
            self.con.cursor().execute(requset)
        except Exception:
            self.statusBar().showMessage('Некорректные данные')
        self.con.commit()
        ex.load_films()
        self.hide()


class AddWidgetGenre(QMainWindow, Ui_AddWindowGenre):
    def __init__(self, con, *, title=None, pk=None):
        super().__init__()
        self.setupUi(self)
        if title:
            state = 'update'
            self.lineEdit.setText(title)
        else:
            state = 'insert'
        self.btnAdd.clicked.connect(lambda: self.add(state, pk))
        self.con = con

    def add(self, state, pk):
        title = self.lineEdit.text()
        if state == 'insert':
            requset = f"""INSERT INTO genres(title) 
                      VALUES ('{title}');"""
        elif state == 'update':
            requset = f"""UPDATE genres
                      SET title = "{title}"
                      WHERE id = {pk}"""
        else:
            raise ValueError('Not valid SQL operation')
        try:
            self.con.cursor().execute(requset)
        except Exception:
            self.statusBar().showMessage('Некорректные данные')
        self.con.commit()
        ex.load_genres()
        self.hide()


class DelWidget(QMainWindow, Ui_DelWindow):
    def __init__(self, con, *, pk, table):
        super().__init__()
        self.con = con
        self.setupUi(self)
        self.radioButton.setChecked(True)
        self.pushButton.clicked.connect(lambda: self.confirm(pk, table))

    def confirm(self, pk, table):
        if not self.radioButton.isChecked():
            self.hide()
            return
        req = f"""DELETE FROM {table}
                      WHERE id = {pk}"""
        self.con.cursor().execute(req)
        self.con.commit()
        if table == 'films':
            ex.load_films()
        elif table == 'genres':
            ex.load_genres()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
