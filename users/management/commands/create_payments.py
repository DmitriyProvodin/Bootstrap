from django.core.management.base import BaseCommand
from users.models import User, Payment
from courses.models import Course, Lesson
from decimal import Decimal
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create sample payments for testing'

    def handle(self, *args, **options):
        users = list(User.objects.all()[:3])
        courses = list(Course.objects.all()[:3])
        lessons = list(Lesson.objects.all()[:3])
        if not users:
            self.stdout.write(self.style.ERROR('No users present - create users first'))
            return
        for i, u in enumerate(users):
            c = courses[i % len(courses)] if courses else None
            l = lessons[i % len(lessons)] if lessons else None
            Payment.objects.create(user=u, course=c, lesson=l, amount=Decimal('19.90'), method='cash', paid_at=timezone.now())
        self.stdout.write(self.style.SUCCESS('Sample payments created'))
