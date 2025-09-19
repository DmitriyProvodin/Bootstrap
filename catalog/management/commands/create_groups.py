from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
class Command(BaseCommand):
    help = 'Create groups and assign permissions (moderator group)'
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        content_type = ContentType.objects.get_for_model(Product)
        try:
            perm_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
            group.permissions.add(perm_unpublish)
        except Permission.DoesNotExist:
            self.stdout.write(self.style.WARNING('Permission can_unpublish_product does not exist. Run makemigrations and migrate first.'))
        try:
            perm_delete = Permission.objects.get(codename='delete_product', content_type=content_type)
            group.permissions.add(perm_delete)
        except Permission.DoesNotExist:
            self.stdout.write(self.style.WARNING('Permission delete_product not found.'))
        self.stdout.write(self.style.SUCCESS('Group "Модератор продуктов" created/updated.'))
