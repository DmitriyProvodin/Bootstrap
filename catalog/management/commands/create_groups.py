from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
from blog.models import Post

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **options):
        product_ct = ContentType.objects.get_for_model(Product)
        try:
            perm_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=product_ct)
        except Permission.DoesNotExist:
            perm_unpublish = None
        perm_delete = Permission.objects.get(codename='delete_product', content_type=product_ct)

        mod_group, _ = Group.objects.get_or_create(name='Модератор продуктов')
        if perm_unpublish:
            mod_group.permissions.add(perm_unpublish)
        mod_group.permissions.add(perm_delete)

        blog_ct = ContentType.objects.get_for_model(Post)
        add_post = Permission.objects.get(codename='add_post', content_type=blog_ct)
        change_post = Permission.objects.get(codename='change_post', content_type=blog_ct)
        delete_post = Permission.objects.get(codename='delete_post', content_type=blog_ct)
        content_group, _ = Group.objects.get_or_create(name='Контент-менеджер')
        content_group.permissions.add(add_post, change_post, delete_post)

        self.stdout.write(self.style.SUCCESS('Groups created/updated.'))
