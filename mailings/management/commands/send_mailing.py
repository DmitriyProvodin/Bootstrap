from django.core.management.base import BaseCommand
from mailings.models import Mailing
from mailings.services import send_mailing_now

class Command(BaseCommand):
    help = 'Send a mailing or all created mailings'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', nargs='?', type=int)

    def handle(self, *args, **options):
        mid = options.get('mailing_id')
        if mid:
            m = Mailing.objects.get(pk=mid)
            send_mailing_now(m)
            self.stdout.write(self.style.SUCCESS(f'Sent mailing {mid}'))
        else:
            for m in Mailing.objects.filter(status='created'):
                send_mailing_now(m)
                self.stdout.write(self.style.SUCCESS(f'Sent mailing {m.pk}'))
