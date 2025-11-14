from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Course

@shared_task
def send_course_update_emails(course_id):
    course = Course.objects.get(id=course_id)
    # if updated less than 4 hours ago - skip
    if timezone.now() - course.updated_at < timedelta(hours=4):
        return {'skipped': True}
    subs = course.subscriptions.select_related('user').all()
    sent = 0
    for sub in subs:
        try:
            send_mail(
                subject=f'Course updated: {course.title}',
                message=f'Course "{course.title}" was updated. Check new materials.',
                from_email='noreply@example.com',
                recipient_list=[sub.user.email],
                fail_silently=True,
            )
            sent += 1
        except Exception:
            continue
    return {'sent': sent}
