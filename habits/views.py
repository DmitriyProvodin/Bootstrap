from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer
from .paginators import SmallPageNumberPagination
from rest_framework.response import Response
class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallPageNumberPagination
    def get_queryset(self):
        if self.request.method == 'GET' and self.request.query_params.get('public') in ('1','true','True'):
            return Habit.objects.filter(is_public=True)
        return Habit.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
