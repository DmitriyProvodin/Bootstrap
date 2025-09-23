from django.test import TestCase, override_settings, Client
from django.core.cache import cache
from catalog.models import Category, Product

class CacheTest(TestCase):
    def setUp(self):
        c = Category.objects.create(name='Cat')
        Product.objects.create(name='P1', description='d', price=10, category=c, is_published=True)
        self.client = Client()

    def test_home_cache(self):
        cache.clear()
        resp1 = self.client.get('/')
        resp2 = self.client.get('/')
        self.assertEqual(resp1.content, resp2.content)
