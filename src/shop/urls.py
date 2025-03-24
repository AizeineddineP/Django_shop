from django.urls import path
from shop.views import first_view, second_view, home, marketplace

#from src.shop.views import second_view

urlpatterns = [
    path('hello/', first_view),
    path('task/', second_view),
    path('home/', home),
    path('marketplace/', marketplace),
]