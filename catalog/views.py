from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts(request):
    return render(request, 'catalog/contacts.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
