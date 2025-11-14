from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='courses/', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    preview = models.ImageField(upload_to='lessons/', blank=True, null=True)
    video_url = models.URLField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lessons')
    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='subscriptions')
    class Meta:
        unique_together = ('user', 'course')
    def __str__(self):
        return f"Subscription: {self.user.email} -> {self.course.title}"
