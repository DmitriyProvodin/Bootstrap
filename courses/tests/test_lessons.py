from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from courses.models import Lesson, Course

User = get_user_model()


class LessonCRUDTestCase(APITestCase):
    def setUp(self):
        # a) Создаем пользователя и курс
        self.user = User.objects.create_user(
            email="user@test.com", password="testpass"
        )
        self.course = Course.objects.create(
            title="Django Course", description="Basic Django"
        )
        self.client.force_authenticate(user=self.user)

        # b) Создаем тестовый урок
        self.lesson = Lesson.objects.create(
            title="Intro", description="Lesson 1", course=self.course, owner=self.user
        )

    def test_create_lesson(self):
        """A. Проверяем создание урока"""
        data = {
            "title": "New lesson",
            "description": "Description",
            "course": self.course.id,
        }
        response = self.client.post("/api/lessons/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lessons(self):
        """B. Проверяем получение списка уроков"""
        response = self.client.get("/api/lessons/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_retrieve_lesson(self):
        """C. Проверяем получение одного урока"""
        response = self.client.get(f"/api/lessons/{self.lesson.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Intro")

    def test_update_lesson(self):
        """D. Проверяем обновление урока"""
        data = {"title": "Updated title"}
        response = self.client.patch(f"/api/lessons/{self.lesson.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated title")

    def test_delete_lesson(self):
        """E. Проверяем удаление урока"""
        response = self.client.delete(f"/api/lessons/{self.lesson.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())
