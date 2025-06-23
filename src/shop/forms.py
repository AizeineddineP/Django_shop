from django import forms
from django.forms import Textarea, ModelForm
from shop.models import Product
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=20,label="Продукт")
#     price = forms.IntegerField(label="Цена")
#     count_items = forms.IntegerField(label="Количество")
def positive_integer_field_validator(value):
    return value > 0

class ProductModelForm(forms.ModelForm):
    class Meta:
       model=Product
       fields = ("name","price","count_items","description","photo")
       widgets = {
            "description": Textarea(attrs={"cols": 20, "rows": 5}),
        }
       validators = {
           'count_items': [
               positive_integer_field_validator
           ]
       }