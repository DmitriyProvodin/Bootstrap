from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Product, Category
from .forms import ProductForm
from .services import get_products_by_category

class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6
    def get_queryset(self):
        cache_key = 'products_list'
        products = cache.get(cache_key)
        if not products:
            products = Product.objects.select_related('category').order_by('-created_at')
            cache.set(cache_key, products, 60*5)
        return products

@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'
    def get_queryset(self):
        return get_products_by_category(self.kwargs.get('category_id'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs.get('category_id'))
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class UnpublishProductView(PermissionRequiredMixin, TemplateView):
    permission_required = 'catalog.can_unpublish_product'
    template_name = 'catalog/unpublish_result.html'
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = Product.objects.filter(pk=pk).first()
        if obj:
            obj.is_published = False
            obj.save()
        return redirect('catalog:product_detail', pk=pk)
