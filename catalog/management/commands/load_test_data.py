
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Загрузка тестовых данных (очищает БД перед вставкой)"

    def handle(self, *args, **options):
        self.stdout.write("Очищаю данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat1 = Category.objects.create(name="Смартфоны", description="Мобильные устройства")
        cat2 = Category.objects.create(name="Ноутбуки", description="Персональные компьютеры")

        Product.objects.create(name="iPhone 15", description="Флагманский смартфон", price=1200, category=cat1)
        Product.objects.create(name="MacBook Air", description="Тонкий ноутбук", price=2000, category=cat2)

        self.stdout.write(self.style.SUCCESS("✅ Данные загружены"))
