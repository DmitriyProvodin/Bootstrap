from celery import shared_task
from django.utils import timezone
import requests
from django.conf import settings
from .models import Habit


@shared_task
def send_habit_reminder(habit_id):
    habit = Habit.objects.get(id=habit_id)
    user = habit.user

    if not user.telegram_chat_id:
        return "NO_CHAT_ID"

    message = f"Напоминание!\n{habit.action} в {habit.time} по адресу: {habit.place}"
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"

    requests.post(url, data={"chat_id": user.telegram_chat_id, "text": message})

    return "SENT"
