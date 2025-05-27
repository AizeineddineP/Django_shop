# Create your views here.
#MTV
#Model = table db
#Template = html
#Views = controller

from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Product
from authentication.models import CustomUser
from shop.forms import ProductModelForm
from shop.models.product import Product, ProductCategory
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache


# Главная страница
def HomeView(request):
    featured_products = Product.objects.filter(is_available=True)
    categories = [(cat.value, cat.label) for cat in ProductCategory]
    return render(request, 'shop/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })


def info(request):
    return render(request, "info.html")
def marketplace(request):
    return render(request, "marketplace.html", {"title": 'Маркетплейс'})

# Страница с товарами
# def products_view(request):
#     products = Product.objects.all()
#     return render(request, "products.html", {"products": products})

class ProductView(ListView):
    template_name = "products.html"
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

# Данные о пользователях
#users = [
    #{"name": "Alice", "age": 22, "phone": "+123456789", "photo": "shop/image/alice.jpg"},
    #"name": "Bob", "age": 30, "phone": "+987654321", "photo": "shop/image/bob.jpg"},
    #{"name": "Charlie", "age": 25, "phone": "+192837465", "photo": "shop/image/charlie.jpg"},
#]
# Страница с пользователями
#def users_view(request):
    #return render(request, "users.html", {"users": users})

# Страница с заказами

class UserOrdersListViews(ListView):
    template_name = "user_order_products.html"
    queryset =  CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')
        return context

# def user_orders(request):
#     users = CustomUser.objects.all().prefetch_related('orders', 'orders__product')
#     context = {
#         "users": users
#     }
#     return render(request, "user_order_products.html", context=context)


# @login_required(login_url="/auth/login/", redirect_field_name="product_form")
# @permission_required(perm="shop.add_product", raise_exception=True)
# @cache_page(60 * 5, cache="default")
# def product_form(request):
#     context = {}
#     if request.method == "POST":
#         form = ProductModelForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             caches["default"].clear()
#             return redirect(reverse("products"))
#         context["form"] = form
#     context["form"] = ProductModelForm()
#
#     return render(request, template_name="product_form.html", context=context)

class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = "product_form.html"
    model = Product
    # form_class = ProductModelForm
    fields = ["name","price","count_items","description","photo"]
    success_url = reverse_lazy("products")
    permission_required = ["shop.add_product"]
    # redirect_field_name = "product"
