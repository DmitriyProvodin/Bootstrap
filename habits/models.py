from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=200)
    time = models.TimeField()
    action = models.CharField(max_length=300)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    periodicity_days = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=200, blank=True)
    duration_seconds = models.PositiveIntegerField(default=60)
    is_public = models.BooleanField(default=False)
    last_performed = models.DateTimeField(null=True, blank=True)
    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError('Cannot set both reward and related_habit')
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError('Pleasant habit cannot have reward or related_habit')
        if self.duration_seconds > 120:
            raise ValidationError('Duration cannot exceed 120 seconds')
        if self.periodicity_days < 1 or self.periodicity_days > 7:
            raise ValidationError('Periodicity must be between 1 and 7 days')
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError('Related habit must be pleasant')
    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.user.email}: {self.action} at {self.time}"
