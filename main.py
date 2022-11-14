import asyncio
import sys

from asyncqt import QEventLoop
from PyQt5.QtWidgets import QApplication

from apps.sign_in.sign_in_widget import SignInWidget
from bot.calendar_notes.send_notes import send_messages


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


async def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    ex = SignInWidget()
    ex.show()
    sys.excepthook = except_hook

    with loop:

        loop.run_until_complete(send_messages())
        loop.run_forever()


if __name__ == '__main__':

    asyncio.run(main())
