from django.http import JsonResponse
from django.conf import settings

def register_webhook(request):
    return JsonResponse({'status': 'ok', 'token_present': bool(settings.TELEGRAM_BOT_TOKEN)})
