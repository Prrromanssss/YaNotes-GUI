import asyncio
import datetime

import telebot.async_telebot

from apps.calendar_notes.models import calendar_notes_model
from settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


async def send_messages():
    while True:
        data = calendar_notes_model.select_all()
        for entry in data:
            # print(entry)
            date_user = entry[2]
            date, time = date_user.split()[0], date_user.split()[-1]
            date_user = datetime.datetime(
                int(date.split('-')[0]),
                int(date.split('-')[1]),
                int(date.split('-')[2]),
                int(time.split(':')[0]),
                int(time.split(':')[1]),
                int(time.split(':')[2])
            )
            date_now = datetime.datetime.now()
            gmt = datetime.timedelta(entry[3] - 3)
            date_user += gmt
            if date_user < date_now:
                calendar_notes_model.delete_entry(entry_id=entry[0])
            if not entry[-1]:
                continue
            event = entry[1]
            chat_id = entry[-3]
            if (date_now.year == date_user.year and
                date_now.month == date_user.month and
                date_now.day == date_user.day and
                date_now.hour == date_user.hour and
                    date_now.minute == date_user.minute):
                try:
                    bot.send_message(chat_id=chat_id, text=event)
                except Exception as e:
                    print(e)
                calendar_notes_model.delete_entry(entry_id=entry[0])
        await asyncio.sleep(1)
