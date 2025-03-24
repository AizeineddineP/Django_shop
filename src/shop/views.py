from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return HttpResponse("<h1>Hello Django<h1\>")

def home(request):
    return render(request, 'home.html', {'title': 'Главная страница'})

def marketplace(request):
    return render(request, 'marketplace.html', {'title': 'Маркетплейс'})

# Create your views here.
#MTV
#Model = table db
#Template = html
#Views = controller
