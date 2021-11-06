from django.urls import path
from .views import RegisterView, ProfileView, ProfilesView, VendorProfilesView, DeleteUserView, RetrieveUserView, BillingAddressView

urlpatterns = [
	path('register/', RegisterView.as_view(), name='register'),
	path('delete/<str:pk>', DeleteUserView.as_view(), name='delete'),
	path('retrieve-user/<str:pk>', RetrieveUserView.as_view(), name='retrieve-user'),
	path('address/', BillingAddressView.as_view(), name='address'),
	path('address/<str:pk>', BillingAddressView.as_view(), name='address'),
	path('profiles', ProfilesView.as_view(), name='profile'),
	path('vendor_profiles/', VendorProfilesView.as_view(), name='vendor_profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]