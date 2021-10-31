from django.contrib import admin
from .models import Product, Store



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ("store", "name", "desc", "category", "price", "discount", "quantity", "tags", "rating", "date_created", "is_stocked")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ("vendor", "name", "category", "sdg_goals")