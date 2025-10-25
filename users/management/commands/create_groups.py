from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from courses.models import Course, Lesson

class Command(BaseCommand):
    help = "Create 'moderators' group with change permissions for Course and Lesson"
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='moderators')
        content_course = ContentType.objects.get_for_model(Course)
        content_lesson = ContentType.objects.get_for_model(Lesson)
        perms = []
        for codename in ['change_course']:
            try:
                perms.append(Permission.objects.get(content_type=content_course, codename=codename))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Permission {codename} not found'))
        for codename in ['change_lesson']:
            try:
                perms.append(Permission.objects.get(content_type=content_lesson, codename=codename))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Permission {codename} not found'))
        group.permissions.set(perms)
        group.save()
        self.stdout.write(self.style.SUCCESS("Group 'moderators' created/updated"))
