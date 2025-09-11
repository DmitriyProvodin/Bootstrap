from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Load test fixtures (categories, products, blog posts)'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        BlogPost.objects.all().delete()
        self.stdout.write('Loading fixtures...')
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')
        call_command('loaddata', 'blog_fixtures.json')
        self.stdout.write(self.style.SUCCESS('Test data loaded.'))
