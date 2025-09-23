from django.test import TestCase, Client
from catalog.models import Category, Product

class ProductPageCacheTest(TestCase):
    def setUp(self):
        c = Category.objects.create(name='Cat')
        p = Product.objects.create(name='P1', description='d', price=10, category=c, is_published=True)
        self.client = Client()
        self.url = f'/product/{p.pk}/'

    def test_product_page_cached(self):
        r1 = self.client.get(self.url)
        r2 = self.client.get(self.url)
        self.assertEqual(r1.content, r2.content)
