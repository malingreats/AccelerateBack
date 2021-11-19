from django.contrib import admin
from .models import Product, Store, Service, StoreOrder, VendorOrder


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

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     search_fields = ("customer_name",)
    
#     list_display = ("customer_name", "id","payment_type", "quantity", "created", "status", "products", "product_owner", "payer_email", "payer_name", "payer_id", "purchase_amount")




@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    search_fields = ("customer_name",)
    
    list_display = ("customer_name", "id","payment_type", "created", "total_purchase_amount")


@admin.register(VendorOrder)
class VendorOrderAdmin(admin.ModelAdmin):
    search_fields = ("payee_name",)
    
    list_display = ("payee_name", "id","payment_type", "quantity", "created", "status", "products", "payer_email", "payer_name", "payer_id", "purchase_amount", "customer")



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ( "id", "vendor", "name", "category", "sdg_goals")