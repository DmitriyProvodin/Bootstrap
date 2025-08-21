
from django.shortcuts import render
from .models import Product

def home(request):
    latest = Product.objects.order_by("-created_at")[:5]
    print("Последние продукты:", list(latest))
    return render(request, "home.html", {"latest": latest})

def contacts(request):
    return render(request, "contacts.html")
