from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson, Subscription

User = get_user_model()

class LessonsAndSubscriptionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(email='u1@example.com', password='pass123')
        self.user2 = User.objects.create_user(email='u2@example.com', password='pass123')
        self.course1 = Course.objects.create(title='Course 1', description='desc', owner=self.user1)
        self.lesson1 = Lesson.objects.create(course=self.course1, title='Lesson 1', description='l1', owner=self.user1)

    def test_lesson_update_by_owner(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('courses:lesson-detail', args=[self.lesson1.pk])
        resp = self.client.patch(url, {'title':'Updated'}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.lesson1.refresh_from_db()
        self.assertEqual(self.lesson1.title, 'Updated')

    def test_lesson_update_by_non_owner(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('courses:lesson-detail', args=[self.lesson1.pk])
        resp = self.client.patch(url, {'title':'Bad'}, format='json')
        self.assertIn(resp.status_code, (403,404))

    def test_subscription_toggle(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('courses:subscriptions')
        resp = self.client.post(url, {'course': self.course1.pk}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Subscription.objects.filter(user=self.user2, course=self.course1).count(), 1)
        resp = self.client.post(url, {'course': self.course1.pk}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Subscription.objects.filter(user=self.user2, course=self.course1).count(), 0)
