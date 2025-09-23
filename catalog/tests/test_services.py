from django.test import TestCase
from catalog.models import Category, Product

class ServicesTest(TestCase):
    def setUp(self):
        c = Category.objects.create(name='Cat')
        Product.objects.create(name='P1', description='d', price=10, category=c, is_published=True)
        Product.objects.create(name='P2', description='d', price=20, category=c, is_published=False)

    def test_get_products_by_category(self):
        from catalog.services import get_products_by_category
        c = Category.objects.first()
        qs = get_products_by_category(c.id)
        self.assertEqual(qs.count(), 1)
