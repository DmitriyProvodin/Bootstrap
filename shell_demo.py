
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")
django.setup()

from catalog.models import Category, Product

os.makedirs("screenshots", exist_ok=True)
log_path = os.path.join("screenshots", "log.txt")
open(log_path, "w").close()

def log(msg):
    print(msg)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

cat1 = Category.objects.create(name="Смартфоны", description="Мобильные устройства")
cat2 = Category.objects.create(name="Ноутбуки", description="Персональные компьютеры")
log("Созданы категории: Смартфоны, Ноутбуки")

prod1 = Product.objects.create(name="iPhone 15", description="Флагманский смартфон", price=1000, category=cat1)
prod2 = Product.objects.create(name="MacBook Air", description="Тонкий ноутбук", price=2000, category=cat2)
log("Созданы продукты: iPhone 15, MacBook Air")

log("==== Все категории ====")
for c in Category.objects.all():
    log(str(c))

log("==== Все продукты ====")
for p in Product.objects.all():
    log(str(p))

log("==== Продукты в категории Смартфоны ====")
for p in Product.objects.filter(category=cat1):
    log(str(p))

prod1.price = 1200
prod1.save()
log(f"Цена {prod1.name} обновлена до {prod1.price}")

prod2.delete()
log("Продукт MacBook Air удален")
