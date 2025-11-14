from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, SubscriptionAPIView
app_name = 'courses'
router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('lessons', LessonViewSet, basename='lesson')
urlpatterns = [path('', include(router.urls)), path('subscriptions/', SubscriptionAPIView.as_view(), name='subscriptions'),]
