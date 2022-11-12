import csv
import os

from PyQt5.QtWidgets import (QFileDialog, QInputDialog, QMainWindow,
                             QTableWidget, QTableWidgetItem)

from .models import table_notes_model
from .templates.table_notes_template import Ui_TableNotes


class TableNotes(QMainWindow, Ui_TableNotes):
    def __init__(self, ex, table_id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.form = ex
        self.table_id = table_id
        self.move(325, 20)
        self.to_list_table_notes_button.clicked.connect(
            self.to_list_table_notes
            )
        self.load_file_button.clicked.connect(self.load_file)
        self.change_title_button.clicked.connect(self.change_title)
        self.delete_file_button.clicked.connect(self.delete_file)

        self.load_data()

    def delete_all_tab_widgets(self):
        pages = table_notes_model.select_pages(table_id=self.table_id)
        if not pages:
            return
        else:
            last_page = pages[-1][0]
        for i in range(last_page):
            self.tabWidget.removeTab(0)

    def load_data(self):
        self.delete_all_tab_widgets()
        data = table_notes_model.select_foreign_key_list_table_notes(
            table_id=self.table_id,
        )
        if data:
            for line in data:
                title_of_the_page = line[4]
                file = line[1]
                delimiter = line[-3]
                quotechar = line[-2]
                newline = line[-1]
                new_table_widget = QTableWidget()
                self.tabWidget.addTab(new_table_widget, title_of_the_page)
                self.load_tab(
                    file=file,
                    delimiter=delimiter,
                    quotechar=quotechar,
                    newline=newline,
                    new_table_widget=new_table_widget,
                )

    def load_tab(self, file, delimiter, quotechar, newline, new_table_widget):
        try:
            with open(file, newline=newline) as csv_file:
                reader = csv.reader(
                    csv_file,
                    delimiter=delimiter,
                    quotechar=quotechar,
                )
                title = next(reader)
                new_table_widget.setColumnCount(len(title))
                new_table_widget.setHorizontalHeaderLabels(title)
                new_table_widget.setRowCount(0)
                for i, row in enumerate(reader):
                    new_table_widget.setRowCount(
                        new_table_widget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        new_table_widget.setItem(
                            i, j, QTableWidgetItem(elem))
            new_table_widget.resizeColumnsToContents()
        except Exception:
            self.status_bar.showMessage('Incorrect data')
            return

    def load_file(self):
        if self.tabWidget.count() == 14:
            self.status_bar.showMessage('The maximum number of tabs')
            return

        title_of_the_page, ok_pressed = QInputDialog.getText(
            self, 'Loading new page',
            'Enter the title'
        )
        if not ok_pressed and not title_of_the_page.strip():
            return

        delimiter, ok_pressed = QInputDialog.getText(
            self, 'Settings of the csv file',
            'Enter the delimiter'
        )
        if not ok_pressed and not delimiter.strip():
            return

        quotechar, ok_pressed = QInputDialog.getText(
            self, 'Settings of the csv file',
            'Enter the quotechar'
        )

        if not ok_pressed and not quotechar.strip():
            return

        newline, ok_pressed = QInputDialog.getText(
            self, 'Settings of the csv file',
            'Enter the newline'
        )
        if not ok_pressed:
            return

        pages = table_notes_model.select_pages(table_id=self.table_id)

        if not pages:
            last_page = 0
        else:
            last_page = pages[-1][0]

        new_table_widget = QTableWidget()
        self.tabWidget.addTab(new_table_widget, title_of_the_page)

        file = QFileDialog.getOpenFileName(
            self,
            'Choose csv file', '',
            'File (*.csv)'
        )[0]

        if not file:
            return
        self.load_tab(
            file=file,
            delimiter=delimiter,
            quotechar=quotechar,
            newline=newline,
            new_table_widget=new_table_widget,
        )

        new_file = file.split('/')[-1]
        new_file = f'tables/{self.table_id}{new_file}'

        with open(new_file, newline=newline, mode='w') as new_csv_file,\
                open(file, newline=newline) as csv_file:
            reader = csv.reader(
                csv_file,
                delimiter=delimiter,
                quotechar=quotechar,
            )
            writer = csv.writer(
                new_csv_file, delimiter=delimiter, quotechar=quotechar)
            for line in reader:
                writer.writerow(line)

        table_notes_model.insert(
            table_id=self.table_id,
            file=new_file,
            page=last_page + 1,
            title_of_the_page=title_of_the_page,
            delimiter=delimiter,
            newline=newline,
            quotechar=quotechar,
        )

    def change_title(self):
        title, ok_pressed = QInputDialog.getText(
            self, 'Changing the title of the page',
            'Enter the title of the existing file you want to change'
        )
        if not ok_pressed and not title.strip():
            return

        data = table_notes_model.check_unique_title(
            table_id=self.table_id,
            title_of_the_page=title
        )
        if not data:
            self.status_bar.showMessage('Such file doesn\'t exist ')
            return

        new_title, ok_pressed = QInputDialog.getText(
            self, 'Changing the title of the page',
            'Enter new title'
        )

        if not ok_pressed and not title.strip():
            return

        entry_id = data[0][0]
        table_notes_model.update_title_of_the_page(
            entry_id=entry_id,
            new_title=new_title,
        )
        self.load_data()

    def delete_file(self):
        title, ok_pressed = QInputDialog.getText(self, 'Deleting the page',
                                                       'Enter the title')
        if not ok_pressed and not title.strip():
            return

        data = table_notes_model.check_unique_title(
            table_id=self.table_id,
            title_of_the_page=title
        )
        if not data:
            self.status_bar.showMessage('Such page doesn\'t exist ')
            return

        entry_id = data[0][0]

        file = table_notes_model.select_file(entry_id=entry_id)[0][0]
        os.remove(file)

        self.delete_all_tab_widgets()
        table_notes_model.delete_page(entry_id=entry_id)

        self.load_data()

    def to_list_table_notes(self):
        self.form.show()
        self.hide()
