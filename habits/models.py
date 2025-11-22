from django.db import models
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits"
    )
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)

    is_pleasant = models.BooleanField(default=False)

    linked_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="pleasant_for",
    )

    period = models.PositiveSmallIntegerField(default=1)  # 1–7 дней
    reward = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveSmallIntegerField()  # секунды
    is_public = models.BooleanField(default=False)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.action} — {self.user.email}"
