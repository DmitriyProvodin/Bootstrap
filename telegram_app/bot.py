import os
from telegram import Bot
from django.conf import settings

def send_message(chat_id, text):
    token = settings.TELEGRAM_BOT_TOKEN
    if not token:
        raise RuntimeError('TELEGRAM_BOT_TOKEN not set')
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=text)
