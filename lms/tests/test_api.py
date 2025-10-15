from django.test import TestCase
from rest_framework.test import APIClient

class ApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_courses_crud(self):
        r = self.client.post('/api/courses/', {'title':'C1','description':'d'}, format='json')
        self.assertEqual(r.status_code, 201)
        cid = r.json()['id']
        r = self.client.get('/api/courses/')
        self.assertEqual(r.status_code, 200)
        r = self.client.get(f'/api/courses/{cid}/')
        self.assertEqual(r.status_code, 200)
