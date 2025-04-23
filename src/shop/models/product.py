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
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    category = models.CharField(
        choices= ProductCategory,
        default=ProductCategory.DEFAULT
    )
    photo = models.ImageField(null=True, blank=True)
    count_items = models.IntegerField(default=10)


    provider = models.ForeignKey(
        to="Provider",
        on_delete=models.SET_NULL,
        related_name="products",
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.name} count:{self.count_items}"