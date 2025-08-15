from django.shortcuts import render
from .models import Product

def home_view(request):
    latest = Product.objects.order_by('-created_at')[:5]
    # Доп. задание: вывести в консоль
    print('[LATEST 5 PRODUCTS]', list(latest.values('id', 'name', 'price', 'created_at')))
    return render(request, 'catalog/home.html', {'latest_products': latest})

def catalog_view(request):
    return render(request, 'catalog/catalog.html')

def category_view(request):
    return render(request, 'catalog/category.html')

def contacts_view(request):
    sent = False
    name = None
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"[CONTACT FORM] Имя: {name} | Телефон: {phone} | Сообщение: {message}")
        sent = True
    context = {'sent': sent, 'name': name}
    return render(request, 'catalog/contacts.html', context)
