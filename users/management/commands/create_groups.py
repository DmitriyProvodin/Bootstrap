from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create moderators group with change permissions for Course and Lesson (no add/delete)'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='moderators')
        ct_course = ContentType.objects.filter(model='course').first()
        ct_lesson = ContentType.objects.filter(model='lesson').first()
        perms = []
        if ct_course:
            p = Permission.objects.filter(content_type=ct_course, codename__startswith='change')
            perms += list(p)
        if ct_lesson:
            p = Permission.objects.filter(content_type=ct_lesson, codename__startswith='change')
            perms += list(p)
        group.permissions.set(perms)
        group.save()
        self.stdout.write(self.style.SUCCESS("Group 'moderators' created/updated"))
