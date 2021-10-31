from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("bio",)
    
    list_display = ("user", "full_name", "phone", "location", "is_staff", "is_vendor", "is_customer")







