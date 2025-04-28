from django.contrib import admin
from django.db.models import F

from shop.models import (
     Product,
     ProductRating,
     Order,
)



class ProductOrderInline(admin.TabularInline):
    model = Order.product.through


class ProductRatingInline(admin.TabularInline):
    model = ProductRating

@admin.action(description="Mark selected discount 5 percent")
def make_discount(modeladmin, request, queryset):
    queryset.update(price = F("price") * 0.95)



class ProductAdmin(admin.ModelAdmin):
    # fields = ("name","description","photo",("price","count_items"))

     fieldsets = [
          (
               None,
               {
                    "fields" : ["name", "provider", ("price", "count_items")],
               },

          ),
          (
               "Advanced options",
               {
                 "classes": ["collapse"],
                 "fields": ["description","photo"],
               },
          ),
     ]
     list_display = ("name","description","price","category","photo","count_items","is_available")
     list_display_links = ("name","category")
     list_editable = ("price","count_items","is_available")
     list_per_page = 4
     list_filter = ("category","is_available" )
     search_fields = ("name","description","price","category","photo","count_items","is_available")
     ordering = ("-price","name")
     #save_on_top = True
     #readonly_fields = ("description",)
     inlines = [
         ProductRatingInline,
         ProductOrderInline,

     ]
     actions = (
         make_discount,

     )

product_admin = admin.site.register(Product,ProductAdmin)


from shop.models import (
     Order,
     ProductDetail,
     ProductOrder,
     Provider,
     Feedback,
     Rating,
     ProductRating,
     ProviderRating
)
# Register your models here.
admin.site.register(Order)
admin.site.register(ProductDetail)
admin.site.register(ProductOrder)
admin.site.register(Provider)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(ProductRating)
admin.site.register(ProviderRating)