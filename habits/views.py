from rest_framework import viewsets, permissions, filters
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['action','place','reward']

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)

    @action(detail=False, methods=['get'], url_path='public', permission_classes=[permissions.AllowAny])
    def list_public(self, request):
        qs = Habit.objects.filter(is_public=True)
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
