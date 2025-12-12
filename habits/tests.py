from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Habit
from django.core.exceptions import ValidationError

User = get_user_model()

class HabitModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')

    def test_reward_and_related_cannot_both_be_set(self):
        r = Habit.objects.create(owner=self.user, place='home', time='12:00', action='rel', is_rewarding=True, periodicity_days=1)
        h = Habit(owner=self.user, place='home', time='12:00', action='act', periodicity_days=1, reward='cake', duration_seconds=30)
        h.related = r
        with self.assertRaises(ValidationError):
            h.full_clean()

    def test_duration_limit(self):
        h = Habit(owner=self.user, place='x', time='12:00', action='a', periodicity_days=1, duration_seconds=121)
        with self.assertRaises(ValidationError):
            h.full_clean()

    def test_periodicity_limits(self):
        h = Habit(owner=self.user, place='x', time='12:00', action='a', periodicity_days=8, duration_seconds=30)
        with self.assertRaises(ValidationError):
            h.full_clean()
