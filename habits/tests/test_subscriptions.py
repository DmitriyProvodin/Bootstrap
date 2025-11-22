import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User
from habits.models import Habit, Subscription

@pytest.mark.django_db
def test_subscription_toggle():
    client = APIClient()
    user = User.objects.create_user(email="test@example.com", password="12345")
    client.force_authenticate(user)
    habit = Habit.objects.create(
        owner=user, place="Дом", time="19:00:00", action="Чтение"
    )

    url = reverse("habits:subscribe")

    # Добавление
    response = client.post(url, {"habit_id": habit.id})
    assert response.status_code == 200
    assert Subscription.objects.count() == 1

    # Удаление
    response = client.post(url, {"habit_id": habit.id})
    assert response.status_code == 200
    assert Subscription.objects.count() == 0
