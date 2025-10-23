from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, PaymentViewSet

app_name = 'users'
router = DefaultRouter()
router.register('profiles', UserProfileViewSet, basename='profile')
router.register('payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
