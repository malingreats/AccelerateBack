from django.contrib import admin
from .models import Product, Store, Service


# from rest_framework_simplejwt.token_blacklist import models
# from rest_framework_simplejwt import token_blacklist

# class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

#     def has_delete_permission(self, *args, **kwargs):
#         return True # or whatever logic you want

# admin.site.unregister(token_blacklist.models.OutstandingToken)
# admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ("store", "id","name", "desc", "category", "price", "discount", "quantity", "tags", "rating", "date_created", "is_stocked")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ("store", "id","name", "desc", "category", "price", "discount", "tags", "rating", "date_created", "availability", "service_image")



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ( "id", "vendor", "name", "category", "sdg_goals")