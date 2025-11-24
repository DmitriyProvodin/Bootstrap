import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from habits.models import Habit

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_habit_creation(authenticated_user):
    client, user = authenticated_user
    response = client.post(reverse('habit-list'), {
        'name': 'Drink water',
        'description': 'Drink 2 litres of water'
    })
    assert response.status_code == 201
    assert Habit.objects.filter(name='Drink water', user=user).exists()


@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(username='tester', password='pass1234')
    client = APIClient()
    client.login(username='tester', password='pass1234')
    return client, user


@pytest.mark.django_db
def test_habit_list(authenticated_user):
    client, user = authenticated_user
    Habit.objects.create(name='Run', user=user)
    Habit.objects.create(name='Read', user=user)
    response = client.get(reverse('habit-list'))
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_record_creation(authenticated_user):
    client, user = authenticated_user
    habit = Habit.objects.create(name='Meditation', user=user)
    response = client.post(reverse('record-list'), {
        'habit': habit.id,
        'value': 1
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_record_statistics(authenticated_user):
    client, user = authenticated_user
    habit = Habit.objects.create(name='Coding', user=user)

    response = client.get(reverse('record-statistics', args=[habit.id]))
    assert response.status_code == 200
    data = response.json()
    assert data['total'] == 3
    assert data['count'] == 2
