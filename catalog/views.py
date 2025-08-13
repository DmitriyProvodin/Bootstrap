from django.shortcuts import render

def home_view(request):
    return render(request, 'catalog/home.html')

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
