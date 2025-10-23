from rest_framework import viewsets, permissions
from .models import User, Payment
from .serializers import UserProfileSerializer, PaymentSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('user', 'course', 'lesson').all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]

    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['paid_at']
    ordering = ['-paid_at']
