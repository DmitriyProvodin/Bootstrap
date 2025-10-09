from django.test import TestCase
from django.contrib.auth import get_user_model
from mailings.models import Recipient, Message, Mailing

User = get_user_model()

class BasicTest(TestCase):
    def setUp(self):
        u = User.objects.create_user(email='a@a.com', password='p')
        r = Recipient.objects.create(email='r@r.com', full_name='R', owner=u)
        m = Message.objects.create(subject='S', body='B', owner=u)
        Mailing.objects.create(start_time='2023-01-01T00:00:00Z', end_time='2023-12-01T00:00:00Z', message=m, owner=u)
    def test_counts(self):
        self.assertEqual(Recipient.objects.count(),1)
