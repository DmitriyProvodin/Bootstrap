import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User
from habits.models import Habit

@pytest.mark.django_db
def test_public_habits_list():
    client = APIClient()
    user = User.objects.create_user(email="test@example.com", password="12345")
    client.force_authenticate(user)

    Habit.objects.create(
        owner=user, place="Парк", time="18:00:00", action="Бег", is_public=True
    )
    Habit.objects.create(
        owner=user, place="Дом", time="10:00:00", action="Чтение", is_public=False
    )

    url = reverse("habits:public")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
