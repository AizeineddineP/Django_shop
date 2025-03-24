from django.urls import path
from shop.views import first_view, home, marketplace

urlpatterns = [
    path('hello/', first_view),
    path('home/', home),
    path('marketplace/', marketplace),
]