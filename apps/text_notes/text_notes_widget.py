from PyQt5.QtWidgets import QInputDialog, QMainWindow

from .models import text_notes_model
from .templates.text_notes_template import Ui_TextNotes


class TextNotes(QMainWindow, Ui_TextNotes):
    def __init__(self, ex, data, folder_id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.form = ex
        self.folder_id = folder_id
        self.move(250, 20)
        for i in range(1, 11):
            self.__getattribute__(f'save_button_page_{i}').clicked.connect(
                self.insert_text
            )

        for i in range(1, 11):
            self.__getattribute__(
                f'change_title_button_page_{i}').clicked.connect(
                    self.change_title
            )
        self.to_main_menu_button.clicked.connect(self.to_list_text_notes)

        indexes_of_all_pages = {i for i in range(1, 11)}

        for i in range(len(data)):
            title_of_the_page = data[i][-1]
            text = data[i][1]
            page = data[i][-2]
            indexes_of_all_pages.remove(page)
            self.all_pages_tool_box.setItemText(page - 1, title_of_the_page)
            self.__getattribute__(f'textEdit_page_{page}').setText(text)

        for elem in indexes_of_all_pages:
            self.all_pages_tool_box.setItemText(elem - 1, f'Page {elem}')

    def insert_text(self):
        sender = self.sender()
        page = int(sender.objectName().split('_')[-1])
        text = self.__getattribute__(f'textEdit_page_{page}').toPlainText()
        page_title = self.all_pages_tool_box.itemText(page - 1)
        text_notes_model.insert(
            text=text,
            page=page,
            title_of_the_page=page_title,
            folder_id=self.folder_id,
        )

    def change_title(self):
        sender = self.sender()
        text, ok_pressed = QInputDialog.getText(
            self,
            "Change title of the page",
            "Enter new title",
        )
        if not ok_pressed and not text.strip():
            return
        page = int(sender.objectName().split('_')[-1])
        self.all_pages_tool_box.setItemText(page - 1, text)
        text_notes_model.update_title_of_the_page(
            folder_id=self.folder_id,
            page=page,
            title_of_the_page=text
        )

    def to_list_text_notes(self):
        self.form.show()
        self.hide()
