from django.urls import path, include

urlpatterns = [
    path('api/habits/', include('habits.urls')),
    path('api/telegram/', include('telegram_app.urls')),
]
