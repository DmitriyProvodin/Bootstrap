from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                 # /
    path('catalog/', views.catalog_view, name='catalog'),   # /catalog/
    path('category/', views.category_view, name='category'),# /category/
    path('contacts/', views.contacts_view, name='contacts') # /contacts/
]
