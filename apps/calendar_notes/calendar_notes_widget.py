import datetime

from PyQt5.QtWidgets import QInputDialog, QMainWindow, QMessageBox

from .models import calendar_notes_model
from .templates.calendar_notes_template import Ui_CalendarNotes


class CalendarNotes(QMainWindow, Ui_CalendarNotes):
    def __init__(self, user_login, user_email, user_image):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.user_login = user_login
        self.user_email = user_email
        self.user_image = user_image
        self.form = None
        self.calendarWidget.setStyleSheet("QCalendarWidget QMenu"
                                          "{"
                                          "border : 4px solid red;"
                                          "}"
                                          )

        self.to_main_menu_button.clicked.connect(self.main_menu)
        list_of_gmt = [f'GMT-{i}' for i in range(12, 0, -1)]
        list_of_gmt.extend([f'GMT+{i}' for i in range(0, 14)])
        self.gmt_indexes = {i: f'GMT-{i}' for i in range(12, 0, -1)}
        self.gmt_indexes.update({i + 13: f'GMT+{i}' for i in range(0, 14)})

        self.comboBox.addItems(list_of_gmt)
        self.comboBox.setCurrentIndex(15)
        self.connect_tg_bot_button.clicked.connect(self.confirm_tg_bot)
        self.add_event_button.clicked.connect(self.add_event)
        self.turn_on_radioButton.setChecked(True)
        self.turn_on_radioButton.toggled.connect(self.clicked_turn_on)
        self.load_data()

    def clicked_turn_on(self):
        sender = self.sender()
        flag_to_send = sender.isChecked()
        calendar_notes_model.update_flag_to_send(
            login=self.user_login,
            flag_to_send=flag_to_send
        )

    def load_data(self):
        data = calendar_notes_model.select(login=self.user_login)
        for line in data:
            if line[-4] > 0:
                gmt = f'+{line[-4]}'
            else:
                gmt = f'GMT{line[-4]}'
            text = line[2] + '-' + line[1]
            flag_to_send = line[-1]
            self.listWidget.addItem(text)
            self.comboBox.setCurrentText(gmt)
            if flag_to_send:
                self.turn_on_radioButton.setChecked(True)

    def add_event(self):
        if not self.event_lineEdit.text():
            QMessageBox.warning(
                self,
                'Error',
                'Write some event',
                QMessageBox.Ok,
            )
            return

        calendar = self.calendarWidget.selectedDate()
        date_user = datetime.datetime(
            int(calendar.year()),
            int(calendar.month()),
            int(calendar.day()),
            int(self.timeEdit.text().split(':')[0]),
            int(self.timeEdit.text().split(':')[-1]))
        date_now = datetime.datetime.now()
        print(date_now, date_user)
        if date_user < datetime.datetime.now():
            QMessageBox.warning(
                self,
                'Error',
                'This date was in the past, look in the future!',
                QMessageBox.Ok,
            )
            return
        gmt = int(self.comboBox.currentText().split('GMT')[-1])
        self.listWidget.addItem(
            f'{calendar.year()}-{calendar.month()}-{calendar.day()}'
            f' {self.timeEdit.text()} - {self.event_lineEdit.text()}'
        )
        self.listWidget.sortItems()
        flag_to_send = self.turn_on_radioButton.isChecked()
        calendar_notes_model.insert(
            login=self.user_login,
            event=self.event_lineEdit.text(),
            gmt=gmt,
            datetime=date_user,
            flag_to_send=flag_to_send,
        )

    def confirm_tg_bot(self):
        chat_id, ok_pressed = QInputDialog.getInt(
            self, 'Configuration tg_bot',
            'Enter chat id'
        )

        if not ok_pressed:
            return

        calendar_notes_model.update_chat_id(
            chat_id=chat_id,
            login=self.user_login,
            )

    def main_menu(self):
        from ..account.account_widget import AccountWidget

        self.form = AccountWidget(
            self.user_login,
            self.user_email,
            self.user_image
        )
        self.form.show()
        self.hide()
