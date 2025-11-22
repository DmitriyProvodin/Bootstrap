import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User
from habits.models import Habit

@pytest.mark.django_db
class TestHabitCRUD:

    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@example.com", password="12345")
        self.client.force_authenticate(self.user)

    def test_create_habit(self):
        url = reverse("habits:create")
        data = {
            "place": "Дом",
            "time": "19:00:00",
            "action": "Прогулка",
            "is_pleasant": False,
            "reward": "Торт",
            "duration": "00:01:00",
            "periodicity": 1,
            "is_public": False
        }
        response = self.client.post(url, data)
        assert response.status_code == 201
        assert Habit.objects.count() == 1

    def test_list_own_habits(self):
        Habit.objects.create(
            owner=self.user,
            place="Улица",
            time="08:00:00",
            action="Зарядка"
        )
        url = reverse("habits:list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_update_habit(self):
        habit = Habit.objects.create(
            owner=self.user, place="Дом", time="09:00:00", action="Чтение"
        )
        url = reverse("habits:update", args=[habit.id])
        response = self.client.patch(url, {"action": "Медитация"})
        assert response.status_code == 200
        habit.refresh_from_db()
        assert habit.action == "Медитация"

    def test_delete_habit(self):
        habit = Habit.objects.create(
            owner=self.user, place="Парк", time="10:00:00", action="Бег"
        )
        url = reverse("habits:delete", args=[habit.id])
        response = self.client.delete(url)
        assert response.status_code == 204
        assert Habit.objects.count() == 0
