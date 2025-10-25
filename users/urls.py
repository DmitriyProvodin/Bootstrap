from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserRegistrationView, PaymentViewSet
app_name = 'users'
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('payments', PaymentViewSet, basename='payment')
urlpatterns = [path('', include(router.urls)), path('register/', UserRegistrationView.as_view(), name='register'),]
