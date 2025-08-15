from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Очистить БД и загрузить тестовые данные из фикстур"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Удаляю старые данные..."))
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Старые данные удалены."))

        self.stdout.write(self.style.WARNING("Загружаю фикстуры..."))
        call_command('loaddata', 'categories.json', app_label='catalog')
        call_command('loaddata', 'products.json', app_label='catalog')
        self.stdout.write(self.style.SUCCESS("Готово!"))
