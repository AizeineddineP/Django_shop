from django.utils.translation import gettext_lazy as _
from django.db import models
from shop.models.base import TimeConfig

class ProductCategory(models.TextChoices):
    TECHNIQUE = "TQ", _("Technique")
    BOOK = "BK", _("Book")
    FURNITURE = "FR", _("Furniture")
    SPORT = "SP", _("Sport")
    Toy = "TY", _("Toy")
    DEFAULT = "DF", _("Default")

class Product(TimeConfig):
    name = models.CharField(max_length=30,verbose_name="продукт")
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="описание")
    price = models.FloatField(verbose_name="цена")
    is_available = models.BooleanField(default=True,verbose_name="в наличии?")
    category = models.CharField(
        choices= ProductCategory,
        default=ProductCategory.DEFAULT,
        verbose_name="категория"
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        verbose_name="фото")
    count_items = models.IntegerField(default=10,verbose_name="количество")


    provider = models.ForeignKey(
        to="Provider",
        on_delete=models.SET_NULL,
        related_name="products",
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.name}"