from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_duration_seconds(value):
    if value > 120:
        raise ValidationError('Время выполнения не должно быть больше 120 секунд.')

class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_rewarding = models.BooleanField(default=False)
    related = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='related_to')
    periodicity_days = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True)
    duration_seconds = models.PositiveIntegerField(default=60, validators=[validate_duration_seconds])
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.reward and self.related:
            raise ValidationError('Нельзя указывать одновременно reward и related.')
        if self.is_rewarding and (self.reward or self.related):
            raise ValidationError('У приятной привычки не может быть reward или related.')
        if self.periodicity_days < 1:
            raise ValidationError('Периодичность не может быть меньше 1 дня.')
        if self.periodicity_days > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем раз в 7 дней.')
        if self.related and not self.related.is_rewarding:
            raise ValidationError('Связанная привычка должна быть приятной.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.owner.username}: {self.action} at {self.time}'
