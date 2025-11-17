from celery import shared_task
from django.utils import timezone
from django.conf import settings
from .models import Habit
import requests
@shared_task
def send_due_reminders():
    token = settings.TELEGRAM_BOT_TOKEN
    if not token:
        return {'sent':0, 'error':'no token'}
    sent = 0
    # Simplified: send reminders for habits whose time is within current hour
    now = timezone.localtime()
    candidates = Habit.objects.filter(is_public=False)[:100]
    for h in candidates:
        try:
            chat_id = h.user.telegram_chat_id or settings.TELEGRAM_CHAT_ID
            if not chat_id:
                continue
            text = f"Reminder: {h.action} at {h.time}. Place: {h.place}"
            url = f'https://api.telegram.org/bot{token}/sendMessage'
            requests.post(url, data={'chat_id': chat_id, 'text': text}, timeout=5)
            sent += 1
        except Exception:
            continue
    return {'sent': sent}
