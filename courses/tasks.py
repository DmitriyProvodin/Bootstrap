from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Course
@shared_task
def send_course_update_emails(course_id):
    course = Course.objects.get(id=course_id)
    if timezone.now() - course.updated_at < timedelta(hours=4):
        return {'skipped': True}
    subs = course.subscriptions.select_related('user').all()
    sent = 0
    for sub in subs:
        send_mail('Course updated', f'Course {course.title} updated', 'noreply@example.com', [sub.user.email], fail_silently=True)
        sent += 1
    return {'sent': sent}
