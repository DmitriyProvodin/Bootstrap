from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson
User = get_user_model()

class LessonCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='owner@example.com', password='pass123')
        self.other = User.objects.create_user(email='other@example.com', password='pass123')
        self.course = Course.objects.create(title='C1', description='d', price=1.0, owner=self.user)
        self.lesson = Lesson.objects.create(course=self.course, title='L1', description='d', owner=self.user)

    def test_create_lesson(self):
        self.client.force_authenticate(self.user)
        url = reverse('courses:lesson-list')
        resp = self.client.post(url, {'course': self.course.id, 'title': 'New', 'description': 'x'})
        self.assertEqual(resp.status_code, 201)

    def test_list_lessons(self):
        self.client.force_authenticate(self.user)
        url = reverse('courses:lesson-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('results' in resp.data)

    def test_retrieve_lesson(self):
        self.client.force_authenticate(self.user)
        url = reverse('courses:lesson-detail', args=[self.lesson.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['title'], 'L1')

    def test_update_by_owner(self):
        self.client.force_authenticate(self.user)
        url = reverse('courses:lesson-detail', args=[self.lesson.id])
        resp = self.client.patch(url, {'title': 'Updated'})
        self.assertEqual(resp.status_code, 200)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated')

    def test_update_by_non_owner(self):
        self.client.force_authenticate(self.other)
        url = reverse('courses:lesson-detail', args=[self.lesson.id])
        resp = self.client.patch(url, {'title': 'Hacked'})
        self.assertIn(resp.status_code, (403,404))

    def test_delete_by_owner(self):
        self.client.force_authenticate(self.user)
        url = reverse('courses:lesson-detail', args=[self.lesson.id])
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    def test_delete_by_non_owner(self):
        self.client.force_authenticate(self.other)
        url = reverse('courses:lesson-detail', args=[self.lesson.id])
        resp = self.client.delete(url)
        self.assertIn(resp.status_code, (403,404))
