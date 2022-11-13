import asyncio
import os
import sys

# import aiohttp
# import telebot.async_telebot
from aiogram import Bot, Dispatcher, executor, types
from asyncqt import QEventLoop
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication

from apps.sign_in.sign_in_widget import SignInWidget

# from telegram.ext import CommandHandler, Updater


# from telegram.ext.dispatcher import run_async


load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN', 'summy-dummy token')

# bot = telebot.async_telebot.AsyncTeleBot(API_TOKEN)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @run_async
# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('Hi!')

# @bot.message_handler(commands=['start'])
# async def basic_commands(message):
#     text = 'Hey'
#     await bot.send_message(chat_id=message.chat.id, text=text)
#     await print_f()


async def print_f():
    while True:
        global count
        print(count)
        count += 1
        # bot.send_message(chat_id=1921020697, text='hey')
        await asyncio.sleep(1)


count = 0


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


async def _main():
    # await bot.close_session()
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    ex = SignInWidget()
    ex.show()
    sys.excepthook = except_hook

    with loop:
        loop.run_until_complete(executor.start_polling(dp, skip_updates=True))

        # loop.run_until_complete(print_f())
        loop.run_forever()


async def main():
    await executor.start_polling(dp, skip_updates=True)


def __main():
    # updater = Updater(API_TOKEN, use_context=True)

    # dp = updater.dispatcher

    # dp.add_handler(CommandHandler("start", start, run_async=True))

    # updater.start_polling()

    # updater.idle()



if __name__ == '__main__':
    asyncio.run(main())
