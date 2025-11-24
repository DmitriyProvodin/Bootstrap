from celery import shared_task
from .bot import send_message

@shared_task
def send_reminder(chat_id, text):
    send_message(chat_id, text)
