from rest_framework import viewsets, permissions, generics
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer, UserSerializer
User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
