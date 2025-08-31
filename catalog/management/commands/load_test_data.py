from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Загружает тестовые данные (категории и продукты)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляю старые данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загружаю фикстуры...")
        call_command("loaddata", "categories.json")
        call_command("loaddata", "products.json")

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены!"))
