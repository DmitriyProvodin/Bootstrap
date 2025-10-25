from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [('cash','Cash'),('transfer','Bank transfer')]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='payments')
    paid_at = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, blank=True, null=True, related_name='payments')
    lesson = models.ForeignKey('courses.Lesson', on_delete=models.SET_NULL, blank=True, null=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    def __str__(self):
        target = self.course.title if self.course else (self.lesson.title if self.lesson else 'Unknown')
        return f"Payment {self.id} by {self.user.email} for {target}"
