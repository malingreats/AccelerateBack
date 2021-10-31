from django.urls import path
from .views import RegisterView, ProfileView, ProfilesView, VendorProfilesView

urlpatterns = [
	path('register/', RegisterView.as_view(), name='register'),
	path('profiles', ProfilesView.as_view(), name='profile'),
	path('vendor_profiles', VendorProfilesView.as_view(), name='vendor_profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]