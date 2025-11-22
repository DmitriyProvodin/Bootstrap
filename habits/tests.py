from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from habits.models import Habit


User = get_user_model()


class HabitTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="12345")
        self.client.force_authenticate(self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="12:00",
            action="Пить воду",
            duration=60,
            period=1
        )

    def test_list(self):
        url = reverse("my_habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = reverse("habit_create")
        data = {
            "place": "Парк",
            "time": "08:00",
            "action": "Прогулка",
            "duration": 90,
            "period": 1,
            "is_public": True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        url = reverse("habit_detail", args=[self.habit.id])
        data = {"action": "Пить воду утром"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = reverse("habit_detail", args=[self.habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
