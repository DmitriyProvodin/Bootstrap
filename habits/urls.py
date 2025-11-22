from django.urls import path
from .views import (
    HabitListView,
    PublicHabitListView,
    HabitCreateView,
    HabitDetailView,
)

urlpatterns = [
    path("", HabitListView.as_view(), name="my_habits"),
    path("public/", PublicHabitListView.as_view(), name="public_habits"),
    path("create/", HabitCreateView.as_view(), name="habit_create"),
    path("<int:pk>/", HabitDetailView.as_view(), name="habit_detail"),
]
