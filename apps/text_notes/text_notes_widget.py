from PyQt5.QtWidgets import QMainWindow, QInputDialog

from .templates.text_notes_template import Ui_TextNotes
from .models import text_notes_model


class TextNotes(QMainWindow, Ui_TextNotes):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)
        self.user_login = user_login
        for i in range(1, 11):
            self.__getattribute__(f'save_button_page_{i}').clicked.connect(self.insert_text)

        for i in range(1, 11):
            self.__getattribute__(f'change_title_button_page_{i}').clicked.connect(self.change_title)

    # ToDo: select data from db

    def insert_text(self):
        sender = self.sender()
        page = int(sender.objectName().split('_')[-1])
        text = self.__getattribute__(f'textEdit_page_{page}').toPlainText()
        page_title = self.all_pages_tool_box.itemText(page - 1)
        text_notes_model.insert(
            text=text,
            page=page,
            title_of_the_page=page_title,
            login=self.user_login,
        )

    def change_title(self):
        sender = self.sender()
        text, ok_pressed = QInputDialog.getText(self, "Change title of the page",
                                                      "Enter new title")
        if not ok_pressed:
            return
        page = int(sender.objectName().split('_')[-1])
        self.all_pages_tool_box.setItemText(page - 1, text)
