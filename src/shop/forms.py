from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=20,label="Продукт")
    price = forms.IntegerField(label="Цена")
    count_items = forms.IntegerField(label="Количество")