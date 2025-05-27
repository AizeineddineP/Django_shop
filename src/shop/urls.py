from django.urls import path
from shop.views import HomeView, ProductView, info, UserOrdersListViews, ProductCreateView
from django.views.decorators.cache import cache_page



#first_view, second_view, first_html,
#from src.shop.views import second_view

urlpatterns = [
    #path('hello/', first_view),
    #path('task/', second_view),
    #path('hi/first_html', first_html),

    path("",HomeView, name='home'),
    path("about/", info, name='info'),
    #path('marketplace/', marketplace),
    path("products/", cache_page(60)(ProductView.as_view()), name='products'),
    #path("users/", users_view, name='users')
    path("user_orders/", UserOrdersListViews.as_view(), name='user_orders'),
    path("add_product/", ProductCreateView.as_view(), name='product_form'),

]