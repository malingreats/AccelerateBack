from django.contrib import admin
from .models import Profile, BillingAddress
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("bio",)
    
    list_display = ("id", "user", "full_name", "phone", "location", "is_staff", "is_vendor", "is_customer")


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = ("id", "name", "building", "street", "city", "state", "country", "post", "isDefault" )




