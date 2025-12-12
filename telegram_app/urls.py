from django.urls import path
from . import views
urlpatterns = [
    path('register_webhook/', views.register_webhook),
]
