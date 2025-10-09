from django.core.mail import send_mail
from django.conf import settings
from .models import Attempt

def send_mailing_now(mailing):
    for recipient in mailing.recipients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                settings.DEFAULT_FROM_EMAIL,
                [recipient.email],
            )
            Attempt.objects.create(mailing=mailing, status='success', server_response='OK')
        except Exception as e:
            Attempt.objects.create(mailing=mailing, status='fail', server_response=str(e))
