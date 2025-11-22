from rest_framework import generics, permissions
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwner
from .paginators import HabitPagination
from .tasks import send_habit_reminder


class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        send_habit_reminder.delay(habit.id)


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        habit = serializer.save()
        send_habit_reminder.delay(habit.id)
