import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User

@pytest.mark.django_db
class TestAuth:

    def setup_method(self):
        self.client = APIClient()

    def test_registration(self):
        url = reverse("users:register")
        data = {
            "email": "newuser@mail.com",
            "password": "12345678"
        }
        response = self.client.post(url, data)
        assert response.status_code == 201
        assert User.objects.filter(email="newuser@mail.com").exists()

    def test_login(self):
        User.objects.create_user(email="user@mail.com", password="12345678")
        url = reverse("token_obtain_pair")
        response = self.client.post(url, {
            "email": "user@mail.com",
            "password": "12345678"
        })
        assert response.status_code == 200
        assert "access" in response.data
