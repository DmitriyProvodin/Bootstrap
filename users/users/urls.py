from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('profiles/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('payments/', views.PaymentListView.as_view(), name='payments'),
]
