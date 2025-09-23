from django.urls import path
from .views import HomeView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView, UnpublishProductView, CategoryProductsView
app_name = 'catalog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
]
