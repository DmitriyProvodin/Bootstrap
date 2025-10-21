from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateView, LessonDetailView
app_name = 'courses'
router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
urlpatterns = [path('', include(router.urls)), path('lessons/', LessonListCreateView.as_view(), name='lesson-list'), path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail')]
