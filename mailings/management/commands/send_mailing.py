from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailings.models import Mailing, Attempt

class Command(BaseCommand):
    help = 'Send mailing manually'

    def handle(self, *args, **options):
        for mailing in Mailing.objects.all():
            for recipient in mailing.recipients.all():
                try:
                    send_mail(
                        mailing.message.subject,
                        mailing.message.body,
                        None,
                        [recipient.email],
                    )
                    Attempt.objects.create(mailing=mailing, status='success', server_response='OK')
                    self.stdout.write(self.style.SUCCESS(f'Sent to {recipient.email}'))
                except Exception as e:
                    Attempt.objects.create(mailing=mailing, status='fail', server_response=str(e))
                    self.stdout.write(self.style.ERROR(f'Fail {recipient.email}: {e}'))
