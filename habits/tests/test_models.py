from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Habit
User = get_user_model()
class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='a@b.com', password='pass')
    def test_valid_habit(self):
        h = Habit.objects.create(user=self.user, place='home', time='12:00', action='stretch', periodicity_days=1)
        self.assertEqual(h.action, 'stretch')
    def test_invalid_duration(self):
        with self.assertRaises(Exception):
            Habit.objects.create(user=self.user, place='home', time='12:00', action='x', duration_seconds=200)
