from django.urls import path
from shop.views import home, products_view, users_view, info

#first_view, second_view, first_html,
#from src.shop.views import second_view

urlpatterns = [
    #path('hello/', first_view),
    #path('task/', second_view),
    #path('hi/first_html', first_html),

    path("", home, name='home'),
    path("about/", info, name='info'),
    #path('marketplace/', marketplace),
    path("products/", products_view, name='products'),
    path("users/", users_view, name='users')
]