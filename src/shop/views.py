# Create your views here.
#MTV
#Model = table db
#Template = html
#Views = controller

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def first_view(request):
    return HttpResponse("<h1>Hello Django<h1\>")

def second_view(request):
    return HttpResponse("<h1>First task on Django<h1\>")

def first_html(request):
    return render(request, 'hi.html')

# Главная страница
def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, "info.html")
def marketplace(request):
    return render(request, 'marketplace.html', {"title": 'Маркетплейс'})

# Страница с товарами
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Данные о пользователях
users = [
    {"name": "Alice", "age": 22, "phone": "+123456789", "photo": "shop/image/alice.jpg"},
    {"name": "Bob", "age": 30, "phone": "+987654321", "photo": "shop/image/bob.jpg"},
    {"name": "Charlie", "age": 25, "phone": "+192837465", "photo": "shop/image/charlie.jpg"},
]
# Страница с пользователями
def users_view(request):
    return render(request, "users.html", {"users": users})
