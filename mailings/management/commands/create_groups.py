from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from mailings.models import Mailing

class Command(BaseCommand):
    help = 'Create group Managers with permissions'

    def handle(self, *args, **kwargs):
        ct = ContentType.objects.get_for_model(Mailing)
        perms = Permission.objects.filter(content_type=ct)
        g, _ = Group.objects.get_or_create(name='Managers')
        g.permissions.set(perms)
        self.stdout.write(self.style.SUCCESS('Managers group created/updated.'))
