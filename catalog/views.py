from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)
from .models import Product
from .forms import ProductForm

class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.select_related('category').order_by('-created_at')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
